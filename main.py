import json
from item.py import Item
with open("items.json", "r", encoding="utf-8") as items_json:
    content = items_json.read()

loadedData = json.loads(content)
items = [] 

for data in loadedData:
    name = data["name"]
    reagents = data["reagents"]
    reagent_amounts = data["reagent_amounts"]
    result_amount = data["result_amount"]
    exp = data["exp"]
    energy = data["energy"]
    img = data["img"]

    
    item = Item(name, ignore, answer)
    items.append(item)