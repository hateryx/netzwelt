import requests
import json


def tree():
    url = 'https://netzwelt-devtest.azurewebsites.net/Territories/All'
    response = requests.get(url)
    data = response.json()
    territories_list = data['data']
    tree = territory_tree(territories_list)
    beau_tree = json.dumps(tree, indent=4, sort_keys=True)
    return tree


def territory_tree(territories, parent=None, level=0):
    hash_tree = {}
    for each in territories:
        if each['parent'] == parent:
            territory_id = each['id']
            name = each['name']
            hash_tree[name] = territory_tree(
                territories, territory_id, level=level+1)
    return hash_tree


# def territory_tree(territories, parent=None, isParent="Yes"):
#     hash_tree = {}
#     for each in territories:
#         if each['parent'] == parent:
#             territory_id = each['id']
#             name = each['name']
#             hash_tree[(name, level)] = territory_tree(
#                 territories, territory_id, level=level+1)
#     return hash_tree


print(tree())
