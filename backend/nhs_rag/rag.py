from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.tools import tool
from langgraph.graph import  MessagesState, StateGraph, START
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient
import os 
from langgraph.checkpoint.memory import MemorySaver
# language model, used for text generation
llm = ChatOpenAI(model="gpt-3.5-turbo")

# embeddings model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1536)

# documents store init
MONGODB_ATLAS_CLUSTER_URI = os.getenv('MONGODB_ATLAS_CLUSTER_URI')

DB_NAME = "nhs_conditions_A_Z"
COLLECTION_NAME = "conditions"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "conditions_index"

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

# Retrieves relavant documents given a query
# this tool is used by the llm
@tool(response_format="content_and_artifact")
def retrieve(query: str):
    """
    Retrieve context information related to a query.
    
    Args:
        query - The query to search
    
    """
    retrieved_docs = vector_store.similarity_search(query, k=5)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


# Step 1: Generate an AIMessage that may include a tool-call to be sent.
def query_or_respond(state: MessagesState):
    """Generate tool call for retrieval or respond."""
    llm_with_tools = llm.bind_tools([retrieve])
    response = llm_with_tools.invoke(state["messages"])

    # MessagesState appends messages to state instead of overwriting
    return {"messages": [response]}


# Step 2: Execute the retrieval.
tools = ToolNode([retrieve])

# Step 3: Generate a response using the retrieved content.
def generate(state: MessagesState):
    """Generate answer."""
    # Get generated ToolMessages
    recent_tool_messages = []
    for message in reversed(state["messages"]):
        if message.type == "tool":
            recent_tool_messages.append(message)
        else:
            break
    tool_messages = recent_tool_messages[::-1]

    # Format into prompt
    docs_content = "\n\n".join(doc.content for doc in tool_messages)    
    
    system_prompt_content = f"""
        You are a healthcare assistant designed to provide concise and accurate medical advice to users about their health concerns. You will be provided with relevant documents from the NHS A-Z Health Conditions website. Each document includes its source URL and page title. 

        Your responsibilities include:
        1. Offering medical advice based on the provided context.
        2. Suggesting possible treatments, self-care options, or next steps.
        3. Advising the user on whether they should consider consulting a GP.

        Always base your response on the documents provided and ensure your answer is helpful and clear. Include the source URL at the end of your response.

        Input Details:
        - **Contextual Information**: {docs_content}


        Output Requirements:
        1. Provide a concise response addressing the user's query.
        2. Include actionable advice, such as suggested treatments or whether to seek medical attention.
        3. Append the source URL(s) from the relevant document(s) at the end of your response.
        """

    
    
    conversation_messages = [
        message
        for message in state["messages"]
        if message.type in ("human", "system")
        or (message.type == "ai" and not message.tool_calls)
    ]
    prompt = [SystemMessage(system_prompt_content)] + conversation_messages

    # Run
    response = llm.invoke(prompt)
    return {"messages": [response]}

graph_builder = StateGraph(MessagesState)

graph_builder.add_node(query_or_respond)
graph_builder.add_node(tools)
graph_builder.add_node(generate)

graph_builder.set_entry_point("query_or_respond")
graph_builder.add_conditional_edges(
    "query_or_respond",
    tools_condition,
    {END : END, "tools": "tools"}
)

graph_builder.add_edge("tools", "generate")
graph_builder.add_edge("generate", END)

graph = graph_builder.compile(checkpointer=MemorySaver())

