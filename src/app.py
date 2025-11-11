import connexion # type: ignore
from flask import redirect # type: ignore
import database

app = connexion.FlaskApp(__name__, specification_dir=".")

app.app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://meteoapi:meteoapi123@db/meteoapi"
database.db.init_app(app.app)
with app.app.app_context():
    database.db.create_all()

app.add_api(
    "meteoapi.yaml",
    arguments={"title": "MeteoAPI"},
    strict_validation=True,
    swagger_ui=True,
)

@app.app.route("/")
def home():
    return redirect("/api/ui/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
