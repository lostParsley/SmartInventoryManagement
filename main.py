import pandas as pd
from inventory import InventoryManager

def main():
    inventory = InventoryManager("inventory_data.csv")
    inventory.check_stock()
    inventory.predict_restock()
    inventory.send_alerts()

if __name__ == "__main__":
    main()
