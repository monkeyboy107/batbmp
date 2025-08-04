import dependencies
from fastapi import FastAPI
from routers import kickstart, register, router

app = FastAPI()

app.include_router(router.router)
app.include_router(kickstart.router)
app.include_router(register.router)
