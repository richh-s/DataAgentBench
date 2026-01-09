code = """import json, pandas as pd

path = var_call_zftAiDpMqvyCLxtxTBcFmAHz
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
# parse month
df['month'] = pd.to_datetime(df['month'])
df['month'] = df['month'].dt.to_period('M').dt.to_timestamp()
# ensure numeric
df['month_end_close_usd'] = pd.to_numeric(df['month_end_close_usd'], errors='coerce')

# Build full month range from 2000-01 to max month across all indices
overall_max = df['month'].max()
months = pd.date_range('2000-01-01', overall_max, freq='MS')

results = []
for idx, g in df.groupby('Index'):
    g = g.sort_values('month')
    # align to full months and forward fill prices
    s = g.set_index('month')['month_end_close_usd'].reindex(months).ffill()
    # start at first non-null month (must have price)
    first_valid = s.first_valid_index()
    if first_valid is None:
        continue
    s = s.loc[first_valid:]
    # compute DCA: invest 1 unit each month at month-end price
    prices = s.values
    # drop any leading/trailing nan
    import numpy as np
    mask = ~pd.isna(prices)
    prices = prices[mask]
    if len(prices) < 12:
        continue
    shares = (1.0 / prices).sum()
    total_invested = float(len(prices))
    final_price = float(prices[-1])
    final_value = shares * final_price
    multiple = final_value / total_invested
    results.append({'Index': idx, 'start_month': str(pd.to_datetime(s.index[0]).date()), 'end_month': str(pd.to_datetime(s.index[mask].max()).date()), 'months': int(len(prices)), 'final_value_per_1_monthly': float(final_value), 'invested': total_invested, 'return_multiple': float(multiple)})

res_df = pd.DataFrame(results).sort_values('return_multiple', ascending=False)
top5 = res_df.head(5).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps({'top5': top5}, ensure_ascii=False))"""

env_args = {'var_call_0DZG2j9dPhmxscRPInlUtT6f': ['index_info'], 'var_call_jSJUx0zU6dMXUE6JeTPWQV2T': ['index_trade'], 'var_call_P50EATEDlOvBUR3rN7S02Pp0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_B5bea3BxTopzr7ZVcBPiEbyP': [{'Index': 'NYA', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '13947'}, {'Index': 'N225', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '13874'}, {'Index': 'IXIC', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '10526'}, {'Index': 'HSI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '8492'}, {'Index': 'GDAXI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '8438'}, {'Index': 'SSMI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '7671'}, {'Index': 'TWII', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5869'}, {'Index': '000001.SS', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5791'}, {'Index': '399001.SZ', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5760'}, {'Index': 'N100', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5474'}, {'Index': 'NSEI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '3346'}, {'Index': 'J203.JO', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '2346'}], 'var_call_u7r4lGgY4KXBKDARPT7oUAmY': [{'Date': '05 Feb 1971, 00:00'}, {'Date': '08 Feb 1971, 00:00'}, {'Date': '1971-02-09 00:00:00'}, {'Date': '1971-02-10 00:00:00'}, {'Date': '11 Feb 1971, 00:00'}], 'var_call_zftAiDpMqvyCLxtxTBcFmAHz': 'file_storage/call_zftAiDpMqvyCLxtxTBcFmAHz.json'}

exec(code, env_args)
