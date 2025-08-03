from flask import Flask
from routes.router import route

app = Flask(__name__)
app.register_blueprint(route)

if '__main__' == __name__:
  app.run()
