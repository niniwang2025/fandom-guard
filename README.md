# 追星护卫队 🛡️
> 智能反黑粉助手 · Full-Stack AI Web App

## 技术栈
| 层 | 技术 | 说明 |
|---|---|---|
| 前端 | HTML5 + CSS3 + Vanilla JS | 手机端H5，零依赖 |
| 后端 | Python 3.10+ · FastAPI | REST API + 静态文件托管 |
| AI | OpenAI 兼容接口（公司内网LLM） | 无需 API Key |
| 部署 | 单命令启动 | `uvicorn main:app` |

## 项目结构
```
fandom-guard/
├── backend/
│   ├── main.py          # FastAPI 主入口
│   ├── routers/
│   │   └── ai.py        # /api/generate 路由
│   ├── services/
│   │   └── llm.py       # LLM 调用封装
│   ├── models/
│   │   └── schemas.py   # Pydantic 数据模型
│   └── config.py        # 配置（内网URL等）
├── frontend/
│   ├── index.html       # 主页面
│   ├── style.css        # 样式
│   └── app.js           # 前端逻辑
├── requirements.txt
└── README.md
```

## 快速启动

### 1. 安装依赖
```bash
cd backend
pip install -r ../requirements.txt
```

### 2. 配置内网 LLM 地址（改这一处即可）
编辑 `backend/config.py`：
```python
LLM_BASE_URL = "http://your-company-llm-host/v1"  # 改成内网地址
LLM_MODEL    = "your-model-name"                   # 改成对应模型
LLM_API_KEY  = "none"                              # 内网不需要可填 none
```

### 3. 启动
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. 访问
手机和电脑同一内网时，打开：
```
http://localhost:8000
```

## API 文档
启动后访问 `http://localhost:8000/docs` 查看 Swagger 文档。

### POST /api/generate
```json
// Request
{
  "mode": "paste",              // "paste" | "template"
  "content": "黑粉原话内容",    // paste模式填原话
  "attack_type": null,          // template模式填攻击类型
  "idol_name": "XXX",          // 可选，偶像名字
  "idol_field": "idol",        // 可选：idol/actor/athlete
  "style": "mixed"              // sharp/humor/logic/mixed
}

// Response
{
  "replies": [
    { "style": "犀利", "text": "..." },
    { "style": "幽默", "text": "..." },
    { "style": "有理", "text": "..." }
  ]
}
```

## 简历亮点写法
- 独立设计并实现前后端分离 AI Web 应用，前端 H5 + 后端 FastAPI
- 对接公司内网 LLM 平台（OpenAI 兼容协议），封装 Prompt Engineering 模块
- 实现流式响应、错误降级、本地缓存等生产级特性
