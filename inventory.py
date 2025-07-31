import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import smtplib

class InventoryManager:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def check_stock(self):
        print("Current Inventory Levels:")
        print(self.df[["Item", "Stock", "ExpiryDate"]])

    def predict_restock(self):
        print("\nPredicting Restock Requirements...")
        for i, row in self.df.iterrows():
            if row["Stock"] < 20:
                print(f"Restock needed for {row['Item']} (Stock: {row['Stock']})")

    def send_alerts(self):
        for i, row in self.df.iterrows():
            if row["Stock"] < 10:
                print(f"ALERT: {row['Item']} critically low (Stock: {row['Stock']})")
