from fastapi import FastAPI
from routers import kickstart, register, autodiscovery, install

app = FastAPI()

app.include_router(install.router)
app.include_router(autodiscovery.router)
app.include_router(kickstart.router)
app.include_router(register.router)
