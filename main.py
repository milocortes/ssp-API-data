from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from routes.tablas_ssp import ssp_router

import uvicorn

app = FastAPI()

# Register routes
app.include_router(ssp_router, prefix="/ssp")

@app.on_event("startup")

def on_startup():
    conn()

@app.get("/")
async def home():
    return RedirectResponse(url="/docs")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)