from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/predict/{symbol}")
def predict(symbol: str):
    # Load your ensemble model, run prediction
    return {"symbol": symbol, "predicted_price": ..., "actual_price": ..., "signal": "BUY/SELL/HOLD", "sentiment_score": ..., "confidence": ..., "technical_indicators": {"rsi": ..., "macd": ..., ...}}

@app.get("/prices/{symbol}")
def prices(symbol: str, days: int = 90):
    # Pull from Alpha Vantage
    return [{"date": ..., "open": ..., "high": ..., "low": ..., "close": ..., "volume": ...}]

@app.get("/news/{symbol}")
def news(symbol: str):
    # Scrape + VADER sentiment
    return [{"title": ..., "source": ..., "url": ..., "published_at": ..., "sentiment": ...}]
