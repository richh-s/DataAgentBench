code = """import json, pandas as pd
from datetime import datetime

# load trade data
path = var_call_lZlRbskbKMvFjEA7vJaatpbx
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# monthly close (last trading day of month)
df['Month'] = df['Date'].dt.to_period('M').dt.to_timestamp('M')
df = df.sort_values(['Index','Date'])
monthly = df.groupby(['Index','Month'], as_index=False).tail(1)
monthly = monthly.sort_values(['Index','Month'])

# compute DCA growth with $1 each month invested at that month's close
# shares accumulated = sum(1/price). final value = shares * last_price
# total invested = number of months
agg = monthly.groupby('Index').agg(
    months=('CloseUSD','size'),
    shares=('CloseUSD', lambda s: float((1.0/s).sum())),
    last_price=('CloseUSD','last'),
    first_month=('Month','min'),
    last_month=('Month','max')
).reset_index()
agg['total_invested'] = agg['months'] * 1.0
agg['final_value'] = agg['shares'] * agg['last_price']
agg['multiple'] = agg['final_value'] / agg['total_invested']
agg = agg[agg['months']>0].sort_values('multiple', ascending=False)

top5 = agg.head(5).copy()

# map Index to country (inferred)
country_map = {
    'GSPC':'United States',
    '^GSPC':'United States',
    'DJI':'United States',
    '^DJI':'United States',
    'IXIC':'United States',
    '^IXIC':'United States',
    'NDX':'United States',
    '^NDX':'United States',
    'RUT':'United States',
    '^RUT':'United States',
    'FTSE':'United Kingdom',
    '^FTSE':'United Kingdom',
    'GDAXI':'Germany',
    '^GDAXI':'Germany',
    'FCHI':'France',
    '^FCHI':'France',
    'STOXX50E':'Eurozone',
    '^STOXX50E':'Eurozone',
    'N225':'Japan',
    '^N225':'Japan',
    'HSI':'Hong Kong',
    '^HSI':'Hong Kong',
    '000001.SS':'China',
    '399001.SZ':'China',
    'KS11':'South Korea',
    '^KS11':'South Korea',
    'BSESN':'India',
    '^BSESN':'India',
    'NSEI':'India',
    '^NSEI':'India',
    'BVSP':'Brazil',
    '^BVSP':'Brazil',
    'MXX':'Mexico',
    '^MXX':'Mexico',
    'GSPTSE':'Canada',
    '^GSPTSE':'Canada',
    'AORD':'Australia',
    '^AORD':'Australia',
    'AXJO':'Australia',
    '^AXJO':'Australia',
    'SSMI':'Switzerland',
    '^SSMI':'Switzerland',
    'IBEX':'Spain',
    '^IBEX':'Spain',
    'MIB':'Italy',
    '^FTMIB':'Italy',
    'FTMIB':'Italy',
    'TA35.TA':'Israel',
    '^TA125.TA':'Israel',
    'IMOEX.ME':'Russia',
    '^IMOEX.ME':'Russia',
    'J203.JO':'South Africa'
}

top5['country'] = top5['Index'].map(country_map).fillna('Unknown')

out = top5[['Index','country','multiple','months','first_month','last_month']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_ryiXunWus6mqQh1ibHkPJRe9': ['index_info'], 'var_call_qS2g06b5g97CAOMhjZ7rFZaD': ['index_trade'], 'var_call_lZlRbskbKMvFjEA7vJaatpbx': 'file_storage/call_lZlRbskbKMvFjEA7vJaatpbx.json'}

exec(code, env_args)
