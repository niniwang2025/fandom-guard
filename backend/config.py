# ============================================================
#  config.py  ·  唯一需要改动的配置文件
#  把下面三行换成你公司内网 LLM 的真实参数即可
# ============================================================

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ✏️  改这里 ↓↓↓
    LLM_BASE_URL: str = "http://localhost:11434/v1"   # 内网LLM地址（OpenAI兼容）
    LLM_MODEL:    str = "qwen2.5:7b"                  # 模型名称
    LLM_API_KEY:  str = "none"                        # 内网通常不需要，填 none 即可
    LLM_TIMEOUT:  int = 120                            # 请求超时秒数

    APP_TITLE:    str = "追星护卫队"
    APP_VERSION:  str = "1.0.0"

    class Config:
        env_file = ".env"   # 也支持 .env 文件覆盖


settings = Settings()
