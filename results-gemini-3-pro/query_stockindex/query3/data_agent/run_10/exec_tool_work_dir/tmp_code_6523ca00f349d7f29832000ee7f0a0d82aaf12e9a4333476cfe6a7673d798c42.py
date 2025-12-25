code = """import pandas as pd
import json
import datetime

# Load data
with open(locals()['var_function-call-14265084757085608486'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates
def parse_date(date_str):
    # Formats: 
    # "31 Dec 1986, 00:00" -> "%d %b %Y, %H:%M"
    # "January 02, 1987 at 12:00 AM" -> "%B %d, %Y at %I:%M %p"
    # "1987-01-05 00:00:00" -> "%Y-%m-%d %H:%M:%S"
    try:
        return pd.to_datetime(date_str)
    except:
        pass
    
    try:
        return datetime.datetime.strptime(date_str, "%d %b %Y, %H:%M")
    except:
        pass
    
    try:
        return datetime.datetime.strptime(date_str, "%B %d, %Y at %I:%M %p")
    except:
        pass
        
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except:
        pass
    
    return pd.NaT

# Apply parsing (this might be slow loop, try to optimize if needed, but 100k is okay)
# Let's try pd.to_datetime with format='mixed' first if available, else fallback
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Manual apply
    df['Date'] = df['Date'].apply(parse_date)

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Sort by Date
df = df.sort_values(['Index', 'Date'])

# Ensure Adj Close is float
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df = df.dropna(subset=['Adj Close'])

# Group by Index and process
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    
    # Resample to get first trading day of each month
    # Create a YearMonth column
    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    
    # Drop duplicates keeping first
    monthly_buy = sub.drop_duplicates(subset=['YearMonth'], keep='first')
    
    # Calculate investment
    # Invest 1 unit each month
    monthly_buy['Units'] = 1 / monthly_buy['Adj Close']
    
    total_units = monthly_buy['Units'].sum()
    total_invested = len(monthly_buy)
    
    # Final price (last available price in dataset for that index)
    final_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * final_price
    
    if total_invested > 0:
        pct_return = (final_value - total_invested) / total_invested * 100
        # start_date = monthly_buy.iloc[0]['Date']
        # end_date = sub.iloc[-1]['Date']
        results.append({
            'Index': idx,
            'Return': pct_return,
            'Total_Invested': total_invested,
            'Final_Value': final_value
        })

# Create DataFrame of results
res_df = pd.DataFrame(results).sort_values('Return', ascending=False)

# Top 5
top5 = res_df.head(5)

# Add country info (Hardcoded mapping based on index symbols)
# Index mapping
index_country_map = {
    "J203.JO": "South Africa",
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "HSI": "Hong Kong",
    "IXIC": "United States",
    "NYA": "United States",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "399001.SZ": "China"
}

top5['Country'] = top5['Index'].map(index_country_map)

print("__RESULT__:")
print(top5.to_json(orient='records'))"""

env_args = {'var_function-call-12184386225509086772': ['index_info'], 'var_function-call-2651222669085114326': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6542151878181096001': ['index_trade'], 'var_function-call-14272459974564012930': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-468282391932724668': [{'Date': '31 Dec 1986, 00:00', 'Index': 'HSI', 'Adj Close': '2568.300049'}, {'Date': 'January 02, 1987 at 12:00 AM', 'Index': 'HSI', 'Adj Close': '2540.100098'}, {'Date': '1987-01-05 00:00:00', 'Index': 'HSI', 'Adj Close': '2552.399902'}, {'Date': '06 Jan 1987, 00:00', 'Index': 'HSI', 'Adj Close': '2583.899902'}, {'Date': '07 Jan 1987, 00:00', 'Index': 'HSI', 'Adj Close': '2607.100098'}], 'var_function-call-15222818763261342873': [{'count_star()': '104224'}], 'var_function-call-14265084757085608486': 'file_storage/function-call-14265084757085608486.json'}

exec(code, env_args)
