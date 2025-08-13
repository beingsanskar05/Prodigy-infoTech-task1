import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace filename if needed)
df = pd.read_csv("Task01_Dataset.csv", skiprows=4)
df.columns = df.columns.str.strip()

# Melt into long format
df_melted = pd.melt(df,
                    id_vars=["Country Name", "Indicator Name"],
                    var_name="Year",
                    value_name="Value")

# Clean data
df_melted["Value"] = pd.to_numeric(df_melted["Value"], errors="coerce")
df_melted = df_melted.dropna()

countries_to_plot = ["India", "China", "United States"]

subset = df_melted[df_melted["Country Name"].isin(countries_to_plot)]

plt.figure(figsize=(12, 6))
sns.histplot(data=subset, x="Value", hue="Country Name", bins=50, kde=True)
plt.title("Distribution of Indicator Values - Selected Countries")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


avg_by_country = df_melted.groupby("Country Name")["Value"].mean().sort_values(ascending=False)
top_20 = avg_by_country.head(20)

plt.figure(figsize=(14, 6))
top_20.plot(kind="bar")
plt.title("Top 20 Countries by Average Indicator Value")
plt.xlabel("Country")
plt.ylabel("Average Value")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

     

