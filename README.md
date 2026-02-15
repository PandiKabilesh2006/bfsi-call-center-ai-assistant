# BFSI Call Center AI Assistant

A lightweight, compliant, and modular AI assistant designed to handle Banking, Financial Services, and Insurance (BFSI) call center queries using a dataset-first architecture, a local Small Language Model (SLM), and Retrieval-Augmented Generation (RAG).

---

## Objective

This project aims to build a safe, efficient, and compliance-aware AI system that:

- Runs locally using a small language model  
- Prioritizes curated dataset responses  
- Uses retrieval for complex financial queries  
- Enforces strict BFSI safety and compliance guardrails  

The system is designed to minimize hallucination and maximize response reliability.

---

## Architecture Overview

```
User Query
    ↓
Guardrails Layer
    ↓
Dataset Similarity Match (Tier 1)
    ↓ (if strong match)
Return Stored Response
    ↓ (if no strong match)
RAG Retrieval (Tier 3)
    ↓ (if policy-related query)
Grounded Response
    ↓ (otherwise)
Local Small Language Model (Tier 2 Fallback)
    ↓
Final Response
```

---

## Core Components

### 1. Guardrails Layer

Ensures:

- No exposure of sensitive data  
- No identity-based personalization  
- No guessing of financial numbers  
- No generation of fake policies  
- Rejection of out-of-domain queries  

This enforces BFSI compliance requirements.

---

### 2. Dataset Layer (Primary Response Engine)

- 151+ Alpaca-formatted BFSI samples  
- Professional and standardized responses  
- Semantic similarity search using `sentence-transformers`  
- Deterministic response behavior  

If a strong similarity match is found, the stored response is returned directly.

---

### 3. Small Local Language Model (SLM)

- **Model:** TinyLlama-1.1B-Chat  
- Runs locally on CPU  
- Used only when dataset match fails  
- Prompt-conditioned for compliance safety  

---

### 4. RAG Layer (Knowledge Retrieval)

- Structured policy documents stored in `data/knowledge_docs`  
- Semantic retrieval using embeddings  
- Context-grounded generation  

Used for:

- Interest explanations  
- EMI breakdowns  
- Penalty rules  
- Loan approval policies  

---

## Project Structure

```
bfsi-call-center-ai-assistant/
│
├── data/
│   ├── alpaca_dataset.json
│   └── knowledge_docs/
│
├── src/
│   ├── similarity.py
│   ├── guardrails.py
│   ├── slm.py
│   ├── rag.py
│   └── pipeline.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/PandiKabilesh2006/bfsi-call-center-ai-assistant.git
cd bfsi-call-center-ai-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

## Example Query Routing

| Query | Response Source |
|--------|----------------|
| How is EMI calculated? | Dataset |
| Explain loan approval criteria | RAG |
| Explain amortization | SLM |
| What is my account number? | Guardrails |

---

## Safety and Compliance Design

This system enforces:

- Deterministic dataset-first responses  
- Strict guardrail filtering  
- No financial number guessing  
- No exposure of customer identity data  
- Grounded RAG responses for policy queries  

---

## Scalability and Maintainability

- Modular architecture  
- Easily extensible dataset  
- Replaceable SLM model  
- Updatable knowledge base  
- Clear separation of concerns  

### Future Improvements

- Advanced semantic routing  
- Conversation memory support  
- Logging and monitoring integration  

---

## Deliverables Covered

- 150+ Alpaca formatted dataset  
- Local SLM integration  
- Structured RAG knowledge base  
- Working end-to-end Streamlit demo  
- Modular architecture with documentation  

---

## Author

**Pandi Kabilesh**  
AI/ML Enthusiast | Aspiring AI Engineer
