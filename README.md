# 🤖 Agentic AI Chatbot Framework (LangGraph + Streamlit)

An extensible **agentic AI framework** built using **LangGraph**, **LLMs**, and **Streamlit**.  
This project demonstrates how to design AI systems as **graph-based workflows** instead of linear scripts, enabling modular, multi-step, and tool-aware agents.

---

## 📖 About

This project is an **agentic AI chatbot framework** designed to create modular, state-driven AI workflows powered by large language models.

Rather than relying on a single monolithic chatbot, the system models AI behavior as **directed graphs**, where each node performs a specific task such as conversation handling, tool execution, or data processing. This design enables flexible control flow, conditional execution, and multi-step reasoning.

The framework currently supports:
- A **basic conversational chatbot**
- A **tool-enabled chatbot with web search**
- A **multi-step AI news summarization pipeline**

The architecture emphasizes **separation of concerns**, **extensibility**, and **clarity**, making it suitable for experimentation, learning agentic AI patterns, and building scalable AI workflows.

---

## 🏗️ Architecture & Design

The system follows a **graph-based agentic architecture** using LangGraph.

### Core Concepts

- **State-driven execution**  
  All graphs operate on a shared `AgentState`, which carries user input, intermediate results, and final outputs.

- **Graph-based orchestration**  
  AI behavior is represented as a directed graph rather than a linear chain.

- **Node isolation**  
  Each node performs a single responsibility and can be reused across workflows.

---

## 📁 Project Structure

```text
CHATBOT/
│
├── .venv/                     # Virtual environment
├── AInews/                    # Optional experimental module
│
├── src/
│   ├── agentic_ai/
│   │   ├── Graph/             # LangGraph builders & orchestration
│   │   ├── LLM/               # LLM configuration & wrappers
│   │   ├── Nodes/             # Graph nodes (agents/tasks)
│   │   ├── State/             # Shared graph state definitions
│   │   ├── Tools/             # Tool integrations (e.g., web search)
│   │   ├── UI/                # Streamlit UI helpers
│   │   ├── main.py            # Core agentic execution logic
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── app.py                     # Streamlit entry point
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
└── .gitignore
```
  

## 🚀 Start Guide


1. **Clone the Repository**  
    Clone the project and move into the project directory:

    ```bash
    git clone <your-repository-url>
    ```

2. **Install Dependencies**  
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   streamlit run app.py
   ```

Once running, open your browser and navigate to:  http://localhost:8501


---

## 🧪 Development & Customization

This framework is designed to be easily extensible.

To customize:
- Add new agent nodes in `src/agentic_ai/Nodes/`
- Define new workflows in `GraphBuilder`
- Integrate external tools in `src/agentic_ai/Tools/`
- Modify the Streamlit UI for new interactions

---

## 🙏 Acknowledgements

This project is inspired by and built upon the work of the open-source community and the developers behind the tools and libraries used.

Special thanks to:

- **LangGraph** for providing a powerful framework for building graph-based, agentic AI workflows
- **LangChain** for foundational abstractions around LLMs and tool usage
- **Streamlit** for enabling rapid development of interactive AI applications
- The broader **open-source AI community** for shared knowledge, examples, and best practices

Their contributions make projects like this possible.
