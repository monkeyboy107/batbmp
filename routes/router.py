from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

route = Blueprint('simple_page', __name__, template_folder='templates')

@route.route('/register/<mac>')
def show(mac):
  return render_template('kickstart.conf.j2')
