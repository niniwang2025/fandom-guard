"""
main.py  ·  FastAPI 应用入口
同时托管前端静态文件，一个端口全搞定
"""
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.ai import router as ai_router
from config import settings

# ── 应用实例 ─────────────────────────────────────────────────
app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="智能反黑粉助手 · 追星护卫队",
)

# ── CORS（本地开发用，上线可按需收窄） ────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── 注册 API 路由 ─────────────────────────────────────────────
app.include_router(ai_router)

# ── 托管前端静态文件 ──────────────────────────────────────────
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/", include_in_schema=False)
    async def serve_index():
        return FileResponse(str(FRONTEND_DIR / "index.html"))
