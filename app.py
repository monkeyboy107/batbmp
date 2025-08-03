from fastapi import FastAPI
from routers import kickstart

app = FastAPI()

app.include_router(kickstart.router)
