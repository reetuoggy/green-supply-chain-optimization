-- 1. Create Tables
CREATE TABLE fuel_master (
    Transport_Mode VARCHAR(20) PRIMARY KEY,
    Cost_Per_Km_Ton DECIMAL(10,2),
    CO2_Kg_Per_Km_Ton DECIMAL(10,3),
    Avg_Transit_Days INT
);

CREATE TABLE suppliers (
    Supplier_ID VARCHAR(20) PRIMARY KEY,
    Location VARCHAR(50),
    Eco_Rating INT,
    Unit_Cost DECIMAL(10,2)
);

CREATE TABLE shipments (
    Shipment_ID VARCHAR(20) PRIMARY KEY,
    Supplier_ID VARCHAR(20),
    Transport_Mode VARCHAR(20),
    Distance_KM INT,
    Weight_Tons DECIMAL(10,2),
    Order_Qty INT,
    Urgency VARCHAR(20)
);

-- 2. Create Analytical View
CREATE VIEW v_supply_chain_analytics AS
SELECT 
    s.Shipment_ID,
    s.Supplier_ID,
    sup.Location,
    sup.Eco_Rating,
    s.Transport_Mode,
    s.Urgency,
    (s.Order_Qty * sup.Unit_Cost) AS Material_Spend,
    (s.Distance_KM * s.Weight_Tons * f.Cost_Per_Km_Ton) AS Freight_Spend,
    (s.Distance_KM * s.Weight_Tons * f.CO2_Kg_Per_Km_Ton) / 1000 AS CO2_Emissions_Tons
FROM shipments s
JOIN suppliers sup ON s.Supplier_ID = sup.Supplier_ID
JOIN fuel_master f ON s.Transport_Mode = f.Transport_Mode;