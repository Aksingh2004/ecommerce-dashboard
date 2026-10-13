# ============================================================
#  E-Commerce Sales Analysis  |  Akash Kumar
#  Tools: Python, Pandas, Matplotlib, Seaborn
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── 1. Load & Inspect Data ──────────────────────────────────
df = pd.read_csv("data/ecommerce_sales.csv", parse_dates=["Date"])
print("="*55)
print("  DATASET OVERVIEW")
print("="*55)
print(f"  Total Orders   : {len(df):,}")
print(f"  Date Range     : {df['Date'].min().date()} → {df['Date'].max().date()}")
print(f"  Total Revenue  : ₹{df['Revenue'].sum():,.0f}")
print(f"  Avg Order Value: ₹{df['Revenue'].mean():,.0f}")
print(f"  Unique Customers: {df['Customer_ID'].nunique()}")
print(f"  Columns        : {list(df.columns)}")

# ── 2. Data Cleaning ────────────────────────────────────────
print("\n── Null Values ──")
print(df.isnull().sum())
print("\n── Duplicates ──", df.duplicated().sum())
df["Month_Num"] = df["Date"].dt.month
df["Year"]      = df["Date"].dt.year

# ── 3. KPI Summary ──────────────────────────────────────────
print("\n" + "="*55)
print("  KEY PERFORMANCE INDICATORS")
print("="*55)

total_rev  = df["Revenue"].sum()
total_ord  = len(df)
aov        = total_rev / total_ord
top_cat    = df.groupby("Category")["Revenue"].sum().idxmax()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()

print(f"  Total Revenue      : ₹{total_rev:,.0f}")
print(f"  Total Orders       : {total_ord:,}")
print(f"  Avg Order Value    : ₹{aov:,.0f}")
print(f"  Best Category      : {top_cat}")
print(f"  Best Region        : {top_region}")

# ── 4. Monthly Revenue Trend ────────────────────────────────
monthly = (df.groupby("Month_Num")["Revenue"]
             .sum()
             .reset_index()
             .sort_values("Month_Num"))
months  = ["Jan","Feb","Mar","Apr","May","Jun",
           "Jul","Aug","Sep","Oct","Nov","Dec"]
monthly["Month_Name"] = monthly["Month_Num"].apply(lambda x: months[x-1])

# ── 5. Category Revenue ─────────────────────────────────────
cat_rev = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

# ── 6. Regional Revenue ─────────────────────────────────────
reg_rev = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

# ── 7. Payment Mode ─────────────────────────────────────────
pay_cnt = df["Payment_Mode"].value_counts()

# ── 8. Top 5 Products ───────────────────────────────────────
top5 = (df.groupby("Product")
          .agg(Orders=("Order_ID","count"),
               Revenue=("Revenue","sum"),
               Avg_Rating=("Rating","mean"))
          .sort_values("Revenue", ascending=False)
          .head(5))
print("\n── Top 5 Products by Revenue ──")
print(top5.to_string())

# ── 9. VISUALISATIONS ───────────────────────────────────────
sns.set_theme(style="darkgrid", palette="deep")
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("E-Commerce Sales Analysis Dashboard — Akash Kumar",
             fontsize=15, fontweight="bold", y=1.01)

colors_cat = ["#7c3aed","#a78bfa","#4f46e5","#818cf8","#c4b5fd"]

# Plot 1 — Monthly Revenue Trend
ax1 = axes[0,0]
ax1.plot(monthly["Month_Name"], monthly["Revenue"]/1000,
         marker="o", color="#7c3aed", linewidth=2.5, markersize=6)
ax1.fill_between(monthly["Month_Name"], monthly["Revenue"]/1000,
                 alpha=0.15, color="#7c3aed")
ax1.set_title("Monthly Revenue Trend (₹ in Thousands)", fontweight="bold")
ax1.set_xlabel("Month"); ax1.set_ylabel("Revenue (₹K)")
ax1.tick_params(axis="x", rotation=45)

# Plot 2 — Category Revenue
ax2 = axes[0,1]
bars = ax2.bar(cat_rev.index, cat_rev.values/1000, color=colors_cat, edgecolor="white")
ax2.set_title("Revenue by Category (₹ in Thousands)", fontweight="bold")
ax2.set_xlabel("Category"); ax2.set_ylabel("Revenue (₹K)")
ax2.tick_params(axis="x", rotation=20)
for bar in bars:
    ax2.text(bar.get_x()+bar.get_width()/2,
             bar.get_height()+0.5,
             f"₹{bar.get_height():.0f}K",
             ha="center", fontsize=8, fontweight="bold")

# Plot 3 — Regional Revenue Pie
ax3 = axes[1,0]
wedge_colors = ["#7c3aed","#a78bfa","#4f46e5","#c4b5fd"]
ax3.pie(reg_rev.values, labels=reg_rev.index,
        autopct="%1.1f%%", colors=wedge_colors,
        startangle=90, pctdistance=0.82,
        wedgeprops=dict(edgecolor="white", linewidth=2))
ax3.set_title("Revenue Distribution by Region", fontweight="bold")

# Plot 4 — Payment Mode Bar
ax4 = axes[1,1]
pay_bar = ax4.barh(pay_cnt.index, pay_cnt.values,
                   color=["#7c3aed","#a78bfa","#4f46e5","#818cf8","#c4b5fd"],
                   edgecolor="white")
ax4.set_title("Orders by Payment Mode", fontweight="bold")
ax4.set_xlabel("Number of Orders")
for bar in pay_bar:
    ax4.text(bar.get_width()+1, bar.get_y()+bar.get_height()/2,
             str(int(bar.get_width())), va="center", fontsize=9)

plt.tight_layout()
plt.savefig("dashboard/analysis_charts.png", dpi=150, bbox_inches="tight")
print("\n✅ Charts saved to dashboard/analysis_charts.png")
plt.close()
print("\n✅ Python analysis complete!")
