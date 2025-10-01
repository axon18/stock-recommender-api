
# main.py: FastAPI app that returns a recommendation for a stock
main_code = '''
from fastapi import FastAPI, Query
from pydantic import BaseModel
import random

app = FastAPI()

class Recommendation(BaseModel):
    action: str
    probability: float
    reason: str

@app.get("/recommend", response_model=Recommendation)
def recommend_stock(symbol: str = Query(..., description="Stock symbol, e.g. AAPL")):
    # Simulated logic for demonstration
    actions = ["Comprar", "Vender", "Manter"]
    action = random.choice(actions)
    probability = round(random.uniform(80, 95), 2)
    reason = "Análise técnica e tendência histórica indicam esta recomendação."

    return Recommendation(action=action, probability=probability, reason=reason)
'''
