code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_2vlcBRplFZpAmEvheCXccS8c)
# map index symbol to country (and exchange) using domain knowledge + provided hint examples
mapping = {
  '399001.SZ': {'country':'China', 'exchange':'Shenzhen Stock Exchange'},
  '000001.SS': {'country':'China', 'exchange':'Shanghai Stock Exchange'},
  'IXIC': {'country':'United States', 'exchange':'NASDAQ'},
  'NYA': {'country':'United States', 'exchange':'New York Stock Exchange'},
  'NSEI': {'country':'India', 'exchange':'National Stock Exchange of India'},
}
meta = top5['Index'].map(mapping)
meta_df = pd.json_normalize(meta)
res = pd.concat([top5, meta_df], axis=1)
res['total_return_since_2000'] = res['total_return_since_2000'].astype(float)
res['overall_return_pct'] = (res['total_return_since_2000']*100).round(1)
res = res.drop(columns=['total_return_since_2000'])
# order already top
out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KkZxaK2Lehgkn4CuuIOpvCoV': ['index_info'], 'var_call_eRKZ8JDgcDeVUNslqLcg3BZ2': ['index_trade'], 'var_call_M2RxHQyFOrNy3qRQsRIxWyMK': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_xOeJD2qLaQOrgYeEIETbPaVe': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_2vlcBRplFZpAmEvheCXccS8c': [{'Index': '399001.SZ', 'total_return_since_2000': '2.7592027372691184'}, {'Index': 'IXIC', 'total_return_since_2000': '2.4892179344618204'}, {'Index': 'NSEI', 'total_return_since_2000': '2.103308772715655'}, {'Index': 'NYA', 'total_return_since_2000': '1.5183504055050108'}, {'Index': '000001.SS', 'total_return_since_2000': '1.3553662336011327'}]}

exec(code, env_args)
