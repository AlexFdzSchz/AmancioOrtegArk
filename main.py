import json
from item import Item

with open("items.json", "r", encoding="utf-8") as items_json:
    content = items_json.read()

loadedData = json.loads(content)
items = [] 

for data in loadedData:
    name = data["name"]
    reagents = data["reagents"]
    reagent_amounts = data["reagent_amounts"]
    result_amount = data["result_amount"]
    crafting_tax = data["crafting_tax"]
    exp = data["exp"]
    energy = data["energy"]

    
item = Item(name, reagents, reagent_amounts, result_amount, crafting_tax, energy, exp)
items.append(item)

for item in items:
    item.print_all()
