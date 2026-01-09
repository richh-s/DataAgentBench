code = """import json, pandas as pd
path = var_call_I60HY7iEWg5C8iUAkTJuHhmz
with open(path,'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['CloseUSD','Date'])

sdf = df.sort_values(['Index','Date']).copy()
final_price = sdf.groupby('Index')['CloseUSD'].last()

sdf['Month'] = sdf['Date'].dt.to_period('M')
first_month = sdf.groupby(['Index','Month'], as_index=False).first()[['Index','Month','CloseUSD']]
first_month['FinalPrice'] = first_month['Index'].map(final_price)
first_month = first_month.dropna(subset=['FinalPrice'])
first_month['UnitsFinalValue'] = first_month['FinalPrice'] / first_month['CloseUSD']

agg = first_month.groupby('Index').agg(months=('Month','nunique'), final_value=('UnitsFinalValue','sum')).reset_index()
agg['invested_amount'] = agg['months']
agg['multiple'] = agg['final_value']/agg['invested_amount']
agg = agg.sort_values('multiple', ascending=False)

top5 = agg.head(5).copy()
country_map = {
    '^GSPC':'United States','^IXIC':'United States','^DJI':'United States',
    'N225':'Japan','HSI':'Hong Kong','000001.SS':'China','399001.SZ':'China',
    '^FTSE':'United Kingdom','^FCHI':'France','^GDAXI':'Germany','^NSEI':'India',
    '^KS11':'South Korea','^TWII':'Taiwan','^SSMI':'Switzerland','^GSPTSE':'Canada',
    '^JSETOP40':'South Africa'
}
top5['country'] = top5['Index'].map(country_map).fillna('Unknown')
top5['overall_return_pct'] = (top5['multiple']-1.0)*100.0
out = top5[['Index','country','months','multiple','overall_return_pct']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_I60HY7iEWg5C8iUAkTJuHhmz': 'file_storage/call_I60HY7iEWg5C8iUAkTJuHhmz.json', 'var_call_RfXZ44Ml6S46DzPqRZJj9z4w': ['index_info'], 'var_call_w68rsQ8bbkkg0yQouK3SHSbw': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
