from dotenv import load_dotenv
load_dotenv()

from .rag import graph

def invoke_rag(query):
    response = graph.invoke({"messages": [query]})
    ai_response = response["messages"][-1].content
    
    return ai_response