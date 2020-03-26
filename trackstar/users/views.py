from . import users


@users.route("/")
def foo():
    return {"status": "users.foo"}

