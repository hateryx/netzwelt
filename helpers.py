from flask import session, redirect
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def territory_tree(territories, parent=None, level=0):
    hash_tree = {}
    for each in territories:
        if each['parent'] == parent:
            territory_id = each['id']
            name = each['name']
            hash_tree[(name, level)] = territory_tree(
                territories, territory_id, level=level+1)
    return hash_tree
