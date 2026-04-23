"""
routers/ai.py
/api/* 路由
"""
from fastapi import APIRouter, HTTPException
from models.schemas import GenerateRequest, GenerateResponse, HealthResponse
from services.phrases import generate_replies
from config import settings

router = APIRouter(prefix="/api", tags=["AI"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """服务健康检查 + 配置确认"""
    return HealthResponse(
        status="ok",
        model=settings.LLM_MODEL,
        version=settings.APP_VERSION,
    )


@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    """
    核心接口：输入黑粉内容，返回 AI 生成的优雅反击回复

    - mode=paste：粘贴黑粉原话
    - mode=template：选择攻击类型
    """
    # 参数校验
    if req.mode == "paste" and not req.content:
        raise HTTPException(status_code=422, detail="paste 模式需要提供 content")
    if req.mode == "template" and not req.attack_type:
        raise HTTPException(status_code=422, detail="template 模式需要提供 attack_type")

    try:
        replies = await generate_replies(req)
    except ValueError as e:
        raise HTTPException(status_code=502, detail=f"AI 解析失败：{str(e)}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=503, detail=f"AI 服务异常：{str(e)}")

    if not replies:
        raise HTTPException(status_code=502, detail="AI 未返回有效回复")

    summary = req.content[:30] + "…" if req.content else f"[{req.attack_type}]"
    return GenerateResponse(replies=replies, input_summary=summary)
