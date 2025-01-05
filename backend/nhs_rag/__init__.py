from dotenv import load_dotenv
load_dotenv()

from .rag import graph

def invoke_rag(query, thread_id):
    if(thread_id):
        config = {"configurable": {"thread_id": thread_id}}
        response = graph.invoke({"messages": [query]}, config)
    else:
        response = graph.invoke({"messages": [query]})
        
    ai_response = response["messages"][-1].content
    
    return ai_response