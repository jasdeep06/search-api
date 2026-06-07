module.exports = {
  apps: [
    {
      name: "oneplace-search-api",
      cwd: __dirname,
      script: ".venv/bin/uvicorn",
      interpreter: "none",
      args: [
        "search_app:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8038",
      ],
      env: {
        PYTHONUNBUFFERED: "1",
      },
    },
  ],
};
