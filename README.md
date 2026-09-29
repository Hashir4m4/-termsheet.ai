# Termsheet.ai

**Problem:** Procurement teams lose historical context of vendor negotiation tactics across multi-year renewals.
**Solution:** Termsheet.ai utilizes Vectorize Hindsight memory to build a longitudinal behavior profile on vendors.

### Architecture
- **Frontend:** Vanilla HTML/JS styled natively for zero-friction hackathon demos.
- **Backend:** FastAPI for high-performance python API serving.
- **Memory:** Simulated Hindsight memory service implementing `retain`, `recall`, and `reflect`.

### Run it
1. `pip install fastapi uvicorn pydantic`
2. `python -m uvicorn src.main:app --port 8000`
3. Visit `http://localhost:8000/static/index.html`

### Tests
- **API Tests:** Run `pytest tests/` (Requires `pytest`, `httpx`).
- **E2E Tests:** Run `node tests/playwright_test.js` (Requires `playwright`).

*Disclaimer: This project uses synthetic negotiation data for demonstration purposes.*
