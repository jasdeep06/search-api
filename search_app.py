from typing import Optional

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 🔒 Hardcode your API key and Tavily settings here
TAVILY_API_KEY = "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"  # <-- replace this

# Hardcoded Tavily options
SEARCH_DEPTH = "basic"
INCLUDE_ANSWER = True
INCLUDE_IMAGES = False


class SearchRequest(BaseModel):
    query: str
    max_results: int = 5


app = FastAPI(title="Simple Tavily Web Search API")


@app.post("/search")
async def search(body: SearchRequest):
    if not TAVILY_API_KEY or TAVILY_API_KEY == "YOUR_TAVILY_API_KEY":
        raise HTTPException(status_code=500, detail="TAVILY_API_KEY not set in code.")

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": body.query,
        "max_results": body.max_results,
        "search_depth": SEARCH_DEPTH,
        "include_answer": INCLUDE_ANSWER,
        "include_images": INCLUDE_IMAGES,
    }

    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post("https://api.tavily.com/search", json=payload)

    if resp.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail={
                "message": "Tavily error",
                "status_code": resp.status_code,
                "body": resp.text,
            },
        )

    return resp.json()
