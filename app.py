import dependencies
from fastapi import FastAPI
from routers import kickstart, register

app = FastAPI()

app.include_router(kickstart.router)
app.include_router(register.router)
