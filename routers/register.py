import dependencies
from fastapi import APIRouter

router = APIRouter()

@router.get('/register/{mac}/', tags=['register'])
async def register_host(mac):
   dependencies.settings = dependencies.load_settings()
   host = dependencies.settings['database'].add_host(mac)
   return host
