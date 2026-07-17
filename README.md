# AI-Based Test Case Generation from Medical Device Manuals

A modular FastAPI backend developed for the **Tri9T AI Internship Assignment**. The application ingests medical device manuals in PDF format, extracts structured document sections, stores multiple document versions, compares revisions, and provides a foundation for AI-assisted software test case generation.

---

## Features

### Implemented

- PDF parsing using **PyMuPDF**
- Automatic document section extraction
- SQLite database integration using **SQLAlchemy**
- Version-based document storage (e.g., v1, v2)
- Section-wise document comparison
- FastAPI REST APIs
- Modular project architecture
- Initial Large Language Model (LLM) integration

### Work in Progress

- Structured JSON validation of LLM responses
- Automated software test case generation
- Stale test detection
- Retry mechanism for invalid LLM output

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| PDF Processing | PyMuPDF (fitz) |
| Validation | Pydantic |
| AI | Groq API (Llama 3.3) |
| API Testing | Swagger UI |

---

## Project Structure

```
Tri9T-AI-Internship/
│
├── app/
│   ├── api/
│   ├── comparison/
│   ├── core/
│   ├── database/
│   ├── llm/
│   ├── models/
│   ├── parser/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── data/
├── generated/
├── scripts/
├── tests/
│
├── documents.db
├── main.py
├── requirements.txt
└── README.md
```

---

# Architecture

```
              PDF Manual
                   │
                   ▼
           PDF Section Parser
                   │
                   ▼
        Structured Document Sections
                   │
                   ▼
            SQLite Database
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 Version Storage      Version Comparison
         │                   │
         └─────────┬─────────┘
                   ▼
              FastAPI APIs
                   │
                   ▼
      LLM Integration (Foundation)
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd Tri9T-AI-Internship
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
GROQ_API_KEY=YOUR_API_KEY
```

---

# Running the Project

### Create the database

```bash
python -m scripts.create_database
```

### Load the first document

```bash
python -m scripts.load_pdf
```

### Start the FastAPI server

```bash
uvicorn main:app --reload
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Available APIs

## 1. Ingest Document

Uploads a PDF, extracts document sections, and stores them in the database under a specified version.

---

## 2. Compare Versions

Compares two stored document versions and classifies sections as:

- Added
- Removed
- Modified
- Unchanged

---

# Design Decisions

The project follows a modular architecture with clear separation of responsibilities.

- **Parser** handles PDF processing and section extraction.
- **Services** manage business logic.
- **Database layer** is isolated using SQLAlchemy.
- **API layer** is responsible only for HTTP request handling.
- **Comparison module** performs version-based section analysis.
- **LLM module** is designed to support future AI-powered test case generation.

This separation improves maintainability, readability, and future extensibility.

---

# Current Status

| Component | Status |
|-----------|--------|
| PDF Parsing | ✅ Complete |
| Section Extraction | ✅ Complete |
| SQLite Integration | ✅ Complete |
| Version Storage | ✅ Complete |
| Version Comparison | ✅ Complete |
| FastAPI APIs | ✅ Complete |
| Initial LLM Connectivity | ✅ Complete |
| Structured Output Validation |  In Progress |
| AI Test Case Generation | In Progress |
| Stale Test Detection | In Progress |

---

# Future Improvements

- Structured JSON validation using Pydantic
- Automatic retry for malformed LLM responses
- Persistent storage of generated test cases
- Automated stale test detection
- Docker containerization
- Comprehensive unit and integration tests

---

# Learning Outcomes

During this project I gained practical experience with:

- Backend API development using FastAPI
- PDF document parsing
- Database design using SQLAlchemy
- Version comparison algorithms
- REST API development
- Modular software architecture
- Initial integration of Large Language Models into backend workflows

---

# Disclaimer

The project is yet to be completed and it was done as internship project.

