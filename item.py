from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from item import Item
class Item:
    def __init__(self, name: str, reagents: List, reagent_amounts: List[float], result_amount: int, crafting_tax: int, energy: str, exp: int):
        self.name = name
        self.reagents = reagents
        self.reagent_amounts = reagent_amounts
        self.result_amount = result_amount
        self.crafting_tax = crafting_tax
        self.energy = energy
        self.exp = exp
        
    def print_all(self):
        print(self.name)
        print(self.reagents)
        print(self.reagent_amounts)
        print(self.result_amount)
        print(self.crafting_tax)
        print(self.energy)
        print(self.exp)
        