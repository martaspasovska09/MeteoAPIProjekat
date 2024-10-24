import os

from flask_sqlalchemy import SQLAlchemy # type: ignore

from open_alchemy import init_yaml # type: ignore

# Construct models
db = SQLAlchemy()
SPEC_DIR = os.path.dirname(__file__)
SPEC_FILE = os.path.join(SPEC_DIR, "meteoapi.yaml")
MODELS_FILENAME = os.path.join(SPEC_DIR, "models.py")
init_yaml(SPEC_FILE, base=db.Model, models_filename=MODELS_FILENAME)
