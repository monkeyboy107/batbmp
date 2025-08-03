from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from jinja2 import Environment, PackageLoader, select_autoescape

router = APIRouter()

@router.get('/kickstart/{mac}/', tags=['kickstart'])
async def retrieve_kickstart(mac, response_class=ORJSONResponse):
  env = Environment(
    loader=PackageLoader('')
  )
  return 'Hello world'
