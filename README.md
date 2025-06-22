# 📚 Automated Book Publication Workflow

This project is a full-stack automation pipeline designed to fetch content from a given web URL, apply AI-based transformation (writing and reviewing), allow multiple rounds of human-in-the-loop editing, and version control the final content using ChromaDB and intelligent retrieval strategies.

> ✅ Built with production-grade tools, showcasing scraping, LLM integration (via Groq API), versioning, and agent communication.

---

## 🎯 Objective

- Fetch a chapter from an online book (Wikisource)
- Use AI to "spin" and rewrite the content
- Review and refine the result with another AI agent
- Allow human edits before finalizing
- Save and version the final chapter
- Retrieve saved versions using intelligent search

---

## 🛠️ Tech Stack

| Component            | Tool/Library               |
|---------------------|----------------------------|
| Language            | Python                     |
| Scraping & Screenshot | Playwright                |
| AI Agents (Writer/Reviewer) | Groq (OpenAI-compatible API) |
| Environment Management | `dotenv`, `venv`         |
| Versioning DB       | ChromaDB (DuckDB+Parquet)  |
| Search (RL-inspired)| Vector-based with Chroma   |

---

## 🧠 Agent Workflow

```
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│  Web Scraper         │    │   AI Writer Agent    │    │  AI Reviewer Agent   │
│  (Playwright)        │───►│   (Groq - Mixtral)   │───►│   (Groq - Mixtral)   │
└──────────────────────┘    └──────────────────────┘    └──────────────────────┘
                                       │
                                       ▼
                          ┌──────────────────────────┐
                          │ Human-in-the-loop Editor │
                          │   (via CLI or GUI)       │
                          └──────────────────────────┘
                                       │
                                       ▼
                          ┌──────────────────────────┐
                          │ Save Final to ChromaDB   │
                          │  + RL-Based Retrieval    │
                          └──────────────────────────┘
```


---

## 📦 Project Structure

```
automated-book-publisher/
│
├── main.py                       # Master pipeline
├── requirements.txt              # Dependencies
├── .env                          # API keys (excluded from Git)
│
├── scraper/
│   ├── fetch.py                  # Web scraping logic
│   └── screenshots.py            # Screenshot capture
│
├── agents/
│   ├── writer.py                 # GROQ-based AI writer
│   ├── reviewer.py               # GROQ-based reviewer
│   ├── groq_client.py            # Shared GROQ wrapper
│   └── human_loop.py             # User input for editing
│
├── versioning/
│   ├── db.py                     # Save and retrieve from Chroma
│   └── retrieval.py              # Search implementation
│
├── data/
│   ├── raw/                      # Raw scraped content
│   ├── processed/                # AI + human outputs (saved)
│   └── screenshots/              # Captured chapter screenshots
│
├── utils/
│   └── logger.py                 # Optional logging
│
└── test/
    └── test_workflow.py          # Test and validation script
```

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

### 2. Add Your GROQ API Key

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Or export it temporarily:

```bash
export GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Main Pipeline

```bash
python3 main.py
```

You’ll get:

* ✍️ `spun_version.txt`
* 🧐 `reviewed_version.txt`
* 🧠 `final_version.txt`
* 💾 Version saved in ChromaDB
* 🖼 Screenshot in `data/screenshots/`

---

## 🧪 Sample Output (files generated)

```
data/
├── processed/
│   ├── spun_version.txt          # AI rephrased version
│   ├── reviewed_version.txt      # Edited for quality
│   └── final_version.txt         # Human approved
├── screenshots/
│   └── chapter1.png              # Full-page screenshot
```

---

## 🧠 Why This Project Matters

This system reflects real-world publishing and editorial workflows, with:

* **Multi-agent collaboration** (Writer → Reviewer → Human)
* **Content version control**
* **Smart retrieval using embeddings**
* **Hands-on use of LLMs in production pipelines**


Built with ❤️ by Sneha P Pratap
