import asyncio
from hindsight_client import Hindsight

async def main():
    # The client connects to the server
    hs = Hindsight(base_url="http://localhost:8889")
    try:
        bank = await hs.acreate_bank(bank_id="nexus-procurement", name="Nexus Procurement Labs")
        print(f"Created bank: {bank.bank_id}")
        
        res = await hs.aretain(
            bank_id=bank.bank_id,
            content="Quote #101: $100k annual for CloudForge",
            metadata={"vendor": "CloudForge", "type": "quote"}
        )
        print("Retain response:", res)
        
        recall_res = await hs.arecall(bank_id=bank.bank_id, query="CloudForge quote")
        print("Recall response:", recall_res)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
