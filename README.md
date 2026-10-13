# 🛒 RetailSense — E-Commerce Sales Analysis

**Analyst:** Akash Kumar | B.Tech CSE '26
**Tools:** Python · Pandas · SQL · Excel · Chart.js

---

## 📌 Project Overview
End-to-end analysis of 1,000 e-commerce orders across 5 product categories,
4 regions, and 12 months (FY 2023) to uncover revenue patterns, top-performing
products, and customer behaviour insights.

---

## 📊 Key Findings
| Metric | Value |
|---|---|
| Total Revenue | ₹60,96,654 |
| Total Orders | 1,000 |
| Avg Order Value | ₹6,096 |
| Unique Customers | 432 |
| Best Category | Electronics (46% revenue) |
| Best Region | South |
| Peak Month | October |
| Top Product | Laptop (₹18.2L revenue) |

---

## 🗂️ Project Structure
```
ecommerce-project/
├── data/
│   ├── ecommerce_sales.csv     # Raw dataset (1000 rows, 15 columns)
│   └── Ecommerce_Analysis.xlsx # 8-sheet Excel workbook
├── sql/
│   └── queries.sql             # 10 business SQL queries
├── dashboard/
│   └── index.html              # Interactive web dashboard
├── analysis.py                 # Python EDA script
└── README.md
```

---

## 🔍 SQL Queries Covered
1. KPI Summary (Revenue, Orders, AOV)
2. Revenue by Category (Ranked)
3. Monthly Revenue Trend
4. Region-wise Performance
5. Top 10 Products
6. Payment Mode Analysis
7. Discount Impact Study
8. High Value Orders Filter
9. City-wise Revenue
10. Quarterly Growth Comparison

---

## 📁 Dataset Columns
`Order_ID · Date · Month · Quarter · Customer_ID · Region · City ·
Category · Product · Quantity · Unit_Price · Discount_Pct · Revenue ·
Payment_Mode · Rating`

---

## 🚀 Live Dashboard
🔗 [View Dashboard](https://aksingh2004.github.io/ecommerce-dashboard/)
