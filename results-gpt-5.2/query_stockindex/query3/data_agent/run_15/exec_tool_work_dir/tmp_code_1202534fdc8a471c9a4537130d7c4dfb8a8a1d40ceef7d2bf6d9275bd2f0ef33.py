code = """import json, pandas as pd

top = pd.DataFrame(var_call_1Fuyd4ijLBrJBeuECujicaRw)
# map index symbols to exchange + country (inferred)
map_info = {
  'GSPTSE': ('Toronto Stock Exchange', 'Canada'),
  'NSEI': ('National Stock Exchange of India', 'India'),
  'IXIC': ('NASDAQ', 'United States'),
  'J203.JO': ('Johannesburg Stock Exchange', 'South Africa'),
  'NYA': ('New York Stock Exchange', 'United States'),
}
rows = []
for _, r in top.iterrows():
    idx = r['Index']
    exch, country = map_info.get(idx, (None, None))
    rows.append({
        'Index': idx,
        'TotalReturn': float(r['total_return']),
        'Exchange': exch,
        'Country': country
    })

out = json.dumps(rows)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_tFP7RIpHozUOFy0MDow4Bhrs': ['index_info'], 'var_call_HLATGjaBPGScc0iVd9bGva1R': ['index_trade'], 'var_call_1Fuyd4ijLBrJBeuECujicaRw': [{'Index': 'GSPTSE', 'total_return': '1.222337744738153'}, {'Index': 'NSEI', 'total_return': '0.9875420170463807'}, {'Index': 'IXIC', 'total_return': '0.8368124097485039'}, {'Index': 'J203.JO', 'total_return': '0.6522797964925076'}, {'Index': 'NYA', 'total_return': '0.10286209914837685'}], 'var_call_mz5sWSR69blYmXjQFVuukeJk': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
