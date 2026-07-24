# OnePlace Search API

A small FastAPI service that exposes Tavily-backed web search to OnePlace.

## API

- `POST /search` accepts a search request and returns normalized results.
- Swagger documentation is available at `/docs`.

## Local setup

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
pm2 start ecosystem.config.js
```

The production process binds to `127.0.0.1:8038`. Provide the required search
provider credentials through the process environment; never place secrets in
this README.
