from fastapi import FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI()

API_KEY = "guvi-honeypot-key"

@app.get("/")
def root():
    return {"status": "Agentic Honeypot running"}

# ✅ GET + POST dono allow
@app.get("/analyze")
@app.post("/analyze")
def analyze(x_api_key: Optional[str] = Header(None)):
    # API key check
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "scam_detected": True,
        "agent_reply": "Payment se pehle bank ka official confirmation chahiye.",
        "extracted_data": {
            "upi_ids": [],
            "bank_accounts": [],
            "phishing_links": []
        }
    }
