# Termsheet.ai - Skill Routing

| Capability Required | Skill Name | Path | Instructions Applied | Phase Applied | Implementation Affected | Verification Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Backend API | `fastapi-pro` | `C:\Users\abdul\.gemini\antigravity-cli\skills\fastapi-pro` | Followed FastAPI routing and standard app configuration | PLAN/IMPLEMENT | `src/main.py` | Pytest and HTTP tests passed |
| Testing | `pytest-skill` | `C:\Users\abdul\.gemini\antigravity-cli\skills\pytest-skill` | Used standard Pytest assertions and TestClient for endpoints | TEST | `tests/test_api.py` | Command `pytest tests/` executed |
| E2E Testing | `playwright-skill` | `C:\Users\abdul\.gemini\antigravity-cli\skills\playwright-skill` | Automated browser navigation to test frontend functionality | TEST | `tests/playwright_test.js` | Node output showed 100% success |
| UX/Frontend | `USE_NATIVE_REASONING` | N/A | Created premium UI layout with standard HTML/JS | IMPLEMENT | `src/static/index.html` | Playwright loaded profile successfully |
