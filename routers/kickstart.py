import dependencies
from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse
from jinja2 import Environment, PackageLoader, select_autoescape
from utils import database

router = APIRouter()

@router.get('/kickstart/{mac}/', tags=['kickstart'])
async def retrieve_kickstart(mac, response_class=ORJSONResponse):
  host = dependencies.settings['database'].find_host(mac)
  if host['status'] == 'Success':
    return host['host']['mac']
  else:
    raise HTTPException(status_code=404, detail=host['status'])
