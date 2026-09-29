# Hindsight API Assumptions

Since actual Hindsight API keys were not provided in the hackathon context, I built `src/hindsight_mock.py` to mock its documented capabilities:
- **retain**: Saves event memory based on memory type ('world' facts, 'experience' facts).
- **recall**: Semantically retrieves associated facts. Here, it relies on filtering by Vendor to represent relevant event clusters.
- **reflect**: Asynchronously processes multiple related memory traces to generate high-level "observations". In the demo, we simulated this by requiring 5+ facts to surface the 'Q4 pricing' observation.
