from flask_migrate import Migrate
from trackstar import create_app, db
from trackstar.models import User

app = create_app("default")
migrate = Migrate(app, db)


@app.cli.command()
def test():
    """Run the unit tests."""

    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)

