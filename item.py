from typing import List
from item.py import Item

class Item:
    def __init__(self,reagents: List[Item], reagent_amounts: List[float], result_amount: int, energy: str, img: str):
        self.reagents = reagents
        self.reagent_amounts = reagent_amounts
        self.result_amount = result_amount
        self.energy = energy
        self.img = img
        
    def print_all():
        print(self.reagents)
        print(self.reagent_amounts)
        print(self.result_amount)
        print(self.energy)
        print(self.img)
        