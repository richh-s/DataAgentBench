code = """import json
import pandas as pd
from dateutil import parser

with open(locals()['var_function-call-4359623576049279886'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
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

results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    sub.set_index('Date', inplace=True)
    sub['YearMonth'] = sub.index.to_period('M')
    monthly_investments = sub.groupby('YearMonth').first()
    
    total_invested = len(monthly_investments)
    if total_invested == 0:
        continue
        
    units_bought = 1 / monthly_investments['Adj Close']
    total_units = units_bought.sum()
    last_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Return': overall_return,
        'StartDate': str(monthly_investments.index[0])
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)
print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-2913934071525250979': ['index_info'], 'var_function-call-2913934071525250614': ['index_trade'], 'var_function-call-3711871085042799337': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-3711871085042802130': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-63921800962576420': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-63921800962578793': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-6037072348525956933': [{'count_star()': '104224'}], 'var_function-call-4359623576049279886': 'file_storage/function-call-4359623576049279886.json', 'var_function-call-17823732982549569091': [{'Index': 'IXIC', 'Country': 'USA', 'Return': 3.8269431542}, {'Index': 'NSEI', 'Country': 'India', 'Return': 1.3584273446}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.3474875235}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3470287159}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.2982076187}], 'var_function-call-9082556908609941110': {'399001.SZ': '2000-01-04', 'GDAXI': '2000-01-03', 'IXIC': '2000-01-03', 'NSEI': '2007-09-17', 'TWII': '2000-01-04'}}

exec(code, env_args)
