import asyncio
import os
import sys
from hindsight_client import Hindsight

async def run_smoke_test():
    print("--- STARTING REAL HINDSIGHT SMOKE TEST ---")
    hs = Hindsight(base_url="http://localhost:8889")
    bank_id = "test-smoke-bank"
    
    # 1. Retain
    try:
        await hs.acreate_bank(bank_id, name="Test Smoke Bank")
    except Exception:
        pass
        
    async def safe_retain(content, metadata):
        for _ in range(5):
            try:
                await hs.aretain(bank_id, content=content, metadata=metadata)
                return
            except Exception as e:
                print(f"Retrying retain: {e}")
                await asyncio.sleep(5)
                
    print("RETAINING evidence...")
    await safe_retain("SmokeTestVendor offered $1000 in 2024.", {"vendor": "SmokeTestVendor", "year": "2024"})
    await safe_retain("SmokeTestVendor dropped price to $900 in 2025.", {"vendor": "SmokeTestVendor", "year": "2025"})
    
    # Wait for embeddings
    await asyncio.sleep(2)
    
    # 2. Recall
    print("RECALLING evidence...")
    recall_res = await hs.arecall(bank_id, query="SmokeTestVendor pricing")
    recall_texts = [r.text for r in recall_res.results]
    print(f"REAL_RECALL_OUTPUT = {recall_texts}")
    
    # 3. Reflect
    print("REFLECTING on evidence...")
    try:
        reflect_res = await hs.areflect(bank_id, query="What is the pricing pattern for SmokeTestVendor?")
        if hasattr(reflect_res, 'observations') and reflect_res.observations:
            reflect_texts = [o.text for o in reflect_res.observations]
        else:
            reflect_texts = []
        print(f"REAL_REFLECT_OUTPUT = {reflect_texts}")
    except Exception as e:
        print(f"REFLECT FAILED (Likely 429 Quota): {e}")

if __name__ == "__main__":
    asyncio.run(run_smoke_test())
