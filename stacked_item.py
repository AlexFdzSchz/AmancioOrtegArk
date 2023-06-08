from typing import List

class Stacked_item:
    def __init__(self, name: str, auction_stack: int):
        self.name = name
        self.auction_stack = auction_stack
        
    def print_all(self):
        print(f"name: {self.name}")
        print(f"auction_stack: {self.auction_stack}")