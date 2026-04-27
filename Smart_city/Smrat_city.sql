create database SmartCityEner;

use SmartCityEnergy ;

-- ============================================
-- SMART CITY ENERGY PROJECT
-- ============================================

-- CREATE TABLE
CREATE TABLE SmartCityEnergy (
    MeterID VARCHAR(50),
    Zone VARCHAR(50),
    ConsumerType VARCHAR(50),
    Date DATE,
    EnergyConsumed_kWh FLOAT,
    PeakUsage_kWh FLOAT,
    OutageMinutes INT,
    MeterStatus VARCHAR(20),
    TariffRate FLOAT
);

-- ============================================
-- QUERIES
-- ============================================

-- 1. Total & Average Consumption by Zone
SELECT 
    Zone,
    SUM(EnergyConsumed_kWh) AS Total_Consumption,
    AVG(EnergyConsumed_kWh) AS Avg_Consumption
FROM SmartCityEnergy
GROUP BY Zone;

-- 2. Top 5 Consumers by Type
SELECT *
FROM (
    SELECT 
        ConsumerType,
        MeterID,
        SUM(EnergyConsumed_kWh) AS Total_Usage,
        RANK() OVER (PARTITION BY ConsumerType ORDER BY SUM(EnergyConsumed_kWh) DESC) AS rnk
    FROM SmartCityEnergy
    GROUP BY ConsumerType, MeterID
) t
WHERE rnk <= 5;

-- 3. Monthly Trend
SELECT 
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(EnergyConsumed_kWh) AS Monthly_Consumption
FROM SmartCityEnergy
GROUP BY Month
ORDER BY Month;

-- 4. Average Cost per Zone
SELECT 
    Zone,
    AVG(EnergyConsumed_kWh * TariffRate) AS Avg_Cost
FROM SmartCityEnergy
GROUP BY Zone;

-- 5. Faulty Meters / Outages
SELECT 
    MeterID,
    COUNT(*) AS Issue_Count,
    SUM(OutageMinutes) AS Total_Outage
FROM SmartCityEnergy
WHERE MeterStatus = 'Faulty' OR OutageMinutes > 0
GROUP BY MeterID
ORDER BY Issue_Count DESC;

-- 6. Least Efficient Zones
SELECT 
    Zone,
    SUM(EnergyConsumed_kWh) AS Total_Usage,
    SUM(OutageMinutes) AS Total_Outage
FROM SmartCityEnergy
GROUP BY Zone
ORDER BY Total_Usage DESC, Total_Outage DESC;

-- 7. Weekday vs Weekend
SELECT 
    CASE 
        WHEN DAYOFWEEK(Date) IN (1,7) THEN 'Weekend'
        ELSE 'Weekday'
    END AS Day_Type,
    AVG(PeakUsage_kWh) AS Avg_Peak_Usage
FROM SmartCityEnergy
GROUP BY Day_Type;