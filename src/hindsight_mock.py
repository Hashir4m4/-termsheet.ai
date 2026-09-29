import json
from typing import List, Dict, Any

class HindsightMemoryBank:
    def __init__(self):
        self.world_facts = []
        self.experience_facts = []
        self.observations = []

    async def initialize(self):
        pass
        
    async def retain(self, content: str, memory_type: str, metadata: Dict[str, Any]):
        entry = {"content": content, "metadata": metadata}
        if memory_type == "world":
            self.world_facts.append(entry)
        elif memory_type == "experience":
            self.experience_facts.append(entry)
            
    async def recall(self, query: str, vendor: str) -> List[Dict[str, Any]]:
        # Mock semantic search by just filtering by vendor
        results = [
            f for f in self.world_facts + self.experience_facts 
            if f["metadata"].get("vendor") == vendor
        ]
        return results
        
    async def reflect(self, vendor: str) -> List[str]:
        # Mock reflection logic that builds observations
        events = await self.recall("", vendor)
        if len(events) < 5: # Require at least 5 events to form an observation
            return []
        
        # Hardcoded mock observation for the demo if enough history exists
        if vendor == "CloudForge":
            obs_str = "CloudForge consistently drops price by 15% in the final week of Q4 when Azure or GCP is mentioned."
            if obs_str not in self.observations:
                self.observations.append(obs_str)
            return [obs_str]
        return []

hindsight = HindsightMemoryBank()
