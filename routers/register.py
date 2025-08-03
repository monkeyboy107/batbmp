from fastapi import APIRouter
from dependencies import db 

router = APIRouter()

@router.get('/register/{mac}/', tags=['register'])
async def register_host(mac):
   host = db.add_host(mac)
   return host
