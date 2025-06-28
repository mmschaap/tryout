"""
A minimal MCP (Model Context Protocol) server using FastAPI.

Run this server with:  python -m mcp_server.server

Available endpoints:
- GET /           : MCP server status message
- GET /status     : Simple status check
- GET /station    : Returns all NS stations from the NS API

Interactive API docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc:      http://localhost:8000/redoc
"""

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from sys import stdout
import uvicorn
import requests
import logging
import sys

# Force unbuffered output for logging and print
sys.stdout.reconfigure(line_buffering=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    force=True  # Ensures logging config is applied even if Uvicorn sets its own
)
logger = logging.getLogger("mcp_server")  # Use a unique logger name

logger.info("Server starting...")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "MCP Server is running!"}

@app.get("/status")
def status():
    logger.info("Status endpoint called")
    return {"status": "ok"}

@app.get("/station")
def get_station():
    API_KEY = "877b721ed49048a0b7214eb8745dd623"
    url = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/stations"
    headers = {"Ocp-Apim-Subscription-Key": API_KEY}
    logger.info("Station endpoint called (all stations)")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logger.error(f"NS API error: {response.status_code} {response.text}")
        return JSONResponse(status_code=response.status_code, content={"error": "Failed to fetch data from NS API"})
    data = response.json()
    logger.debug(f"NS API response: {data}")
    return data

if __name__ == "__main__":
    import sys
    logging.getLogger().setLevel(logging.INFO)
    uvicorn.run("mcp_server.server:app", host="127.0.0.1", port=8000, reload=True, log_level="debug", access_log=True)
