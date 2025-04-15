from fastapi import APIRouter, UploadFile
from app.services.content_analysis import ContentAuditAgent

router = APIRouter()
agent = ContentAuditAgent()

@router.post("/analyze")
async def analyze_content(file: UploadFile):
    result = agent.run({"file": await file.read()})
    return result
