code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-15839610252102377840']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Date
# The dates are messy. pd.to_datetime is smart.
# "January 02, 1987 at 12:00 AM" -> %B %d, %Y at %I:%M %p
# "31 Dec 1986, 00:00" -> %d %b %Y, %H:%M
# "1987-01-05 00:00:00" -> ISO
# We can try to replace " at " with " " and remove ", " to simplify?
# Or just let pandas handle it.

# Try standard conversion first
# Note: In the provided environment, dateutil parser used by pandas usually handles these.
df['Date_Parsed'] = pd.to_datetime(df['Date'], errors='coerce')

# Check for nulls
# If any dates failed to parse, we might need to handle them.
# Assuming standard formats, it should be fine.

# Filter >= 2000-01-01
df = df[df['Date_Parsed'] >= '2000-01-01']

# Sort
df = df.sort_values(['Index', 'Date_Parsed'])

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Group by Index
results = []

for idx, group in df.groupby('Index'):
    group = group.sort_values('Date_Parsed')
    
    # Check start date
    start_date = group['Date_Parsed'].iloc[0]
    if start_date.year > 2000:
        # Exclude if starts significantly later
        # e.g. NSEI starts 2007. J203.JO starts 2012.
        # Allow if it starts in Jan/Feb 2000.
        continue
        
    # Resample to monthly. Get the first trading day of each month.
    # Create a Month identifier
    group['Month'] = group['Date_Parsed'].dt.to_period('M')
    
    # Take the first entry per month
    monthly_investments = group.groupby('Month').first().reset_index()
    
    # Calculate DCA
    # Invest 1 unit of currency (USD) each month
    monthly_investments['Units_Bought'] = 1.0 / monthly_investments['CloseUSD']
    
    total_units = monthly_investments['Units_Bought'].sum()
    total_invested = len(monthly_investments)
    
    # Final Value
    # Using the last available price in the dataset for that index
    last_price = group['CloseUSD'].iloc[-1]
    final_value = total_units * last_price
    
    # Return Multiple
    multiple = final_value / total_invested if total_invested > 0 else 0
    
    results.append({
        'Index': idx,
        'Multiple': multiple,
        'Final_Value': final_value,
        'Total_Invested': total_invested,
        'Last_Date': group['Date_Parsed'].iloc[-1].strftime('%Y-%m-%d')
    })

# Convert to DataFrame for sorting
res_df = pd.DataFrame(results).sort_values('Multiple', ascending=False)

# Map countries
country_map = {
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N100': 'Europe',
    'J203.JO': 'South Africa',
    'NSEI': 'India'
}

res_df['Country'] = res_df['Index'].map(country_map)

# Get top 5
top_5 = res_df.head(5)[['Index', 'Country', 'Multiple']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-18360343161845397000': ['index_info'], 'var_function-call-18360343161845398715': ['index_trade'], 'var_function-call-15998170493143971984': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-15998170493143971577': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16188891357112266804': [{'Index': 'J203.JO', 'usd_count': '1854', 'adj_count': '1854', 'min_date': '2012-02-08 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'usd_count': '7979', 'adj_count': '7979', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'usd_count': '6506', 'adj_count': '6506', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'usd_count': '2577', 'adj_count': '2577', 'min_date': '2007-09-25 00:00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'usd_count': '5590', 'adj_count': '5590', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'IXIC', 'usd_count': '7351', 'adj_count': '7351', 'min_date': '2000-01-06 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'HSI', 'usd_count': '5604', 'adj_count': '5604', 'min_date': '2000-01-14 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NYA', 'usd_count': '7960', 'adj_count': '7960', 'min_date': '2000-01-03 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'usd_count': '4245', 'adj_count': '4245', 'min_date': '2000-01-10 00:00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'usd_count': '4355', 'adj_count': '4355', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '000001.SS', 'usd_count': '4354', 'adj_count': '4354', 'min_date': '2000-01-04 00:00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'usd_count': '5188', 'adj_count': '5188', 'min_date': '2000-01-05 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'usd_count': '4385', 'adj_count': '4385', 'min_date': '2000-01-17 00:00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_function-call-2242398351796785036': 'file_storage/function-call-2242398351796785036.json', 'var_function-call-15839610252102377840': 'file_storage/function-call-15839610252102377840.json'}

exec(code, env_args)
