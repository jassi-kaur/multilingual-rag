# Multilingual RAG — One Space, Many Languages

A research-oriented multilingual Retrieval-Augmented Generation (RAG) system that enables users to ask questions in one language and retrieve relevant information from documents written in another.

## 1. Project Overview

Most document question-answering systems work best when the user's query and the document content are in the same language.

This project explores cross-lingual information retrieval: retrieving relevant passages from documents even when the question is asked in a different language.

The initial implementation focuses on retrieving relevant English passages using Hindi queries and generating grounded answers in the user's chosen language.

The system will initially support PDF documents.

## 2. Research Objective

To investigate how effectively multilingual embedding models retrieve relevant English document passages when users submit queries in Hindi.

The project will compare retrieval approaches, evaluate their performance and document the experimental findings.

### Primary Research Question

How effectively can multilingual embedding models retrieve semantically relevant English document passages from Hindi queries?

### Research Goals

- Build a functional multilingual RAG application.
- Investigate cross-lingual semantic retrieval.
- Compare multilingual embedding models and retrieval approaches.
- Evaluate retrieval quality independently from answer-generation quality.
- Measure and document experimental results.
- Develop a reproducible research framework.

## 3. Proposed System Workflow

1. User uploads a PDF document.
2. The system extracts text and page information.
3. Extracted text is divided into smaller passages (chunks).
4. An embedding model converts passages into numerical vectors.
5. The vectors are stored for semantic retrieval.
6. The user submits a question in their preferred language.
7. The query is converted into an embedding.
8. The retrieval component finds the most relevant document passages.
9. Retrieved passages are supplied to the language model as context.
10. The language model generates a grounded answer.
11. The application displays the answer with supporting original passages and page references.

## 4. Initial Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.12 |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Embedding framework | Sentence Transformers |
| Initial embedding model | intfloat/multilingual-e5-small |
| Initial similarity search | NumPy |
| Future vector indexing | FAISS CPU |
| LLM runtime | Ollama |
| Initial language model | Llama 3.2 3B |
| PDF processing | PyMuPDF |
| Data validation | Pydantic |
| Testing | pytest |
| Experiments | Jupyter Notebook |
| Data analysis | NumPy, Pandas, Matplotlib |
| Version control | Git and GitHub |

The initial implementation will avoid high-level RAG frameworks so that the core retrieval and generation pipeline can be understood, implemented and evaluated independently.

## 5. Research and Engineering Principles

- Keep retrieval and generation components independent of the web framework.
- Preserve document IDs, chunk IDs and page metadata.
- Keep application documents separate from fixed research evaluation datasets.
- Evaluate retrieval performance separately from generation quality.
- Use consistent conditions when comparing embedding models.
- Record experiment configurations, measurements and limitations.
- Introduce additional technologies only when there is a clear technical or research justification.

## 6. Project Structure

```text
Multilingual-RAG/
│
├── src/
│   └── multilingual_rag/
│       ├── ingestion/
│       ├── retrieval/
│       ├── generation/
│       └── evaluation/
│
├── frontend/
├── tests/
├── experiments/
├── datasets/
│   └── evaluation/
├── documents/
├── configs/
├── docs/
│
├── .gitignore
└── README.md

```

## 7. Development Roadmap

| Phase | Focus |
|---|---|
| Phase 1 | Foundations and Environment |
| Phase 2 | Document Ingestion and Processing |
| Phase 3 | Embeddings and Semantic Retrieval |
| Phase 4 | RAG Generation and Grounded Answers |
| Phase 5 | Web Application Development |
| Phase 6 | Research and Evaluation |
| Phase 7 | Advanced Research and Optimization |
| Phase 8 | Portfolio, Documentation and Research Presentation |

## 8. Current Development Status

**Phase 1 — Foundations and Environment**

- [x] Project directory structure created.
- [x] Python virtual environment created.
- [x] Git installation verified.
- [x] VS Code development extensions verified.
- [x] Initial `.gitignore` configured.
- [ ] README and Git initialization.
- [ ] Dependency compatibility verification.
- [ ] Embedding model execution verification.
- [ ] Local LLM generation verification.

## 9. Research Scope

The initial research experiment will focus on English documents and Hindi queries.

Future experiments may investigate:

- Additional language combinations.
- Different multilingual embedding models.
- Direct cross-lingual retrieval versus translation-based retrieval.
- Chunking strategies.
- Retrieval ranking and similarity methods.
- Retrieval accuracy and latency.
- Grounded answer quality.

These extensions will be introduced progressively and supported by experimental evidence.

## 10. Project Philosophy

**One Space, Many Languages.**

The objective is not simply to build another document chatbot. It is to understand, implement and evaluate how information retrieval and language generation can work across language boundaries.

