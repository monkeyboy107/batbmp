import dependencies
import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from utils import templates

router = APIRouter()

@router.get('/install/{mac}/', tags=['install'], response_class=HTMLResponse)
async def retrieve_kickstart(mac):
  host = dependencies.settings['database'].find_host(mac)
  if host['status'] == 'Success':
    config = dependencies.load_settings()
    host_config = json.loads(host['host']['config'])
    config.update(host_config)
    return templates.render_template('boot.conf.j2', **config)
  else:
    raise HTTPException(status_code=404, detail=host['status'])
