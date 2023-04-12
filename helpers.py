import requests


def territory_tree(territories, parent=None):
    hash_tree = {}
    for each in territories:
        if each['parent'] == parent:
            territory_id = each['id']
            hash_tree[each['name']] = territory_tree(territories, territory_id)
    return hash_tree
