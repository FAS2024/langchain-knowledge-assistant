from fastapi import APIRouter, Query, HTTPException
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from app.core.config import settings
import os

router = APIRouter()

# === Check if vector store file exists ===
if not os.path.exists(settings.VECTOR_STORE_PATH):
    raise RuntimeError(f"FAISS index not found at: {settings.VECTOR_STORE_PATH}")

# === Setup Embeddings ===
embedding = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

# === Load FAISS Vector Store ===
db = FAISS.load_local(settings.VECTOR_STORE_PATH, embeddings=embedding)

# === Setup OpenAI Chat LLM ===
llm = ChatOpenAI(
    model_name=settings.OPENAI_MODEL,
    openai_api_key=settings.OPENAI_API_KEY,
    temperature=0  # optional: for predictable answers
)

# === Build the QA Chain ===
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True  # optional: remove if not needed
)

# === In-Memory Chat History ===
memory = []

# === API Route ===
@router.get("/chat/")
async def chat(question: str = Query(..., min_length=1)):
    try:
        response = qa({
            "question": question,
            "chat_history": memory
        })

        # Extract answer and store in memory
        answer = response.get("answer")
        if answer:
            memory.append((question, answer))
            return {"question": question, "answer": answer}
        else:
            raise HTTPException(status_code=500, detail="No answer returned from chain.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LangChain Error: {str(e)}")
