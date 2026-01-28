code = """import pandas as pd
import json
# load data from the earlier query result file
path = var_call_hykG1MPEl5U6WmuU8zBSmvqS
# read json records
df = pd.read_json(path)
# normalize types
df['Date'] = pd.to_datetime(df['Date'])
# CloseUSD may be string; convert
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# consider only rows with valid price
df = df.dropna(subset=['CloseUSD'])
# create year-month
df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
# sort and get first trading day price per month per index
df_sorted = df.sort_values(['Index','Date'])
monthly = df_sorted.groupby(['Index','YearMonth'], as_index=False).first()[['Index','YearMonth','CloseUSD','Date']]
# prepare results
results = []
# mapping of index to country (inferred)
country_map = {
    "J203.JO": "South Africa",
    "N225": "Japan",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "HSI": "Hong Kong",
    "NYA": "United States",
    "IXIC": "United States",
    "000001.SS": "China",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Netherlands",
    "399001.SZ": "China"
}

for idx, group in monthly.groupby('Index'):
    prices = group['CloseUSD'].values
    months = len(prices)
    if months == 0:
        continue
    # buy $1 each month at that month's first trading day's CloseUSD
    shares_bought = (1.0 / prices).sum()
    # final price = last available CloseUSD in full df for this index
    final_price = float(df[df['Index'] == idx].sort_values('Date', ascending=False).iloc[0]['CloseUSD'])
    final_value = shares_bought * final_price
    invested = float(months)
    return_factor = final_value / invested if invested > 0 else None
    results.append({
        'Index': idx,
        'MonthsInvested': months,
        'TotalInvestedUSD': round(invested, 2),
        'FinalValueUSD': round(final_value, 6),
        'ReturnFactor': round(return_factor, 6),
        'ReturnPct': round((return_factor - 1) * 100, 2) if return_factor is not None else None,
        'Country': country_map.get(idx, 'Unknown')
    })

# sort by ReturnFactor descending
results_sorted = sorted(results, key=lambda x: x['ReturnFactor'], reverse=True)
# top 5
top5 = results_sorted[:5]
# prepare output
out = top5
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_7bYFnCocCYIvgjgcqEXjK46F': ['index_trade'], 'var_call_4fKMupXXKsyPlmxzpm87FDQz': ['index_info'], 'var_call_NQUQME3s7gFZg3gEhHYbiuJl': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_hykG1MPEl5U6WmuU8zBSmvqS': 'file_storage/call_hykG1MPEl5U6WmuU8zBSmvqS.json', 'var_call_cab90LRnfe2nwPkYBMh2GYi1': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}]}

exec(code, env_args)
