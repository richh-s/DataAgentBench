code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_44MllmX44liLvNcLgyUXQY2y)

# Map index symbols to exchanges (per dataset/hint knowledge)
idx_to_exchange = {
  'IXIC': 'NASDAQ',
  'NYA': 'New York Stock Exchange',
  '000001.SS': 'Shanghai Stock Exchange',
  '399001.SZ': 'Shenzhen Stock Exchange',
  'NSEI': 'National Stock Exchange of India'
}
exchange_to_country = {
  'NASDAQ': 'United States',
  'New York Stock Exchange': 'United States',
  'Shanghai Stock Exchange': 'China',
  'Shenzhen Stock Exchange': 'China',
  'National Stock Exchange of India': 'India'
}

rows = []
for _, r in top5.iterrows():
    idx = r['Index']
    mult = float(r['total_return_multiple'])
    exch = idx_to_exchange.get(idx)
    country = exchange_to_country.get(exch)
    rows.append({
        'Index': idx,
        'Total return multiple (monthly DCA since 2000)': mult,
        'Exchange': exch,
        'Country': country
    })

out = json.dumps(rows)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_J05TlPQ2XU70sEuxMdvKMKVR': ['index_trade'], 'var_call_eGU9HEHnts89f8PQeS8GcLMn': ['index_info'], 'var_call_QoRg2O2dJwyawdYnpXVFEpdq': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_SNTtR7E8AbE1JBRFEIOKi14j': [{'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}], 'var_call_edi4ePVZGxaWdIbZE9JCmqMq': [{'Index': 'HSI', 'd1': '1986-12-31 00:00:00', 'd2': 'NaT', 'd3': 'NaT'}, {'Index': 'HSI', 'd1': 'NaT', 'd2': '1987-01-02 00:00:00', 'd3': 'NaT'}, {'Index': 'HSI', 'd1': 'NaT', 'd2': 'NaT', 'd3': '1987-01-05 00:00:00'}, {'Index': 'HSI', 'd1': '1987-01-06 00:00:00', 'd2': 'NaT', 'd3': 'NaT'}, {'Index': 'HSI', 'd1': '1987-01-07 00:00:00', 'd2': 'NaT', 'd3': 'NaT'}], 'var_call_44MllmX44liLvNcLgyUXQY2y': [{'Index': '399001.SZ', 'n_months': '257', 'total_return_multiple': '3.7592027372691192'}, {'Index': 'IXIC', 'n_months': '256', 'total_return_multiple': '3.4892179344618204'}, {'Index': 'NSEI', 'n_months': '164', 'total_return_multiple': '3.103308772715655'}, {'Index': 'NYA', 'n_months': '256', 'total_return_multiple': '2.5183504055050108'}, {'Index': '000001.SS', 'n_months': '256', 'total_return_multiple': '2.3553662336011327'}], 'var_call_H5H4bWCcFgxru89av6dGnoUi': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
