code = """import json
import pandas as pd
from datetime import datetime

# Read the file path from storage
file_path = var_functions.query_db_12
if isinstance(file_path, str):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = var_functions.query_db_12

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date strings to datetime objects
def parse_date(date_str):
    try:
        # Try different date formats
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d',
            '%d %b %Y, %H:%M',
            '%B %d, %Y at %H:%M %p',
            '%B %d, %Y'
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                continue
        return None
    except:
        return None

df['Date_parsed'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date_parsed'])

# Filter for dates from 2000 onwards
df = df[df['Date_parsed'] >= datetime(2000, 1, 1)]

# Create year-month column for monthly aggregation
df['YearMonth'] = df['Date_parsed'].dt.to_period('M')

# Get first trading day of each month for each index (simulating monthly investment)
monthly_data = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Sort by Index and Date to ensure proper ordering
monthly_data = monthly_data.sort_values(['Index', 'Date_parsed'])

# Calculate returns for each index assuming $100 invested monthly
def calculate_returns(group):
    if len(group) < 2:
        return None
    
    # Monthly investment of $100
    monthly_investment = 100
    total_invested = monthly_investment * len(group)
    
    # Calculate units purchased each month
    group = group.copy()
    group['Units'] = monthly_investment / group['CloseUSD']
    
    # Total units accumulated
    total_units = group['Units'].sum()
    
    # Final value (using last price)
    final_value = total_units * group['CloseUSD'].iloc[-1]
    
    # Total return
    total_return = final_value - total_invested
    return_percentage = (total_return / total_invested) * 100
    
    return {
        'Index': group['Index'].iloc[0],
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percentage': return_percentage,
        'Months': len(group),
        'First_Date': group['Date_parsed'].iloc[0],
        'Last_Date': group['Date_parsed'].iloc[-1]
    }

# Calculate returns for each index
index_returns = []
for index in monthly_data['Index'].unique():
    index_data = monthly_data[monthly_data['Index'] == index]
    result = calculate_returns(index_data)
    if result:
        index_returns.append(result)

# Convert to DataFrame and sort by return percentage
returns_df = pd.DataFrame(index_returns)
returns_df = returns_df.sort_values('Return_Percentage', ascending=False)

# Get top 5 indices
top_5 = returns_df.head(5)

# Map index codes to exchanges and countries
index_to_exchange = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange', 
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'GDAXI': 'Frankfurt Stock Exchange',
    'N100': 'Euronext',
    'GSPTSE': 'Toronto Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'SSMI': 'Swiss Stock Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'J203.JO': 'Johannesburg Stock Exchange'
}

# Map exchanges to countries
exchange_to_country = {
    'Tokyo Stock Exchange': 'Japan',
    'Hong Kong Stock Exchange': 'Hong Kong',
    'Shanghai Stock Exchange': 'China',
    'Shenzhen Stock Exchange': 'China',
    'New York Stock Exchange': 'United States',
    'NASDAQ': 'United States',
    'Frankfurt Stock Exchange': 'Germany',
    'Euronext': 'Europe (Multiple)',
    'Toronto Stock Exchange': 'Canada',
    'National Stock Exchange of India': 'India',
    'Swiss Stock Exchange': 'Switzerland',
    'Taiwan Stock Exchange': 'Taiwan',
    'Johannesburg Stock Exchange': 'South Africa'
}

# Add exchange and country information
top_5['Exchange'] = top_5['Index'].map(index_to_exchange)
top_5['Country'] = top_5['Exchange'].map(exchange_to_country)

result = top_5[['Index', 'Exchange', 'Country', 'Return_Percentage', 'Total_Invested', 'Final_Value']].copy()
result['Return_Percentage'] = result['Return_Percentage'].round(2)

result_json = result.to_json(orient='records')
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:7': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
