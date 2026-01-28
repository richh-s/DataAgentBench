code = """import json, pandas as pd

trade_src = var_call_1REGSUHyxGGaKaXFYTnMX03V
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trade = json.load(f)
else:
    trade = trade_src

df = pd.DataFrame(trade)
# robust datetime parsing
s = df['Date'].astype(str).str.replace(' 00:00:00','', regex=False)
df['Date'] = pd.to_datetime(s, errors='coerce', format='%Y-%m-%d')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date','CloseUSD'])

monthly = (df.sort_values(['Index','Date'])
             .assign(YearMonth=lambda x: x['Date'].dt.to_period('M'))
             .groupby(['Index','YearMonth'], as_index=False)
             .agg(Date=('Date','max'), Price=('CloseUSD','last')))
monthly = monthly[monthly['YearMonth'] >= pd.Period('2000-01', freq='M')]

monthly_sorted = monthly.sort_values(['Index','YearMonth'])
last_price = monthly_sorted.groupby('Index').tail(1).set_index('Index')['Price']
units = monthly_sorted.assign(inv_units=lambda x: 1.0/x['Price']).groupby('Index')['inv_units'].sum()
contrib_months = monthly_sorted.groupby('Index').size()
final_value = units * last_price
invested = contrib_months.astype(float)
return_multiple = final_value / invested

res = (pd.DataFrame({
    'Index': return_multiple.index,
    'months': contrib_months.values,
    'invested_usd': invested.values,
    'final_value_usd': final_value.values,
    'return_multiple': return_multiple.values,
    'overall_return_pct': (return_multiple.values - 1.0) * 100.0,
}).sort_values('return_multiple', ascending=False))

index_to_country = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'N225': 'Japan',
    'N100': 'Europe (Euronext)',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'NSEI': 'India',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}
res['country'] = res['Index'].map(index_to_country)

out = res.head(5)[['Index','country','overall_return_pct','return_multiple']]
out['overall_return_pct'] = out['overall_return_pct'].round(2)
out['return_multiple'] = out['return_multiple'].round(4)

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_1REGSUHyxGGaKaXFYTnMX03V': 'file_storage/call_1REGSUHyxGGaKaXFYTnMX03V.json', 'var_call_ulmDo1EQzIr3bc31K9lb8eoE': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_i9g12FdxiXPCMzJqKokbNdmy': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
