import dependencies
from fastapi import APIRouter

router = APIRouter()

@router.get('/register/{mac}/', tags=['register'])
async def register_host(mac):
   dependencies.settings = dependencies.load_settings()
   config = {
     'users': dependencies.settings['users'],
     'mirror': dependencies.settings['mirror'],
     'os': dependencies.settings['os'],
     'host': dependencies.settings['host']
   }
   host = dependencies.settings['database'].add_host(mac, config)
   return host
