# Smart Inventory Management System

This project is a basic inventory management system designed for FMCG warehouses. It monitors stock levels, predicts when items need restocking, and simulates alerts for critical inventory.

## 🧠 Features

- Real-time stock overview from CSV data
- Expiry date awareness
- Predictive restocking suggestions (based on stock threshold)
- Low-stock alerts

## 📁 Files

- `main.py` — Main script to run the inventory system.
- `inventory.py` — Contains the `InventoryManager` class with logic for inventory processing.
- `inventory_data.csv` — Sample inventory dataset with stock and expiry dates.

## ▶️ How to Run

1. Ensure Python is installed.
2. Install required libraries:  
```bash
pip install pandas scikit-learn
```
3. Run the program:
```bash
python main.py
```

## 📌 Example Output

```
Current Inventory Levels:
     Item  Stock  ExpiryDate
0     Tea     12  2025-09-01
1  Coffee      8  2025-08-25
2   Sugar     35  2025-12-01
3    Salt     18  2025-11-15

Predicting Restock Requirements...
Restock needed for Tea (Stock: 12)
Restock needed for Coffee (Stock: 8)
Restock needed for Salt (Stock: 18)

ALERT: Coffee critically low (Stock: 8)
```

## 📈 Skills Demonstrated

- Python scripting
- Data handling with Pandas
- CSV-based inventory logic
- Simple ML-ready structure (Linear Regression placeholder)
- Real-world application to FMCG and warehouse systems
