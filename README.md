# 🌐 Web Navigator AI Agent

## 📌 Problem Statement
The **Web Navigator AI Agent** aims to revolutionize web interactions by building an autonomous system capable of understanding natural language instructions and executing them on a local computer. The agent leverages a locally running Large Language Model (LLM) for instruction parsing and planning, combined with browser automation to perform web tasks such as searching, clicking, form-filling, and extracting structured information.  

**Goal:** Provide a fully local, intelligent assistant that can navigate the web autonomously, perform multi-step reasoning, and return clean, structured outputs without relying on cloud services.

---

## 💡 Proposal & Prototype Plan
The proposed system will have the following capabilities:

1. **Instruction Understanding:**  
   - Use a locally hosted LLM (e.g., Ollama LLaMA 3.2 7B) to interpret user commands and plan task execution.  
   - Convert natural language instructions into actionable steps for the browser.

2. **Browser Automation:**  
   - Use Playwright to control a headless or VM-based browser.  
   - Automate searches, clicks, text extraction, and form submissions.  

3. **Task Execution & Multi-Step Reasoning:**  
   - Support multi-step instructions and task chaining (e.g., search → filter → extract).  
   - Implement error handling, retries, and fallback strategies to improve reliability.  

4. **Output & Data Management:**  
   - Return structured results including titles, links, snippets, and optional screenshots.  
   - Save/export task results in CSV or JSON formats for further analysis.

5. **User Interaction:**  
   - Provide a simple GUI using React + Flask for easy interaction.  
   - Optional voice input for natural command entry.  

**Prototype Steps:**  
- Build a local LLM interface to parse instructions.  
- Integrate Playwright for browser automation.  
- Develop backend (Flask) to handle requests and orchestrate tasks.  
- Build a frontend (React) for intuitive interaction and displaying results.  

---

## 🚀 Features
- **Instruction Parsing:** Understand natural language instructions via local LLM.  
- **Autonomous Browser Control:** Automate web tasks including search, click, and data extraction.  
- **Structured Outputs:** Return clean, structured data with optional screenshots.  
- **Multi-Step Task Handling:** Chain multiple tasks in a single command.  
- **Error Handling & Retry Mechanism:** Robust execution with fallback options.  
- **Task Memory:** Remember previous instructions for continuity.  
- **User-Friendly GUI:** React-based interface with REST API backend.  
- **Local Setup:** Fully functional without cloud dependency.  
- **Export Results:** Save task outcomes in CSV/JSON formats.  
- **Voice Input (Optional):** Control the agent via voice commands.

---

## 🛠️ Tech Stack
| Layer | Technology |
|-------|------------|
| **Frontend** | React + Vite |
| **Backend** | Python + Flask |
| **Browser Automation** | Playwright |
| **LLM** | Ollama (LLaMA 3.2 7B) |
| **Interface** | REST API + Web UI |
| **Environment Management** | Virtualenv / .env |

---

## 📂 Project Structure
Web Navigator AI Agent/
├── backend/ # Flask backend + Playwright scripts
├── frontend/ # React frontend
├── .env.example # Example environment variables
├── .gitignore
├── README.md
├── CONTRIBUTING.md
└── LICENSE

---
```yaml

## 👥 Team Contributions
| Member | Role | Contribution |
|--------|------|-------------|
| Rawhan Ramzi | Project Lead | Defined problem statement, oversaw LLM integration, coordinated tasks. |
| Sumanth | Backend Developer | Implemented Flask API, integrated Playwright automation, handled data parsing. |
| Harish | Frontend Developer | Developed React UI, designed dashboards for structured outputs. |
| Rajesh | LLM Specialist | Configured and fine-tuned local LLaMA model for instruction parsing. |


---

## 📈 Vision
The **Web Navigator AI Agent** is envisioned as the foundation for autonomous web agents that can act intelligently without cloud reliance. Future enhancements may include complex task orchestration, integration with local databases, adaptive learning from user behavior, and multi-agent collaboration.

---

## ⚡ Getting Started
1. Clone the repository:  
   ```bash
   git clone https://github.com/Rawhan1819/Web-Navigator-AI-Agent.git

2. Set up backend environment:
    cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Configure .env with required keys (e.g., Ollama API).

4. Run Flask backend and React frontend:
      # Backend
       python app.py
       # Frontend
       cd ../frontend
       npm install
       npm run dev
5. Interact with the agent via the web GU