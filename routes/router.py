from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import yaml

route = Blueprint('simple_page', __name__, template_folder='templates')

@route.route('/register/<mac>')
def show(mac):
  with open('config.yaml') as stream:
    config = yaml.safe_load(stream)
  return render_template('kickstart.conf.j2', **config)
