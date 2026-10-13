-- ============================================================
--  E-Commerce Sales SQL Analysis  |  Akash Kumar
--  Database: SQLite / MySQL compatible
-- ============================================================

-- ── TABLE STRUCTURE ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS ecommerce_sales (
    Order_ID      VARCHAR(20),
    Date          DATE,
    Month         VARCHAR(15),
    Quarter       VARCHAR(5),
    Customer_ID   VARCHAR(20),
    Region        VARCHAR(20),
    City          VARCHAR(30),
    Category      VARCHAR(30),
    Product       VARCHAR(50),
    Quantity      INT,
    Unit_Price    DECIMAL(10,2),
    Discount_Pct  INT,
    Revenue       DECIMAL(10,2),
    Payment_Mode  VARCHAR(30),
    Rating        DECIMAL(3,1)
);

-- ── Q1: Total Revenue & Orders ──────────────────────────────
SELECT
    COUNT(*)                    AS Total_Orders,
    ROUND(SUM(Revenue), 0)      AS Total_Revenue,
    ROUND(AVG(Revenue), 0)      AS Avg_Order_Value,
    ROUND(MAX(Revenue), 0)      AS Max_Order_Value
FROM ecommerce_sales;

-- ── Q2: Revenue by Category (Ranked) ───────────────────────
SELECT
    Category,
    COUNT(*)                        AS Total_Orders,
    ROUND(SUM(Revenue), 0)          AS Total_Revenue,
    ROUND(AVG(Revenue), 0)          AS Avg_Revenue,
    ROUND(SUM(Revenue) * 100.0 /
        (SELECT SUM(Revenue) FROM ecommerce_sales), 2) AS Revenue_Pct
FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- ── Q3: Monthly Revenue Trend ───────────────────────────────
SELECT
    Month,
    COUNT(*)                   AS Orders,
    ROUND(SUM(Revenue), 0)     AS Monthly_Revenue,
    ROUND(AVG(Revenue), 0)     AS Avg_Order_Value
FROM ecommerce_sales
GROUP BY Month
ORDER BY MIN(Date);

-- ── Q4: Region-wise Performance ─────────────────────────────
SELECT
    Region,
    COUNT(DISTINCT Customer_ID)   AS Unique_Customers,
    COUNT(*)                       AS Total_Orders,
    ROUND(SUM(Revenue), 0)         AS Total_Revenue,
    ROUND(AVG(Rating), 2)          AS Avg_Rating
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- ── Q5: Top 10 Products by Revenue ──────────────────────────
SELECT
    Product,
    Category,
    COUNT(*)                   AS Orders,
    SUM(Quantity)              AS Units_Sold,
    ROUND(SUM(Revenue), 0)     AS Total_Revenue,
    ROUND(AVG(Rating), 2)      AS Avg_Rating
FROM ecommerce_sales
GROUP BY Product, Category
ORDER BY Total_Revenue DESC
LIMIT 10;

-- ── Q6: Payment Mode Popularity ─────────────────────────────
SELECT
    Payment_Mode,
    COUNT(*)                        AS Orders,
    ROUND(SUM(Revenue), 0)          AS Revenue,
    ROUND(COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM ecommerce_sales), 2) AS Order_Pct
FROM ecommerce_sales
GROUP BY Payment_Mode
ORDER BY Orders DESC;

-- ── Q7: Discount Impact on Revenue ──────────────────────────
SELECT
    Discount_Pct,
    COUNT(*)                   AS Orders,
    ROUND(AVG(Revenue), 0)     AS Avg_Revenue,
    ROUND(SUM(Revenue), 0)     AS Total_Revenue
FROM ecommerce_sales
GROUP BY Discount_Pct
ORDER BY Discount_Pct;

-- ── Q8: High Value Orders (Revenue > ₹20,000) ───────────────
SELECT
    Order_ID, Date, Customer_ID, Product,
    Category, Region, Revenue, Rating
FROM ecommerce_sales
WHERE Revenue > 20000
ORDER BY Revenue DESC
LIMIT 15;

-- ── Q9: City-wise Top Revenue ───────────────────────────────
SELECT
    City, Region,
    COUNT(*)               AS Orders,
    ROUND(SUM(Revenue), 0) AS Revenue
FROM ecommerce_sales
GROUP BY City, Region
ORDER BY Revenue DESC
LIMIT 10;

-- ── Q10: Quarter-wise Growth ────────────────────────────────
SELECT
    Quarter,
    COUNT(*)                   AS Orders,
    ROUND(SUM(Revenue), 0)     AS Quarterly_Revenue,
    ROUND(AVG(Revenue), 0)     AS Avg_Order_Value
FROM ecommerce_sales
GROUP BY Quarter
ORDER BY Quarter;
