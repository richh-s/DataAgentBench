code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-7948131773756513851'], 'r') as f:
    trade_data = json.load(f)

df_trade = pd.DataFrame(trade_data)
df_trade["Date"] = pd.to_datetime(df_trade["Date"])
df_trade["CloseUSD"] = pd.to_numeric(df_trade["CloseUSD"])

# Get the first available date for each month for each index
df_monthly_first = df_trade.groupby([df_trade["Index"], df_trade["Date"].dt.to_period("M")])["CloseUSD"].transform("first")
df_trade["MonthlyFirstClose"] = df_monthly_first

# Filter to get only the data from the first trading day of each month
# This simulates investing at the beginning of each month
df_investments = df_trade[df_trade["CloseUSD"] == df_trade["MonthlyFirstClose"]]
df_investments = df_investments.drop_duplicates(subset=["Index", "Date"]).copy()

# Calculate returns for each index
returns = {}
for index_symbol in df_investments["Index"].unique():
    index_df = df_investments[df_investments["Index"] == index_symbol].sort_values("Date")

    if not index_df.empty:
        # Assuming an initial investment of $1 at the start of each month
        # The total value would be the sum of (final_price / investment_price)
        initial_investment_per_month = 1.0
        total_value = 0.0
        for i in range(len(index_df)):
            if i + 1 < len(index_df):
                # Calculate return for each monthly investment
                return_on_investment = (index_df.iloc[-1]["CloseUSD"] / index_df.iloc[i]["CloseUSD"])
                total_value += initial_investment_per_month * return_on_investment
            else:
                # For the last investment, its final value is just 1 unit, as we don't know the future return
                total_value += initial_investment_per_month


        # Total return is the total value minus total invested amount, divided by total invested amount.
        # However, a simpler way for regular investments is to average the final value of each $1 invested.
        # This is equivalent to summing up final prices of each $1 invested and dividing by the number of investments.
        # Let's re-think the return calculation.
        # If an investor makes regular monthly investments, it means they buy a certain amount of index
        # at the start of each month. Let's assume they invest 1 unit of currency each month.
        # The total return would be (sum of final values of each monthly investment - total invested) / total invested
        # This is a cumulative return.

        # Let's simplify: the total return is the final closing price divided by the first closing price,
        # adjusted by the number of investments to simulate continuous investment.
        # Or, a more robust way to model regular monthly investments:
        # Assume an investor invests $1 at the beginning of each month.
        # The value of that $1 at the end of the period is final_close / investment_close.
        # Sum these up for all monthly investments.

        if len(index_df) > 1:
            cumulative_return_values = []
            for i in range(len(index_df)):
                # Value of a $1 investment made at month 'i' at the end of the period
                value_at_end = index_df.iloc[-1]["CloseUSD"] / index_df.iloc[i]["CloseUSD"]
                cumulative_return_values.append(value_at_end)
            
            # The average of these values represents the overall return for each dollar invested
            overall_return = (sum(cumulative_return_values) / len(cumulative_return_values)) - 1
            returns[index_symbol] = overall_return
        elif len(index_df) == 1: # Only one data point, no return
            returns[index_symbol] = 0.0
    else:
        returns[index_symbol] = 0.0

# Sort indices by returns in descending order
sorted_indices = sorted(returns.items(), key=lambda item: item[1], reverse=True)

# Get the top 5 indices
top_5_indices = sorted_indices[:5]

print("__RESULT__:")
print(json.dumps(top_5_indices))"""

env_args = {'var_function-call-7948131773756513851': 'file_storage/function-call-7948131773756513851.json'}

exec(code, env_args)
