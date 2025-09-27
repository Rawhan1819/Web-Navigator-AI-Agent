 ┌──────────────┐
 │   User       │
 │ (Frontend)   │
 │ Command Input│
 └──────┬───────┘
        │
        ▼
 ┌────────────────────────┐
 │ React Frontend (App.jsx)│
 │ - Sends command via     │
 │   POST /execute         │
 │ - Shows results cards   │
 └─────────┬──────────────┘
           │
           ▼
 ┌─────────────────────────┐
 │  Flask Backend (main.py)│
 │ - Receives command      │
 │ - Calls DuckDuckGo      │
 │ - Fetches URLs + Snippets│
 │ - Calls Playwright for  │
 │   screenshots/thumbnails│
 └─────────┬───────────────┘
           │
           ▼
 ┌─────────────────────────┐
 │  LLM Agent (LLMAgent)  │
 │ - Plan steps for browser│
 │   actions from command  │
 └─────────┬───────────────┘
           │
           ▼
 ┌─────────────────────────┐
 │ Web Agent (WebAgent)    │
 │ - Executes plan in      │
 │   headless browser      │
 │ - Extracts text, clicks │
 │ - Takes screenshots     │
 └─────────┬───────────────┘
           │
           ▼
 ┌─────────────────────────┐
 │ Backend Response JSON   │
 │ - List of results:      │
 │   title, link, snippet, │
 │   screenshot, thumbnail │
 └─────────┬───────────────┘
           │
           ▼
 ┌─────────────────────────┐
 │ Frontend Displays Cards │
 │ - Thumbnail image       │
 │ - Title + clickable link│
 │ - Snippet preview       │
 └─────────────────────────┘
# ðŸŒ Web Navigator AI Agent

## ðŸ“Œ Overview
The **Web Navigator AI Agent** is a prototype system that takes natural language instructions and autonomously drives the web using:
- ðŸ§  Local LLM (via Ollama)
- ðŸŒ Browser automation (Playwright)
- âš¡ Python backend (Flask)
- ðŸŽ¨ React frontend

Example command:
> "Search for laptops under 50k and list top 5"

The agent will:
1. Parse the instruction using a local LLM.
2. Control the browser to search and extract data.
3. Return structured results (title, link, snippet, screenshot).

---

## ðŸš€ Features
- Instruction parsing via local LLM.
- Browser automation with Playwright.
- Structured results with screenshots.
- React-based GUI.
- Fully local setup (no cloud dependency).

---

## ðŸ› ï¸ Tech Stack
- **Frontend:** React + Vite
- **Backend:** Flask + Python
- **Automation:** Playwright
- **LLM:** Ollama (LLaMA 3.2 7B)
- **Interface:** REST API + Web UI

---

## ðŸ“‚ Project Structure

# Web-Navigator-AI-Agent
