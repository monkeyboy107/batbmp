from jinja2 import Environment, BaseLoader, select_autoescape, TemplateNotFound
from os.path import join, exists, getmtime

class loader(BaseLoader):
  def __init__(self, path):
    self.path = path
  
  def get_source(self, environment, template):
    path = join(self.path, template)
    if not exists(path):
      raise TemplateNotFound(template)
    mtime = getmtime(path)
    with open(path) as stream:
      data = stream.read()
    return data, path, lambda: mtime == getmtime(path)

env = Environment(
  loader=loader('template/templates'),
  autoescape=select_autoescape()
)

def render_template(template, **kwargs):
  template = env.get_template(template)
  return template.render(**kwargs)
