**Traversaal-x-Optimized-AI-Hackathon**

**An autonomous AI agent that audits educational content for outdated, redundant, or missing materials — built with FastAPI for the Traversaal x Optimized AI Hackathon. Designed to integrate effortlessly with Notion, Google Drive, and LMS platforms. Smart. Modular. Ready for scale.**

**Our Approach**

**Problem:** Education teams struggle with manual updates of content and version control.

**Solution:** Automate this with a smart agent that scans documents and gives update suggestions.

**Strategy:** Design a pluggable agent that works with multiple data sources and can be extended to NLP tasks such as summarization, gap detection, or question generation.

**Project Overview**

The **Content Analysis Agent** is built for EdTech teams looking to:

- **Automate audits** of their course materials
- **Detect outdated, redundant, or missing content**
- **Integrate seamlessly** with Google Drive, Notion, LMS, etc. (OAuth-ready)
- Work with **adaptive workflows** using a flexible agentic backend

Built with :

- **FastAPI** for high-performance backend
- **Python** for core logic
- Integrations with **LangChain**, **OAuth**, and frontends like **Lovable** or **Zapier**

💡 **Bonus: Built with AgentPro by Traversaal**

This project integrates [AgentPro](https://github.com/traversaal-ai/AgentPro), Traversaal's open-source, production-grade framework for AI agents.

We used AgentPro to structure our content audit agent in modular, testable steps :

- **Step-based execution**
- **Context-aware chaining**
- **FastAPI-compatible and scalable**

📂 **File Structure Explained**

app/main.py: FastAPI entry point

routes/: API endpoints

services/: Core logic for document analysis

models/: Data models and schemas

utils/: File parsing or helper functions

tests/: Unit tests

**Agentic Architecture**

 ![Agentic Architecture](assets/architecture.png)
