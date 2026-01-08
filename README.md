# Agentic Banking Chatbot using CrewAI

## Overview
This project demonstrates a production-ready banking chatbot built using
CrewAI, Retrieval-Augmented Generation (RAG), and Large Language Models.

## Architecture
- Multi-agent orchestration using CrewAI
- RAG with FAISS vector store
- FastAPI backend
- Dockerized deployment

## Use Case
Handles customer queries related to:
- Account information
- Banking policies
- Loan and interest rates
- Compliance-safe responses

## Tech Stack
- CrewAI
- LangChain
- FAISS
- OpenAI / LLaMA
- FastAPI
- Docker

## How to Run
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
