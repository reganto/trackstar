from flask_migrate import Migrate
from trackstar import create_app, db
from trackstar.models import User

app = create_app("default")
migrate = Migrate(app, db)

