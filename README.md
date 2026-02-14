🏦 BFSI Call Center AI Assistant

A lightweight, compliant, and modular AI assistant designed to handle Banking, Financial Services, and Insurance (BFSI) call center queries using a dataset-first architecture, local Small Language Model (SLM), and Retrieval-Augmented Generation (RAG).

📌 Objective

The goal of this project is to build a safe, efficient, and compliance-aware AI system that:

Runs locally using a small language model

Prioritizes curated dataset responses

Uses retrieval for complex financial queries

Enforces strict BFSI safety and compliance guardrails

This system is designed to minimize hallucination and maximize response reliability.

🏗 Architecture Overview
User Query
    ↓
Guardrails Layer
    ↓
Tier 1: Dataset Similarity Match (Alpaca)
    ↓ (if strong match)
Return Stored Response
    ↓ (if no strong match)
Tier 3: RAG (Policy Retrieval)
    ↓ (if policy-related query)
Grounded Response Generation
    ↓ (otherwise)
Tier 2: Local Small Language Model (Fallback)
    ↓
Final Response

🧠 Core Components
1️⃣ Guardrails Layer (Compliance First)

Ensures:

No exposure of sensitive data

No identity-based personalization

No guessing of financial numbers

No generation of fake policies

Rejection of out-of-domain queries

This enforces BFSI regulatory compliance.

2️⃣ Dataset Layer (Primary Response Engine)

151+ Alpaca-formatted BFSI samples

Professional and standardized responses

Semantic similarity search using sentence-transformers

Deterministic response behavior

If a strong similarity match is found, the stored response is returned directly.

This minimizes hallucination and ensures compliance.

3️⃣ Small Local Language Model (SLM)

Model: TinyLlama-1.1B-Chat

Runs locally on CPU

Used only when dataset match fails

Prompt-conditioned for compliance safety

Note: Due to hardware and time constraints, prompt conditioning was used instead of full LoRA fine-tuning. The architecture supports future fine-tuning if required.

4️⃣ RAG Layer (Knowledge Retrieval)

Structured policy documents stored in data/knowledge_docs

Semantic retrieval using embeddings

Context-grounded generation

Used for:

Interest explanations

EMI breakdowns

Penalty rules

Loan approval policies

This ensures grounded responses for complex financial queries.

📂 Project Structure
bfsi-call-center-ai-assistant/
│
├── data/
│   ├── alpaca_dataset.json
│   ├── knowledge_docs/
│
├── src/
│   ├── similarity.py
│   ├── guardrails.py
│   ├── slm.py
│   ├── rag.py
│   ├── pipeline.py
│
├── app.py
├── requirements.txt
├── README.md

🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/PandiKabilesh2006/bfsi-call-center-ai-assistant.git
cd bfsi-call-center-ai-assistant

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Streamlit App
streamlit run app.py

🧪 Example Query Routing
Query	Response Source
How is EMI calculated?	Dataset
Explain loan approval criteria	RAG
Explain amortization	SLM
What is my account number?	Guardrails
🛡 Safety & Compliance Design

This system enforces:

Deterministic dataset-first responses

Strict guardrail filtering

No financial number guessing

No exposure of customer identity data

Grounded RAG responses for policy queries

Designed to reflect real-world BFSI AI deployment standards.

📊 Scalability & Maintainability

Modular architecture

Easily extensible dataset

Replaceable SLM model

Updatable knowledge base

Clear separation of concerns

Future Improvements:

LoRA fine-tuning on Alpaca dataset

Advanced semantic routing

Conversation memory support

Logging & monitoring integration

🎯 Key Design Decisions
Why Dataset First?

To minimize hallucination and ensure standardized compliance-safe responses.

Why RAG Before Generic SLM?

To ground policy-related answers and reduce risk of misinformation.

Why Local SLM?

To ensure data privacy and offline capability.

📦 Deliverables Covered

✔ 150+ Alpaca formatted dataset
✔ Local SLM integration
✔ Structured RAG knowledge base
✔ Working end-to-end Streamlit demo
✔ Modular architecture with documentation

🧑‍💻 Author

Pandi Kabilesh
AI/ML Enthusiast | Aspiring Machine Learning Engineer