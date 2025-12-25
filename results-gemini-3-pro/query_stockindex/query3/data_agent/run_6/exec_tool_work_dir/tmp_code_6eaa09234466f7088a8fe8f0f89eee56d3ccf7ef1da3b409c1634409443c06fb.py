code = """import json
import pandas as pd
from dateutil import parser

# Load data
with open(locals()['var_function-call-4359623576049279886'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are in various formats. pd.to_datetime with errors='coerce' and infer_datetime_format=True (deprecated) or format='mixed' (new in pandas 2.0)
# Since I don't know the pandas version, I will try using dateutil parser in a lambda or just pd.to_datetime without format
# But 'January 02, 1987 at 12:00 AM' might be tricky for standard to_datetime without format='mixed'
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback if format='mixed' is not supported or fails
    from dateutil import parser
    def parse_dt(x):
        try:
            return parser.parse(x)
        except:
            return pd.NaT
    df['Date'] = df['Date'].apply(parse_dt)

df = df.dropna(subset=['Date', 'Adj Close'])
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01'].sort_values('Date')

# Define function to calculate return
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    sub.set_index('Date', inplace=True)
    
    # Resample to monthly start or similar. 
    # Strategy: Invest on the first available day of each month.
    # We can group by Year-Month and take the first entry.
    sub['YearMonth'] = sub.index.to_period('M')
    monthly_investments = sub.groupby('YearMonth').first()
    
    # Calculate investment
    # Invest 1 unit of currency each month
    total_invested = len(monthly_investments)
    if total_invested == 0:
        continue
        
    # Units bought = 1 / Price
    units_bought = 1 / monthly_investments['Adj Close']
    total_units = units_bought.sum()
    
    # Final value = Total Units * Last Price
    # Last price is the last available price in the dataset for this index
    last_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Return': overall_return,
        'TotalInvested': total_invested,
        'FinalValue': final_value,
        'StartDate': monthly_investments.index[0],
        'EndDate': monthly_investments.index[-1]
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

# Mapping
mapping = {
    'NYA': 'USA',
    'IXIC': 'USA',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'N225': 'Japan',
    'N100': 'Europe', 
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

top5 = results_df.head(5)
top5['Country'] = top5['Index'].map(mapping)

print("__RESULT__:")
print(top5[['Index', 'Country', 'Return']].to_json(orient='records'))"""

env_args = {'var_function-call-2913934071525250979': ['index_info'], 'var_function-call-2913934071525250614': ['index_trade'], 'var_function-call-3711871085042799337': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3711871085042802130': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-63921800962576420': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-63921800962578793': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-6037072348525956933': [{'count_star()': '104224'}], 'var_function-call-4359623576049279886': 'file_storage/function-call-4359623576049279886.json'}

exec(code, env_args)
