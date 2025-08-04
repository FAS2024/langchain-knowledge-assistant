# LangChain Knowledge Assistant

A production-ready full-stack application for uploading documents, chatting with them, and retrieving intelligent answers. Built with **LangChain**, **FAISS**, **PostgreSQL**, **FastAPI**, and **React**.

## 🧠 Features

* 📄 Upload and parse multiple file types (PDF, DOCX, TXT, etc.)
* 💬 Chat with documents using LangChain & OpenAI
* 🔍 FAISS vector store for semantic search
* 🗂️ PostgreSQL database for metadata and session history
* 🧠 Chat memory support
* ⚡ FastAPI backend
* 💻 React frontend (Vite + Tailwind)
* 📦 Dockerized for deployment
* 📁 Modular and scalable architecture

---

## 📁 Project Structure

```bash
langchain-knowledge-assistant/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   ├── vite.config.ts
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Technologies

* **LangChain** – for intelligent agent and chain management
* **OpenAI API** – for embeddings & chat completion
* **FAISS** – for fast vector similarity search
* **FastAPI** – high-performance Python backend
* **PostgreSQL** – for storing session and file metadata
* **React + Vite + Tailwind** – for a fast, modern UI
* **Docker** – for containerized deployment

---

## 🔐 Environment Variables (.env)

See `.env.example`:

```env
OPENAI_API_KEY=your-openai-key
API_HOST=
API_PORT=
ENVIRONMENT=
APP_NAME=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
DATABASE_URL=

OPENAI_API_KEY=
OPENAI_API_BASE=
OPENAI_MODEL=

VECTOR_DB_TYPE=
VECTOR_STORE_PATH=

UPLOAD_DIR=

MEMORY_WINDOW_SIZE=

LOG_LEVEL=

```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FAS2024/langchain-knowledge-assistant.git
cd langchain-knowledge-assistant
```

### 2. Create `.env` Files

Copy `.env.example` and update values in `backend/.env`.

```bash
cp backend/.env.example backend/.env
```

### 3. Build and Run with Docker

```bash
docker-compose up --build
```

Backend: `http://localhost:8000`
Frontend: `http://localhost:3000`

---

## 🧪 Running Tests (Coming Soon)

```bash
# backend tests
cd backend
pytest
```

---

## 📦 Deployment

You can deploy using Docker to any cloud platform:

* Render
* Railway
* AWS/GCP/Azure

Set environment variables for production and use secure credentials.

---

## 🧑‍💻 Author

**Fatai Ayinla Sunmonu (FAS)**

* LinkedIn: [https://linkedin.com/in/fatai-sunmonu](https://linkedin.com/in/fatai-sunmonu)
* GitHub: [https://github.com/FAS2024](https://github.com/FAS2024)

---

## 📜 License

This project is licensed under the MIT License.