code = """import pandas as pd
import json

# Load the data from the file
with open(locals()['var_function-call-4533615524418986648'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Date to datetime, handling potential errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.normalize()

# Convert CloseUSD to numeric, coercing errors will turn invalid parsing into NaN
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows where Date or CloseUSD could not be parsed
df.dropna(subset=['Date', 'CloseUSD'], inplace=True)

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

    # Get the latest closing price for the current index from the full dataframe
    # Ensure there's a last close price to avoid index errors on empty slices
    if not df[df['Index'] == index_symbol]['CloseUSD'].empty:
        last_close_price = df[df['Index'] == index_symbol]['CloseUSD'].iloc[-1]
    else:
        last_close_price = 0 # Or handle as an error case, here 0 will result in 0 return

    # Sum of (last_close_price / monthly_first_price) for each monthly investment
    if last_close_price != 0: # Avoid division by zero if last_close_price is 0
        total_current_value = (last_close_price / index_df['CloseUSD']).sum()
    else:
        total_current_value = 0
    
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
    'SMSI': 'China', # Assuming SMSI is also China-related
    'NSEI': 'India', # Nifty 50 Index
    '399001.SZ': 'China' # SZSE Component Index
}

# Apply the mapping
top_5_indices['Country'] = top_5_indices['Index'].map(index_to_country)

# Replace any NaN values in the 'Country' column with None for JSON serialization
top_5_indices['Country'] = top_5_indices['Country'].apply(lambda x: None if pd.isna(x) else x)

# Convert to a list of dictionaries for the final output
final_result = top_5_indices.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-4533615524418986648': 'file_storage/function-call-4533615524418986648.json', 'var_function-call-2575415461627619627': [{'Index': 'IXIC', 'OverallReturn': 382.20467671180944, 'Country': 'United States'}, {'Index': 'NSEI', 'OverallReturn': 136.08849755128486, 'Country': nan}, {'Index': 'GDAXI', 'OverallReturn': 134.7462383645538, 'Country': 'Germany'}, {'Index': '399001.SZ', 'OverallReturn': 134.4545336356674, 'Country': nan}, {'Index': 'TWII', 'OverallReturn': 123.74061754244634, 'Country': 'Taiwan'}]}

exec(code, env_args)
