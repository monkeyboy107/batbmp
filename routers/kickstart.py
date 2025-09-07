import dependencies
import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from utils import templates

router = APIRouter()

@router.get('/kickstart/{mac}/', tags=['kickstart'], response_class=HTMLResponse)
async def retrieve_kickstart(mac):
  host = dependencies.settings['database'].find_host(mac)
  if host['status'] == 'Success':
    config = json.loads(host['host']['config'])
    return templates.render_template('kickstart.conf.j2', **config)
  else:
    raise HTTPException(status_code=404, detail=host['status'])
