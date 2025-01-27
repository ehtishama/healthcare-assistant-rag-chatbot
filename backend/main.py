from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from nhs_rag import invoke_rag


class MessageQuery(BaseModel):
    message: str
    thread_id: str | None = None


app = FastAPI()

origins = [
    "*"

]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/query_health_condition/")
async def query_health_condition(query: MessageQuery):
    message = query.message.lower()
    thread_id = query.thread_id

    response = {"message": invoke_rag(message, thread_id)}

    return response
