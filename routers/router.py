import dependencies
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from jinja2 import Environment, PackageLoader, select_autoescape

router = APIRouter()

@router.get('/router/{mac}/', tags=['router'], response_class=HTMLResponse)
async def evaluate_destenation(mac):
  host = dependencies.settings['database'].find_host(mac)
  if host['status'] == 'Success':
    config = json.loads(host['host']['config'])
    return templates.render_template('kickstart.conf.j2', **config)
  else:
    raise HTTPException(status_code=404, detail=host['status'])
