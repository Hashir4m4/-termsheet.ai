import asyncio
from src.memory_provider import memory
from datetime import datetime

async def _retain_with_retry(*args, **kwargs):
    for i in range(5):
        try:
            await memory.retain(*args, **kwargs)
            return
        except Exception as e:
            print(f"Retrying retain ({i+1}/5)... error: {e}")
            await asyncio.sleep(2)
    print("Failed to retain after 5 attempts")

async def _reflect_with_retry(*args, **kwargs):
    for i in range(5):
        try:
            await memory.reflect(*args, **kwargs)
            return
        except Exception as e:
            print(f"Retrying reflect ({i+1}/5)... error: {e}")
            await asyncio.sleep(2)

async def seed_data():
    await memory.initialize()
    # Year 1
    await _retain_with_retry("Quote #101: $100k annual", "world", {"vendor": "CloudForge", "date": "2024-11-01", "type": "quote"})
    await _retain_with_retry("Email: We can't do $100k, evaluating Azure.", "experience", {"vendor": "CloudForge", "date": "2024-12-10", "type": "email"})
    await _retain_with_retry("Email: I can drop to $85k if we close by EOY.", "world", {"vendor": "CloudForge", "date": "2024-12-24", "type": "email"})
    await _retain_with_retry("Contract signed for $85k.", "experience", {"vendor": "CloudForge", "date": "2024-12-28", "type": "contract"})
    
    # Year 2
    await _retain_with_retry("Quote #205: $110k annual renewal", "world", {"vendor": "CloudForge", "date": "2025-11-05", "type": "quote"})
    await _retain_with_retry("Email: Azure offered $90k.", "experience", {"vendor": "CloudForge", "date": "2025-12-15", "type": "email"})
    await _retain_with_retry("Email: My VP approved $93.5k (15% off) to match, must sign by Dec 31.", "world", {"vendor": "CloudForge", "date": "2025-12-26", "type": "email"})
    await _retain_with_retry("Contract signed for $93.5k.", "experience", {"vendor": "CloudForge", "date": "2025-12-29", "type": "contract"})
    
    # Ensure reflect runs to generate the observation
    # await _reflect_with_retry("CloudForge")

def get_vendors():
    return ["CloudForge", "MetricFlow"]
