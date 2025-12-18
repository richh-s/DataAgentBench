code = """import pandas as pd
import json

# Load the data from the file
with open(locals()['var_function-call-4533615524418986648'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date']).dt.normalize()
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter data from January 1, 2000 onwards (already done in SQL, but good to ensure)
df = df[df['Date'] >= '2000-01-01']

# Get the first closing price for each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_first_prices = df.groupby(['Index', 'YearMonth'])['CloseUSD'].first().reset_index()

# Calculate overall returns
results = []
for index_symbol in monthly_first_prices['Index'].unique():
    index_df = monthly_first_prices[monthly_first_prices['Index'] == index_symbol].sort_values('YearMonth')
    
    if len(index_df) == 0:
        continue

    # Total investment amount (e.g., $1 per month)
    total_invested = len(index_df) * 1  # Assuming $1 invested each month

    # Calculate the total value of investments at the last available closing price
    # We assume investments are made at the first price of each month.
    # The total value is calculated based on the last available closing price of the index.
    last_close_price = df[df['Index'] == index_symbol]['CloseUSD'].iloc[-1] # Get the last close price for the index
    
    # Sum of (last_close_price / monthly_first_price)
    total_current_value = (last_close_price / index_df['CloseUSD']).sum()
    
    # Calculate overall return
    overall_return = ((total_current_value - total_invested) / total_invested) * 100 if total_invested > 0 else 0
    
    results.append({'Index': index_symbol, 'OverallReturn': overall_return})

returns_df = pd.DataFrame(results)

# Sort by overall return and get the top 5
top_5_indices = returns_df.sort_values(by='OverallReturn', ascending=False).head(5)

# Mapping index to country based on the hint and general knowledge
index_to_country = {
    '000001.SS': 'China',
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    'GDAXI': 'Germany',
    'SPX': 'United States',
    'IXIC': 'United States',
    'DJI': 'United States',
    'TSX': 'Canada',
    'FTSE': 'United Kingdom',
    'AS51': 'Australia',
    'BSESN': 'India',
    'JCI': 'Indonesia',
    'KLSE': 'Malaysia',
    'KOSPI': 'South Korea',
    'NZ50': 'New Zealand',
    'STI': 'Singapore',
    'TWII': 'Taiwan',
    'RUT': 'United States',
    'SMSI': 'China' # Assuming SMSI is also China-related, like Shanghai Composite
}

top_5_indices['Country'] = top_5_indices['Index'].map(index_to_country)

# Convert to a list of dictionaries for the final output
final_result = top_5_indices.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-4533615524418986648': 'file_storage/function-call-4533615524418986648.json'}

exec(code, env_args)
