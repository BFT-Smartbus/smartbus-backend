import config
from flask import Flask
from config import db
from handler.rider_login import rider_login
from handler.driver_login import driver_login


app = Flask(__name__)
# make app available to fll files within entire folder
app.config.from_object(config)
db.init_app(app)

# refactoring
app.register_blueprint(rider_login)
app.register_blueprint(driver_login)

with app.app_context():
    db.create_all()


if __name__ == "__main__":

  app.run(debug=True)
