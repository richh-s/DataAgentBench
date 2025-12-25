code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-14095839042875052654'])

df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

df = df[df['Date'].dt.year >= 2000]

# Get the first trading day of each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_first_day = df.loc[df.groupby(['Index', 'YearMonth'])['Date'].idxmin()]

# Calculate returns for each index
returns = {}
for index_name, group in monthly_first_day.groupby('Index'):
    # Assuming an equal monthly investment, sum up the inverse of the prices
    # and multiply by the last price to simulate returns
    # This is a simplified approach for "overall returns" with "regular monthly investments"
    # A more precise calculation would involve portfolio value over time.
    # For simplicity, we are calculating the growth of 1 unit invested each month.
    # The total return is (sum of (last_price / monthly_investment_price)) / number_of_investments - 1
    # or, if we assume a fixed amount invested, the number of shares bought each month would be
    # fixed_investment_amount / monthly_price.
    # Then, total value = sum(shares_bought_each_month * last_price).
    # Let's use a simplified approach: assume 1 unit of currency is invested each month.
    # The "return" will be the sum of (final_price / investment_price) for all monthly investments.

    # For a fair comparison of total return with regular monthly investments, we can simulate investing 1 USD each month.
    # The number of shares bought each month would be 1 / CloseUSD.
    # The total number of shares accumulated is the sum of (1 / CloseUSD) for each month.
    # The final value of these accumulated shares is (total_shares * last_CloseUSD).
    # Initial investment would be the number of months * 1 USD.

    if len(group) > 1: # Need at least two points to calculate a meaningful return
        total_investment_amount = len(group)
        total_final_value = (1 / group['CloseUSD']).sum() * group['CloseUSD'].iloc[-1]
        overall_return = (total_final_value / total_investment_amount) - 1
        returns[index_name] = overall_return

# Sort by returns and get the top 5
sorted_returns = sorted(returns.items(), key=lambda item: item[1], reverse=True)
top_5_indices = sorted_returns[:5]

# Prepare the result for the next step
result_indices = []
for index_symbol, return_value in top_5_indices:
    result_indices.append({'Index': index_symbol, 'Return': return_value})

print('__RESULT__:')
print(json.dumps(result_indices))"""

env_args = {'var_function-call-14095839042875052654': 'file_storage/function-call-14095839042875052654.json'}

exec(code, env_args)
