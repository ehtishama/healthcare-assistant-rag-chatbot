from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class MessageQuery(BaseModel):
    message: str


app = FastAPI()


hardcoded_responses = {
    "fever": "You might be experiencing the early stages of flu or a viral infection.",
    "headache": "It could be a migraine, stress, or tension-related headache.",
    "cough": "This could indicate a respiratory issue, such as cold, flu, or COVID-19.",
    "fatigue": "Fatigue can result from various causes like poor sleep, stress, or an underlying condition."
}


@app.post("/query_health_condition/")
async def query_health_condition(query: MessageQuery):
    message = query.message.lower()
    
    
    response = {"message": "Sorry, I couldn't understand your symptoms. Could you please provide more details?"}
    
    
    for symptom, recommendation in hardcoded_responses.items():
        if symptom in message:
            response = {"message": recommendation}
            break
    
    return response
