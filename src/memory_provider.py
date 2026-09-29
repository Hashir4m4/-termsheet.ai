import os
from src.hindsight_mock import hindsight as mock_hindsight

class RealHindsightProvider:
    def __init__(self):
        from hindsight_client import Hindsight
        self.hs = Hindsight(base_url="http://localhost:8889")
        self.bank_id = "nexus-procurement"

    async def initialize(self):
        try:
            await self.hs.acreate_bank(self.bank_id, name="Nexus Procurement")
        except Exception:
            pass

    async def retain(self, content, type_val, metadata):
        await self.hs.aretain(self.bank_id, content=content, metadata=metadata)

    async def recall(self, query, vendor):
        res = await self.hs.arecall(self.bank_id, query=query + " " + vendor)
        return [{"content": r.text, "type": r.type, "metadata": r.metadata} for r in res.results]

    async def reflect(self, vendor):
        import asyncio
        for attempt in range(2):
            try:
                res = await asyncio.wait_for(
                    self.hs.areflect(self.bank_id, query=f"What is the negotiation behavior or pattern for {vendor}?"),
                    timeout=5.0
                )
                if hasattr(res, 'observations') and res.observations:
                    return [o.text for o in res.observations]
                break
            except Exception as e:
                print(f"Reflect LLM call failed on attempt {attempt+1}: {e}")
                if attempt == 0:
                    await asyncio.sleep(2)
        
        recall_res = await self.hs.arecall(self.bank_id, query=f"negotiation behavior and patterns for {vendor}")
        return ["[FALLBACK: Reflection temporarily unavailable. Raw memory:] " + r.text for r in recall_res.results[:3]]

class MemoryProvider:
    def __init__(self):
        self.mode = os.getenv("MEMORY_PROVIDER", "mock")
        if self.mode == "hindsight":
            self.provider = RealHindsightProvider()
        else:
            self.provider = mock_hindsight
            
    async def initialize(self):
        if self.mode == "hindsight":
            await self.provider.initialize()
        else:
            await self.provider.initialize()
            
    async def retain(self, content, type_val, metadata):
        return await self.provider.retain(content, type_val, metadata)

    async def recall(self, query, vendor):
        return await self.provider.recall(query, vendor)
        
    async def reflect(self, vendor):
        return await self.provider.reflect(vendor)

memory = MemoryProvider()
