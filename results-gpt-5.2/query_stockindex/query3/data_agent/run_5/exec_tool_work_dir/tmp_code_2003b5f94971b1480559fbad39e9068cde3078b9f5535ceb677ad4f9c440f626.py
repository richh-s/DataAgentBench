code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_qq0vMzuXeh0twqzvpVDAZOhv)
info = pd.DataFrame(var_call_cFOe4LxCtDJ0Ryd4znDp5ieG)

symbol_map = {
  'IXIC': ('NASDAQ', 'United States'),
  'NYA': ('New York Stock Exchange', 'United States'),
  '000001.SS': ('Shanghai Stock Exchange', 'China'),
  '399001.SZ': ('Shenzhen Stock Exchange', 'China'),
  'NSEI': ('National Stock Exchange of India', 'India'),
}

rows = []
for _, r in top5.iterrows():
    idx = r['Index']
    exch, country = symbol_map.get(idx, (None, None))
    currency = None
    if exch is not None:
        m = info.loc[info['Exchange'] == exch, 'Currency']
        currency = m.iloc[0] if len(m) else None
    rows.append({
        'Index': idx,
        'Country': country,
        'Exchange': exch,
        'Currency': currency,
        'DCA_growth_multiple_since_2000': float(r['dca_growth'])
    })

out = json.dumps(rows)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_E2LtzW7fXuTqv683PJ04imdc': ['index_info'], 'var_call_N8TsKdxR7yfRSHgIuzgOsFIc': ['index_trade'], 'var_call_KQF2mbMDbaF2dMgV14pUUGvd': [], 'var_call_LcUxLtNKkaG8SUuOtZMvU2im': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_qq0vMzuXeh0twqzvpVDAZOhv': [{'Index': '399001.SZ', 'dca_growth': '3.7592027372691184'}, {'Index': 'IXIC', 'dca_growth': '3.4892179344618204'}, {'Index': 'NSEI', 'dca_growth': '3.1033087727156556'}, {'Index': 'NYA', 'dca_growth': '2.5183504055050108'}, {'Index': '000001.SS', 'dca_growth': '2.355366233601133'}], 'var_call_cFOe4LxCtDJ0Ryd4znDp5ieG': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
