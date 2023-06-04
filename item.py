from typing import List

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
        print(f"name: {self.name}")
        print(f"reagents: {self.reagents}")
        print(f"reagents amount: {self.reagent_amounts}")
        print(f"result amomunt: {self.result_amount}")
        print(f"crafting tax: {self.crafting_tax}")
        print(f"energy: {self.energy}")
        print(f"exp: {self.exp}")
        