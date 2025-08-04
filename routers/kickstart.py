import dependencies
import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from jinja2 import Environment, PackageLoader, select_autoescape
from utils import database, templates

router = APIRouter()

@router.get('/kickstart/{mac}/', tags=['kickstart'], response_class=HTMLResponse)
async def retrieve_kickstart(mac):
  host = dependencies.settings['database'].find_host(mac)
  if host['status'] == 'Success':
    env = Environment(
      loader=templates.loader,
      autoescape=select_autoescape()
    )
    config = json.loads(host['host']['config'])
    return templates.render_template('kickstart.conf.j2', **config)
  else:
    raise HTTPException(status_code=404, detail=host['status'])
