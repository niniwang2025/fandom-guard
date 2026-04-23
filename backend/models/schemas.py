from pydantic import BaseModel, Field
from typing import Literal, Optional


# ---------- 请求体 ----------
class GenerateRequest(BaseModel):
    mode: Literal["paste", "template"] = Field(
        ..., description="paste=粘贴原话, template=选类型"
    )
    content: Optional[str] = Field(
        None, description="paste模式：黑粉原话"
    )
    attack_type: Optional[str] = Field(
        None, description="template模式：攻击类型"
    )
    idol_name: Optional[str] = Field(
        None, description="偶像名字，增强回复针对性"
    )
    idol_field: Optional[Literal["idol", "actor", "athlete", "other"]] = Field(
        "idol", description="偶像领域"
    )
    style: Literal["sharp", "humor", "logic", "mixed"] = Field(
        "mixed", description="回复风格"
    )


# ---------- 响应体 ----------
class Reply(BaseModel):
    style: str         # 风格标签，如 "犀利"
    text: str          # 回复正文
    emoji: str = ""    # 装饰 emoji


class GenerateResponse(BaseModel):
    replies: list[Reply]
    input_summary: str = ""   # 对输入的简短摘要（调试用）


# ---------- 健康检查 ----------
class HealthResponse(BaseModel):
    status: str
    model: str
    version: str
