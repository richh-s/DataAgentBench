code = """import json
import pandas as pd
import dateutil.parser

# Load data
with open('var_function-call-16195887922252299573.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Clean and Parse Date
# The date formats are mixed. pd.to_datetime with format='mixed' helps.
# However, 'mixed' might not be available in older pandas.
# Let's try to convert using dateutil if to_datetime fails or just let pandas handle it.
# The preview showed: "31 Dec 1986, 00:00", "January 02, 1987 at 12:00 AM", "1987-01-05 00:00:00"
# These are parseable.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback if format='mixed' is not supported in this env
    df['Date'] = df['Date'].apply(dateutil.parser.parse)

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with NaN in Date or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD'])

# Filter for data since 2000
df = df[df['Date'] >= '2000-01-01']

# Sort by Index and Date
df = df.sort_values(['Index', 'Date'])

# Identify first trading day of each month for each index
# Create a 'Month' column (YYYY-MM)
df['YearMonth'] = df['Date'].dt.to_period('M')

# Group by Index and YearMonth, take the first entry (min Date)
monthly_investments = df.groupby(['Index', 'YearMonth']).head(1)

# Calculate ROI for each index
results = []
indices = df['Index'].unique()

for idx in indices:
    # Get investments
    inv_data = monthly_investments[monthly_investments['Index'] == idx]
    
    if inv_data.empty:
        continue
    
    # Check if data covers a reasonable range (starts near 2000?)
    # The prompt says "since 2000". If an index started in 2010, the "since 2000" investment strategy 
    # would just start investing in 2010.
    
    # Calculate shares bought (assume $1 investment per month)
    shares = (1.0 / inv_data['CloseUSD']).sum()
    total_invested = len(inv_data)
    
    # Get final price (the very last available date in the dataset for this index)
    last_price = df[df['Index'] == idx].iloc[-1]['CloseUSD']
    
    final_value = shares * last_price
    
    # ROI Percentage
    roi = (final_value - total_invested) / total_invested * 100
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'TotalInvested': total_invested,
        'FinalValue': final_value,
        'StartDate': inv_data['Date'].min().strftime('%Y-%m-%d'),
        'EndDate': df[df['Index'] == idx]['Date'].max().strftime('%Y-%m-%d')
    })

# Convert to DataFrame to sort
res_df = pd.DataFrame(results)
res_df = res_df.sort_values('ROI', ascending=False)

# Get Top 5
top_5 = res_df.head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-11103673439672531261': ['index_info'], 'var_function-call-11103673439672530174': ['index_trade'], 'var_function-call-11103673439672529087': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-11103673439672532096': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_function-call-8652362811134081670': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-8652362811134080107': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6622336040025501380': [{'count_star()': '104224'}], 'var_function-call-16195887922252299573': 'file_storage/function-call-16195887922252299573.json'}

exec(code, env_args)
