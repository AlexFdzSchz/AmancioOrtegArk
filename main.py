import json, os
from item import Item
from stacked_item import Stacked_item
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QFrame, QSpinBox, QLabel, QSlider
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    # item List
    items = [] 
    stacked_items = [] 
    selected_item = None
    discount = 0
    time_reduction = 0

    def __init__(self):
        super().__init__()
        loadUi('interface/main_window.ui', self)

        #Load all items
        self.load_Jsons()

        # Load the list
        listWidget = self.findChild(QListWidget, "listWidget")
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        cont = 1
        for item in self.items:
            
            listWidget.addItem(item.name.title())
            cont += 1
        #Load the sliders
        cost_reduction_slider = self.findChild(QSlider, "cost_reduction_slider")
        time_reduction_slider = self.findChild(QSlider, "time_reduction_slider")
        cost_reduction_slider.valueChanged.connect(self.discount_slider_value_changed)
        time_reduction_slider.valueChanged.connect(self.time_reduction_slider_value_changed)
        
    
    def choose_Item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.selected_item = item
                self.load_Item(self.selected_item)
    
    def on_item_clicked(self, listItem):
        self.choose_Item(listItem.text())
        self.deselect_Items(self)
        print(f"click on {listItem.text()}")

    def discount_slider_value_changed(self, value):
        self.discount = value
        label = self.findChild(QLabel, "cost_reduction_result")
        label.setText(f"{value}%")
        print("Discount: ", self.discount)
    
    def time_reduction_slider_value_changed(self, value):
        self.time_reduction = value
        label = self.findChild(QLabel, "time_reduction_result")
        label.setText(f"{value}%")
        print("Time reduction: ", self.time_reduction)
    
    def load_Item(self, item):
        frame = self.findChild(QFrame, "frame")
        cont = 1
        # Shows all related widgets
        self.hide_Widgets()
        for reagent in item.reagents:
            spinner = self.findChild(QSpinBox, f"spinBox_{cont}")
            spinner.setVisible(True)

            label_reagent_amount = self.findChild(QLabel, f"label_reagent_amount_{cont}")
            label_reagent_amount.setVisible(True)
            label_reagent_amount.setText(f"x{item.reagent_amounts[cont-1]}")

            img = self.findChild(QLabel, f"img_{cont}")
            img.setVisible(True)

            if os.path.isfile(f"img/{reagent.lower()}.webp"):
                img.setPixmap(QPixmap(f"img/{reagent.lower()}.webp"))
            else:
                img.setPixmap(QPixmap("img/unknow.webp"))
            print(f"added img to reagent {cont}")
                
            cont += 1
        # Load the crafted item widgets
        img_crafted = self.findChild(QLabel, f"img_crafted")
        img_crafted.setPixmap(QPixmap(f"img/{item.name.lower()}.webp"))
        label_reagent_amount_crafted = self.findChild(QLabel, f"label_reagent_amount_crafted")
        label_reagent_amount_crafted.setVisible(True)
        label_reagent_amount_crafted.setText(f"x{item.result_amount}")
        spinner = self.findChild(QSpinBox, f"spinBox_crafted")
        spinner.setVisible(True)

    def calculate():
        return
               
        
            
    def hide_Widgets(self):
        # Hide all spinbox
        spin_boxes = self.frame.findChildren(QSpinBox)
        for spin_box in spin_boxes:
            spin_box.setVisible(False)

        # Hide all labels
        labels = self.frame.findChildren(QLabel)
        for label in labels:
            if label.objectName().startswith("img") or label.objectName().startswith("label_reagent"):
                label.setPixmap(QPixmap("img/empty.png"))

    def deselect_Items(self, item):
        # Iterar sobre todos los elementos de la lista
        for index in range(self.listWidget.count()):
            list_item = self.listWidget.item(index)
            if list_item.text().lower() != self.selected_item.name.lower():
                # Deseleccionar los elementos distintos al actual
                list_item.setSelected(False)
        
    def load_Jsons(self):
       with open("items.json", "r", encoding="utf-8") as items_json:
        content = items_json.read()

        loadedData = json.loads(content)
        

        for data in loadedData:
            name = data["name"]
            reagents = data["reagents"]
            reagent_amounts = data["reagent_amounts"]
            result_amount = data["result_amount"]
            crafting_tax = data["crafting_tax"]
            exp = data["exp"]
            energy = data["energy"]

            item = Item(name, reagents, reagent_amounts, result_amount, crafting_tax, energy, exp)
            self.items.append(item)

            
        
        # log items
        print("-" * 40)
        for item in self.items:
            item.print_all()
            print("-" * 40)
        
        with open("stacked_items.json", "r", encoding="utf-8") as items_json:
            content = items_json.read()

        loadedData = json.loads(content)
        

        for data in loadedData:
            name = data["name"]
            auction_stack = data["auction_stack"]

            item = Stacked_item(name, auction_stack)
            self.stacked_items.append(item)

        # log items
        print("-" * 40)
        for item in self.stacked_items:
            item.print_all()
            print("-" * 40)

        



        
        




if __name__ == '__main__':
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
