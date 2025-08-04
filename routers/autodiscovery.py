import dependencies
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from utils import templates

router = APIRouter()

@router.get('/autodiscovery/{mac}/', tags=['autodiscovery'], response_class=HTMLResponse)
async def evaluate_destenation(mac):
  host = dependencies.settings['database'].find_host(mac)
  if host['status'] == 'Success':
    route='kickstart'
  else:
    route='register'
  return templates.render_template('chain.ipxe.j2', scheme=dependencies.settings['server']['scheme'], batbmp_host=dependencies.settings['server']['host'], route=route)
