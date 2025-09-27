# 🌐 Web Navigator AI Agent

## 📌 Overview
The **Web Navigator AI Agent** is a prototype system that takes natural language instructions and autonomously drives the web using:
- 🧠 Local LLM (via Ollama)
- 🌍 Browser automation (Playwright)
- ⚡ Python backend (Flask)
- 🎨 React frontend

Example command:
> "Search for laptops under 50k and list top 5"

The agent will:
1. Parse the instruction using a local LLM.
2. Control the browser to search and extract data.
3. Return structured results (title, link, snippet, screenshot).

---

## 🚀 Features
- Instruction parsing via local LLM.
- Browser automation with Playwright.
- Structured results with screenshots.
- React-based GUI.
- Fully local setup (no cloud dependency).

---

## 🛠️ Tech Stack
- **Frontend:** React + Vite
- **Backend:** Flask + Python
- **Automation:** Playwright
- **LLM:** Ollama (LLaMA 3.2 7B)
- **Interface:** REST API + Web UI

---

## 📂 Project Structure
Web Navigator AI Agent/
├── backend/ # Flask + Playwright backend
├── frontend/ # React frontend
├── .env.example # Example environment variables
├── .gitignore
├── README.md
├── CONTRIBUTING.md
└── LICENSE