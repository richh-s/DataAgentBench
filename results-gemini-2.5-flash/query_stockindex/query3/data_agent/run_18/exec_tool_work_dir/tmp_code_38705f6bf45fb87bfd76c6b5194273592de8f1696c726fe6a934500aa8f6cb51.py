code = """import pandas as pd
import json

df = pd.read_json(locals()["var_function-call-15735413083344890865"])

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])
df = df[df["Date"].dt.year >= 2000]

# Sort by Index and Date to easily get the first day of each month
df = df.sort_values(by=["Index", "Date"])

# Get the first trading day of each month for each index
df["year_month"] = df["Date"].dt.to_period("M")
monthly_data = df.groupby(["Index", "year_month"]).first().reset_index()

# Calculate the return for each index
returns = {}
for index_symbol in monthly_data["Index"].unique():
    index_df = monthly_data[monthly_data["Index"] == index_symbol].copy()
    index_df["CloseUSD"] = pd.to_numeric(index_df["CloseUSD"], errors="coerce")
    index_df = index_df.dropna(subset=["CloseUSD"])

    if len(index_df) > 0:
        total_invested = len(index_df) # Assuming 1 USD invested each month
        total_value = index_df["CloseUSD"].sum()
        overall_return = (total_value - total_invested) / total_invested
        returns[index_symbol] = overall_return

# Sort by return and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

__RESULT__:
print(json.dumps(top_5_indices))"""

env_args = {'var_function-call-15735413083344890865': 'file_storage/function-call-15735413083344890865.json'}

exec(code, env_args)
