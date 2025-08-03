from db import connect
from flask import Flask
from routes.kickstart import kickstart

app = Flask(__name__)
app.register_blueprint(kickstart)

print(connect.engine)

if '__main__' == __name__:
  app.run()
