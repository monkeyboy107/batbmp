from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import yaml

kickstart = Blueprint('kickstart', __name__, template_folder='templates')

@kickstart.route('/kickstart/<mac>')
def show(mac):
  with open('config.yaml') as stream:
    config = yaml.safe_load(stream)
  return render_template('kickstart.conf.j2', **config)
