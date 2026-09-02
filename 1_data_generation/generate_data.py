import pandas as pd
import numpy as np
import random

np.random.seed(42)

# 1. Fuel & Emissions Master
fuel_data = {
    'Transport_Mode': ['Air', 'Road', 'Rail', 'Ocean'],
    'Cost_Per_Km_Ton': [2.50, 0.45, 0.15, 0.08],
    'CO2_Kg_Per_Km_Ton': [1.65, 0.36, 0.09, 0.045],
    'Avg_Transit_Days': [2, 5, 10, 25]
}
df_fuel = pd.DataFrame(fuel_data)

# 2. Supplier Dimension
cities = ['Shanghai', 'Hamburg', 'Houston', 'Mumbai', 'Vietnam']
suppliers = []
for i in range(1, 51):
    eco_rating = random.randint(1, 5)
    # Higher eco rating slightly increases base material cost
    base_cost = round(random.uniform(10, 50) + (eco_rating * 1.5), 2)
    suppliers.append({
        'Supplier_ID': f'SUP_{i:03}',
        'Location': random.choice(cities),
        'Eco_Rating': eco_rating,
        'Unit_Cost': base_cost
    })
df_suppliers = pd.DataFrame(suppliers)

# 3. Shipment Fact Table
shipments = []
for i in range(1, 10001):
    mode = np.random.choice(['Air', 'Road', 'Rail', 'Ocean'], p=[0.15, 0.40, 0.25, 0.20])
    distance = random.randint(500, 8000) if mode in ['Air', 'Ocean'] else random.randint(100, 2000)
    shipments.append({
        'Shipment_ID': f'SHP_{i:05}',
        'Supplier_ID': random.choice(suppliers)['Supplier_ID'],
        'Transport_Mode': mode,
        'Distance_KM': distance,
        'Weight_Tons': round(random.uniform(1.0, 20.0), 2),
        'Order_Qty': random.randint(100, 1000),
        'Urgency': random.choice(['Critical', 'Standard', 'Low'])
    })
df_shipments = pd.DataFrame(shipments)

# Export
df_fuel.to_csv('fuel_master.csv', index=False)
df_suppliers.to_csv('suppliers.csv', index=False)
df_shipments.to_csv('shipments.csv', index=False)
print("Data generated successfully.")