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
 │ - pymongo (Python) or        │
 │   official MongoDB drivers   │
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
