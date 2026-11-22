# AI Support Desk

**AI Support Desk** is an AI-powered backend service designed to process customer support tickets and related documents. Built as a human-in-the-loop assistant, its primary goal is to help customer support agents handle routine preparation work—reading lengthy messages, extracting key details, and drafting responses—without replacing human judgment or making risky automated decisions.

## Overview

Customer support agents spend a significant amount of time parsing incoming messages of varying lengths, identifying the core issue, and gathering missing context before replying. AI Support Desk streamlines this workflow by automating initial triage and preparation, leaving the final review and decision-making entirely to the support operator.

## Key Features

- **Ticket Ingestion:** Accepts raw customer inquiry text for processing.
- **Smart Summarization:** Generates concise summaries of lengthy or complex customer messages.
- **Entity & Gap Extraction:** Automatically identifies the ticket category, key facts, and missing information required to resolve the issue.
- **Response Drafting:** Suggests context-aware draft replies for the operator to review and edit.
- **Conversation Awareness:** Takes previous dialogue history into account for accurate context tracking.
- **Multimodal Document Analysis:** Parses and analyzes attached files, including **PDF**, **DOCX**, and **images**.
- **Controlled Tool Execution:** Retrieves authorized data using strictly scoped, permission-limited tools.
- **REST API:** Built on **FastAPI** for high performance, clean architecture, and automatic interactive API documentation.
- **Observability & Error Handling:** Returns clear, structured error responses and logs safe, sanitized diagnostic data.

## Philosophy: Assist, Don't Replace

The core principle of this project is **assistance**. AI Support Desk acts as a co-pilot for support specialists:
- It **does** organize information, highlight critical details, and accelerate response preparation.
- It **does not** autonomously send messages to customers or execute high-risk actions on behalf of the agent.

## Tech Stack

- **Framework:** FastAPI (Python)
- **API Architecture:** RESTful API
- **Supported Attachments:** PDF, DOCX, Images

## Getting Started

```bash
# Clone the repository
git clone [https://github.com/rivka-levit/ai-support-desk.git](https://github.com/rivka-levit/ai-support-desk.git)
cd ai-support-desk

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```

## License
This project is developed for educational purposes.
