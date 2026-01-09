code = """import json, pandas as pd

# Load trade data (may be a filepath)
trade_src = var_call_5IMktDah33pEtPM9sdniGwm4
if isinstance(trade_src, str):
    with open(trade_src, 'r') as f:
        trade = json.load(f)
else:
    trade = trade_src

df = pd.DataFrame(trade)
# Parse types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Monthly investment: invest 1 unit of USD at first available trading day each month per index
# Shares purchased = 1 / CloseUSD_at_invest_date
# Final value = total_shares * last CloseUSD
# Total invested = number_of_months_with_data

# Determine month period
df['Month'] = df['Date'].dt.to_period('M')

# first trading day per month per index
firsts = (df.sort_values(['Index','Date'])
            .groupby(['Index','Month'], as_index=False)
            .first()[['Index','Month','Date','CloseUSD']])
firsts['shares'] = 1.0 / firsts['CloseUSD']

shares_sum = firsts.groupby('Index', as_index=False).agg(months=('Month','nunique'), total_shares=('shares','sum'))

last_price = (df.sort_values(['Index','Date'])
                .groupby('Index', as_index=False)
                .last()[['Index','CloseUSD']]
                .rename(columns={'CloseUSD':'last_CloseUSD'}))

res = shares_sum.merge(last_price, on='Index', how='inner')
res['total_invested_usd'] = res['months'].astype(float)
res['final_value_usd'] = res['total_shares'] * res['last_CloseUSD']
res['multiple'] = res['final_value_usd'] / res['total_invested_usd']
res = res.sort_values('multiple', ascending=False)

top5 = res.head(5).copy()

# Map index symbol -> country (best-effort, inferred from common major indices)
country_map = {
    '^IXIC':'United States', '^GSPC':'United States', '^DJI':'United States',
    'N225':'Japan',
    'HSI':'Hong Kong',
    '000001.SS':'China', '399001.SZ':'China',
    '^FTSE':'United Kingdom',
    '^GDAXI':'Germany',
    '^FCHI':'France',
    '^NSEI':'India',
    '^STI':'Singapore',
    '^KS11':'South Korea',
    '^TWII':'Taiwan',
    '^BVSP':'Brazil',
    '^MXX':'Mexico',
    '^AORD':'Australia', '^AXJO':'Australia',
    '^GSPTSE':'Canada',
    '^SSMI':'Switzerland',
    '^STOXX50E':'Eurozone',
    '^BFX':'Belgium',
    '^ATX':'Austria',
    '^OMXS30':'Sweden',
    '^OSEAX':'Norway',
    '^NZ50':'New Zealand',
}
top5['country'] = top5['Index'].map(country_map).fillna('Unknown')

out = top5[['Index','country','months','total_invested_usd','final_value_usd','multiple']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, default=str))"""

env_args = {'var_call_9FQratsz5fiBvcjfD6Cotnke': ['index_info'], 'var_call_jPgJrsQnZeAE6Bp8dl43bHpP': ['index_trade'], 'var_call_5IMktDah33pEtPM9sdniGwm4': 'file_storage/call_5IMktDah33pEtPM9sdniGwm4.json'}

exec(code, env_args)
