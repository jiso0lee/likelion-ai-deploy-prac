import logging
from fastapi import FastAPI, Request
from routers import ocr_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="가계부 OCR AI 서버",
    description="PaddleOCR을 이용한 영수증 텍스트 추출 API",
    version="1.0.0"
)

# 라우터 등록
app.include_router(ocr_router.router, prefix="/api/v2", tags=["Analysis"])

@app.get("/")
def health_check(request: Request):
    logger.info(f"Health check called from {request.client.host}")
    return {"status": "ok", "message": "OCR Server is running on CPU"}