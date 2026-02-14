# 🏦 BFSI Call Center AI Assistant

A lightweight, compliant, and modular AI assistant designed to handle Banking, Financial Services, and Insurance (BFSI) call center queries using a dataset-first architecture, local Small Language Model (SLM), and Retrieval-Augmented Generation (RAG).

## 📌 Objective
The goal of this project is to build a safe, efficient, and compliance-aware AI system that:
* Runs locally using a small language model.
* Prioritizes curated dataset responses.
* Uses retrieval for complex financial queries.
* Enforces strict BFSI safety and compliance guardrails.

*This system is designed to minimize hallucination and maximize response reliability.*

## 🏗 Architecture Overview

```text
User Query
    ↓
Guardrails Layer
    ↓
Tier 1: Dataset Similarity Match (Alpaca)
    ↓ (if strong match) ➔ Return Stored Response
    ↓ (if no strong match)
Tier 3: RAG (Policy Retrieval)
    ↓ (if policy-related query) ➔ Grounded Response Generation
    ↓ (otherwise)
Tier 2: Local Small Language Model (Fallback)
    ↓
Final Response

🧠 Core Components
1️⃣ Guardrails Layer (Compliance First)
Ensures BFSI regulatory compliance by enforcing:

No exposure of sensitive data.

No identity-based personalization.

No guessing of financial numbers.

No generation of fake policies.

Rejection of out-of-domain queries.

2️⃣ Dataset Layer (Primary Response Engine)
Dataset: 151+ Alpaca-formatted BFSI samples.

Quality: Professional and standardized responses.

Search: Semantic similarity search using sentence-transformers.

Behavior: Deterministic.

Note: If a strong similarity match is found, the stored response is returned directly. This minimizes hallucination and ensures compliance.

3️⃣ Small Local Language Model (SLM)
Model: TinyLlama-1.1B-Chat

Execution: Runs locally on CPU.

Usage: Used only when a dataset match fails.

Safety: Prompt-conditioned for compliance safety.

Note: Due to hardware and time constraints, prompt conditioning was used instead of full LoRA fine-tuning. The architecture supports future fine-tuning if required.

4️⃣ RAG Layer (Knowledge Retrieval)
Storage: Structured policy documents stored in data/knowledge_docs.

Mechanism: Semantic retrieval using embeddings for context-grounded generation.

Used For: Interest explanations, EMI breakdowns, penalty rules, and loan approval policies.

Benefit: Ensures grounded responses for complex financial queries.

📂 Project Structure
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

🚀 How to Run Locally1️⃣ Clone RepositoryBashgit clone [https://github.com/PandiKabilesh2006/bfsi-call-center-ai-assistant.git](https://github.com/PandiKabilesh2006/bfsi-call-center-ai-assistant.git)
cd bfsi-call-center-ai-assistant
2️⃣ Create Virtual EnvironmentBashpython -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate # Mac/Linux
3️⃣ Install DependenciesBashpip install -r requirements.txt
4️⃣ Run Streamlit AppBashstreamlit run app.py
🧪 Example Query RoutingQueryResponse SourceHow is EMI calculated?DatasetExplain loan approval criteriaRAGExplain amortizationSLMWhat is my account number?Guardrails🛡 Safety & Compliance DesignDesigned to reflect real-world BFSI AI deployment standards, this system enforces:Deterministic dataset-first responses.Strict guardrail filtering.No financial number guessing.No exposure of customer identity data.Grounded RAG responses for policy queries.📊 Scalability & MaintainabilityModular architectureEasily extensible datasetReplaceable SLM modelUpdatable knowledge baseClear separation of concernsFuture Improvements:LoRA fine-tuning on the Alpaca dataset.Advanced semantic routing.Conversation memory support.Logging & monitoring integration.🎯 Key Design DecisionsWhy Dataset First? To minimize hallucination and ensure standardized, compliance-safe responses.Why RAG Before Generic SLM? To ground policy-related answers and reduce the risk of misinformation.Why Local SLM? To ensure data privacy and offline capability.📦 Deliverables Covered[x] 150+ Alpaca formatted dataset[x] Local SLM integration[x] Structured RAG knowledge base[x] Working end-to-end Streamlit demo[x] Modular architecture with documentation🧑‍💻 Author Pandi Kabilesh AI/ML Enthusiast | Aspiring Machine Learning Engineer