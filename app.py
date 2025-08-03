from flask import Flask
from routes.kickstart import kickstart
from db import connect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

app.register_blueprint(kickstart)
connect.db.init_app(app)

with app.app_context():
  connect.db.create_all()

if '__main__' == __name__:
  app.run()
