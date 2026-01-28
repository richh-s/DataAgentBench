code = """import pandas as pd
import json
from datetime import datetime

# Load the large query result from the storage-provided filepath
data_path = var_call_RM4MfejXF3UiUQAmBnUKtN2K
with open(data_path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Clean and parse dates
# Remove common trailing text
df['Date_clean'] = df['Date'].astype(str).str.replace(' at 12:00 AM', '', regex=False)
# Some dates use commas before time like '31 Dec 1986, 00:00' - remove trailing time fragments
# Remove patterns like ', 00:00' or ', 00:00'
import re
df['Date_clean'] = df['Date_clean'].str.replace(r',\s*\d{2}:\d{2}(:\d{2})?','', regex=True)
# Parse
df['Date_parsed'] = pd.to_datetime(df['Date_clean'], errors='coerce', infer_datetime_format=True)
# Convert CloseUSD to float
# Some CloseUSD values may be strings; coerce errors
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Filter from 2000-01-01
df = df[df['Date_parsed'] >= pd.Timestamp('2000-01-01')].copy()

# Ensure we have data
if df.empty:
    result = {"error": "No data >= 2000-01-01"}
    print("__RESULT__:")
    print(json.dumps(result))
else:
    # For each index, perform monthly DCA: invest $1 on the first available trading day of each month
    results = []
    for idx, group in df.groupby('Index'):
        g = group.sort_values('Date_parsed').copy()
        if g['CloseUSD'].isna().all():
            continue
        # Create Year-Month column
        g['ym'] = g['Date_parsed'].dt.to_period('M')
        # For each ym, pick first date (earliest) and its price
        first_by_month = g.groupby('ym').first().reset_index()
        # count months invested
        months = len(first_by_month)
        if months == 0:
            continue
        # Units bought per month with $1
        first_by_month['units'] = 1.0 / first_by_month['CloseUSD']
        total_units = first_by_month['units'].sum()
        total_invested = months * 1.0
        # last available close price for index
        last_price = g.sort_values('Date_parsed', ascending=True).iloc[-1]['CloseUSD']
        final_value = total_units * last_price
        return_multiple = final_value / total_invested if total_invested>0 else None
        results.append({
            'Index': idx,
            'months_invested': months,
            'total_invested_usd': round(total_invested,2),
            'final_value_usd': round(float(final_value),2),
            'return_multiple': round(float(return_multiple),4)
        })
    res_df = pd.DataFrame(results)
    # Rank by return_multiple descending
    res_df = res_df.sort_values('return_multiple', ascending=False)
    # Keep top 10 to inspect
    top5 = res_df.head(5).to_dict(orient='records')

    # Map indices to countries (inferred)
    mapping = {
        'J203.JO': 'South Africa',
        'N225': 'Japan',
        'GSPTSE': 'Canada',
        'NSEI': 'India',
        'GDAXI': 'Germany',
        'IXIC': 'United States',
        'HSI': 'Hong Kong',
        'NYA': 'United States',
        'N100': 'Euronext (Pan-European)',
        '399001.SZ': 'China (Shenzhen)',
        '000001.SS': 'China (Shanghai)',
        'SSMI': 'Switzerland',
        'TWII': 'Taiwan'
    }
    for r in top5:
        r['country'] = mapping.get(r['Index'], 'Unknown')

    result = { 'top5': top5 }
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_call_df1INp74AVRygBP16D6szr2G': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_FQqlvaCwckEuIgM2Xb8FYaHq': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_RM4MfejXF3UiUQAmBnUKtN2K': 'file_storage/call_RM4MfejXF3UiUQAmBnUKtN2K.json'}

exec(code, env_args)
