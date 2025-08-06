from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.core.config import settings

router = APIRouter()

@router.post("/upload/")
async def upload_docs(files: list[UploadFile] = File(...)):
    saved_files = []
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    for file in files:
        filename = file.filename or "unnamed_file"
        filepath = os.path.join(settings.UPLOAD_DIR, filename)
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved_files.append({"filename": filename})

    return {"files": saved_files}
