import dependencies
from fastapi import FastAPI
from routers import kickstart, register, autodiscovery

app = FastAPI()

app.include_router(autodiscovery.router)
app.include_router(kickstart.router)
app.include_router(register.router)
