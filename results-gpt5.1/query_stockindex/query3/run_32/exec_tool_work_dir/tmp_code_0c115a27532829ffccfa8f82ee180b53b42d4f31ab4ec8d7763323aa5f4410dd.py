code = """import json, pandas as pd

path = var_call_NbKQpLDsJtaBHFKjiBgAJGWM
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure Date parsed correctly by taking only date part
df['Date'] = pd.to_datetime(df['Date'].str.slice(0,10), format='%Y-%m-%d')
df['Adj Close'] = df['Adj Close'].astype(float)

monthly = df.sort_values(['Index','Date']).groupby(['Index', pd.Grouper(key='Date', freq='MS')]).first().reset_index()

monthly['cum_units'] = 100 / monthly['Adj Close']
monthly['cum_units'] = monthly.groupby('Index')['cum_units'].cumsum()
monthly['final_price'] = monthly.groupby('Index')['Adj Close'].transform('last')
monthly['final_value'] = monthly['cum_units'] * monthly['final_price']

result = monthly.groupby('Index').agg(total_invested=('Adj Close', lambda x: 100*len(x)),
                                      final_value=('final_value','last'))
result['return_multiple'] = result['final_value'] / result['total_invested']

Top5 = result.sort_values('return_multiple', ascending=False).head(5).reset_index()

index_country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPC': 'United States',
    'IXIC': 'United States',
    'GDAXI': 'Germany',
    'FCHI': 'France',
    'STOXX50E': 'Eurozone',
    'FTSE': 'United Kingdom',
    'BVSP': 'Brazil',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'KS11': 'South Korea',
    'NSEI': 'India',
}

Top5['Country'] = Top5['Index'].map(index_country_map).fillna('Unknown')

answer = Top5.to_dict(orient='records')

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NbKQpLDsJtaBHFKjiBgAJGWM': 'file_storage/call_NbKQpLDsJtaBHFKjiBgAJGWM.json', 'var_call_e9EnscDxSQk5X41DE23tkjDY': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
