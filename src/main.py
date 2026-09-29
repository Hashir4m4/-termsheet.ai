from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.memory_provider import memory
from src.data_generator import seed_data, get_vendors

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

class StrategyRequest(BaseModel):
    vendor: str
    current_offer: str
    use_memory: bool = True

@app.on_event("startup")
async def startup_event():
    import os
    if os.getenv("MEMORY_PROVIDER", "mock") == "mock":
        try:
            await seed_data()
        except Exception as e:
            print(f"Failed to seed data: {e}")

@app.get("/api/vendors")
async def list_vendors():
    return {"vendors": get_vendors()}

@app.get("/api/vendor/{vendor}/profile")
async def vendor_profile(vendor: str):
    history = await memory.recall("", vendor)
    observations = await memory.reflect(vendor)
    return {
        "vendor": vendor,
        "history_count": len(history),
        "history": history,
        "observations": observations
    }

@app.post("/api/strategy")
async def generate_strategy(req: StrategyRequest):
    if not req.use_memory:
        return {
            "recommendation": "Standard counter-offer: request a 5-10% discount.",
            "reasoning": "Without historical context, 5-10% is a safe industry average for software renewals.",
            "evidence": [],
            "mode": "Control"
        }
    
    # Use memory
    obs = await memory.reflect(req.vendor)
    history = await memory.recall("", req.vendor)
    
    if len(history) > 0:
        # Dynamically build the recommendation from real Hindsight observation
        reasoning_text = " ".join(obs) if obs else "No clear pattern observed yet."
        return {
            "recommendation": f"Based on institutional memory, follow the pattern observed: {reasoning_text[:100]}...",
            "reasoning": reasoning_text,
            "evidence": history, # Show all recalled evidence
            "mode": "Memory"
        }
    
    return {
        "recommendation": "Insufficient historical data. Request 5%.",
        "reasoning": "Hindsight memory does not contain enough events to form a behavioral observation.",
        "evidence": [],
        "mode": "Memory"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
