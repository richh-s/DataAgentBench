code = """import json, pandas as pd

top = pd.DataFrame(var_call_egi1qmlvdL71jTDGQ7vRjY22)
# map index symbol to exchange/country
map_idx = {
  'IXIC': ('NASDAQ', 'United States'),
  'GSPTSE': ('Toronto Stock Exchange', 'Canada'),
  '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
  '000001.SS': ('Shanghai Stock Exchange', 'China'),
  'N225': ('Tokyo Stock Exchange', 'Japan'),
  'HSI': ('Hong Kong Stock Exchange', 'Hong Kong'),
  'NSEI': ('National Stock Exchange of India', 'India'),
  'GDAXI': ('Frankfurt Stock Exchange', 'Germany'),
  'SSMI': ('SIX Swiss Exchange', 'Switzerland'),
  '^KS11': ('Korea Exchange', 'South Korea'),
  'TWII': ('Taiwan Stock Exchange', 'Taiwan'),
  'J203.JO': ('Johannesburg Stock Exchange', 'South Africa'),
  '^GSPC': ('New York Stock Exchange', 'United States'),
  'NYA': ('New York Stock Exchange', 'United States'),
  'N100': ('Euronext', 'Europe')
}

def enrich(row):
    ex,country = map_idx.get(row['Index'], (None,None))
    return pd.Series({'Exchange': ex, 'Country': country})

enr = top.join(top.apply(enrich, axis=1))
# format return as percent
enr['total_return'] = enr['total_return'].astype(float)
enr['TotalReturnPct'] = (enr['total_return']*100).round(2)
result = enr[['Index','Exchange','Country','TotalReturnPct','n_months']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EFblubmBsc09DZuTkT8XshAY': ['index_trade'], 'var_call_Ow0RtqlL9R2BXH1JyT8wS6IO': ['index_info'], 'var_call_xQlmYiKr2iWuPbOl3DNXnmGI': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_call_FsQ3crj9dpHRSKPJVChWRMzd': [{'min_iso': 'NaT', 'max_iso': 'NaT'}], 'var_call_egi1qmlvdL71jTDGQ7vRjY22': [{'Index': 'NSEI', 'n_months': '165', 'total_return': '1.4322190645996713'}, {'Index': 'IXIC', 'n_months': '257', 'total_return': '1.140840683168177'}, {'Index': '399001.SZ', 'n_months': '258', 'total_return': '0.8789456697406237'}, {'Index': 'GSPTSE', 'n_months': '257', 'total_return': '0.740377833999468'}, {'Index': 'J203.JO', 'n_months': '112', 'total_return': '0.6735227770198748'}], 'var_call_9dQfvde6EEpJhGNVgGCBUu2j': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
