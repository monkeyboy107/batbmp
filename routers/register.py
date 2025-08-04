import dependencies
import utils
from fastapi import APIRouter

router = APIRouter()

@router.get('/register/{mac}/', tags=['register'])
async def register_host(mac):
   dependencies.settings = dependencies.load_settings()
   config = {
     'users': dependencies['users'],
     'mirror': dependencies['mirror'],
     'os': dependencies['os'],
     'host': dependencies['name']
   }
   host = dependencies.settings['database'].add_host(mac, config)
   return host
