from fastapi import FastAPI
from pydantic import BaseModel
from random import choice, uniform

app = FastAPI()

class RecommendationResponse(BaseModel):
    symbol: str
    action: str
    probability: float

@app.get("/recommend", response_model=RecommendationResponse)
def recommend(symbol: str):
    action = choice(["Comprar", "Vender", "Manter"])
    probability = round(uniform(80, 95), 2)
    return RecommendationResponse(symbol=symbol, action=action, probability=probability)
