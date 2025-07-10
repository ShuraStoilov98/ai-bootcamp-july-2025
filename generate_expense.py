import pandas as pd
import random
from datetime import datetime, timedelta

# Sample categories and notes
categories = ["Food", "Travel", "Utilities", "Shopping", "Health", "Entertainment"]
notes = [
    "Groceries", "Uber", "Electric bill", "Online shopping",
    "Pharmacy", "Cinema", "Coffee", "Gym", "Restaurant", "Train ticket"
]

# Generate 100 random expense records
data = []
for _ in range(100):
    date = datetime.now() - timedelta(days=random.randint(0, 90))
    amount = round(random.uniform(5, 250), 2)
    category = random.choice(categories)
    note = random.choice(notes)
    data.append([date.strftime("%Y-%m-%d"), amount, category, note])

# Create DataFrame and save
df = pd.DataFrame(data, columns=["Date", "Amount", "Category", "Notes"])
df.to_csv("expenses.csv", index=False)

print("✅ 'expenses.csv' generated successfully.")
