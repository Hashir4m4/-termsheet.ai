# Termsheet.ai ⚡

> **AI Agent for Longitudinal Vendor Intelligence & Procurement Decisions**

Termsheet.ai is an AI-powered procurement agent designed to preserve and reason over historical vendor interactions, negotiation patterns, pricing behavior, and renewal decisions.

Instead of treating every procurement cycle as a new conversation, Termsheet.ai builds a **longitudinal memory of vendor behavior** and uses that context to help procurement teams make better decisions.

---

## 🎯 Problem

Procurement teams often lose critical institutional knowledge when:

- Vendor negotiations span multiple years
- Procurement employees change roles
- Previous concessions are forgotten
- Vendor pricing patterns are not tracked
- Negotiation tactics are scattered across documents and conversations

This creates an **organizational memory problem**.

### Our Solution

Termsheet.ai acts as an **AI procurement intelligence agent** that:

1. Captures historical vendor interactions
2. Stores relevant information in long-term memory
3. Recalls previous negotiations during new procurement cycles
4. Identifies recurring vendor behavior
5. Reflects on historical outcomes
6. Provides context-aware negotiation intelligence

---

# 🧠 Agent Architecture

```text
                    ┌─────────────────────┐
                    │    Procurement User │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Agent Interface  │
                    │      HTML / JS      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    │  Agent Orchestrator │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌───────────┐    ┌───────────┐    ┌───────────┐
        │  Retain   │    │  Recall   │    │  Reflect  │
        │  Memory   │    │  Memory   │    │  Memory   │
        └───────────┘    └───────────┘    └───────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Vendor Behavior     │
                    │ Intelligence Layer  │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Contextual Agent    │
                    │ Recommendation      │
                    └─────────────────────┘
