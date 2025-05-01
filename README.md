
 # 🧠 Talk_to_DB – Natural Language Interface to MongoDB

**Talk_to_DB** is an intelligent interface that lets users query a MongoDB database using plain English. It transforms natural language input into executable MongoDB queries using LLMs like GPT, with schema-awareness, input preprocessing, and secure execution.

---

## 🚀 Features

- Query MongoDB using plain English (via Web UI, CLI, or Chat)
- Input preprocessing (cleanup, NER, date formatting)
- LLM-based query generation (schema-aware)
- Secure MongoDB execution using `pymongo`
- JSON/table display with optional query explanation
- Export results as CSV or via API

---

## 🧱 Architecture Overview

```plaintext
┌────────────────────────┐
│    User Interface (UI) │
│ (Web App / CLI / Chat) │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Input Preprocessing  │
│ (Text cleanup, NER,    │
│  Date formatting, etc) │
└────────────┬───────────┘
             │
             ▼
┌──────────────────────────────┐
│     Prompt Builder / LLM     │
│ - Inject schema (optional)   │
│ - Call GPT / Local LLM       │
│ - Output: MongoDB query      │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│ MongoDB Query Executor       │
│ - pymongo or MongoDB driver  │
│ - Run query against DB       │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│      Results Formatter       │
│ - Display JSON / Table       │
│ - Optionally explain query   │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────────┐
│        Output Delivery       │
│ (UI Display, CSV Export, API)│
└──────────────────────────────┘
