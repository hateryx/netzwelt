import requests
from flask import session, redirect
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def territory_tree(territories, parent=None):
    hash_tree = {}
    for each in territories:
        if each['parent'] == parent:
            territory_id = each['id']
            hash_tree[each['name']] = territory_tree(territories, territory_id)
    return hash_tree
