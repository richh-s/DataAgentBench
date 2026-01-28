code = """import json
import pandas as pd

df = pd.DataFrame(var_call_FrSvI6cJas4xVBZfYItF2VIB)
# map index symbol to country (major index)
country_map = {
    'IXIC': 'United States',
    'GDAXI': 'Germany',
    'NSEI': 'India',
    '399001.SZ': 'China',
    'TWII': 'Taiwan'
}

df['Country'] = df['Index'].map(country_map)
# format multiples
out = df[['Index','Country','multiple']].copy()
out['multiple'] = out['multiple'].astype(float)
out = out.sort_values('multiple', ascending=False)
records = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_kVLZoZ3k8ZzFOOkNXDQZvFga': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_eoxaYpmbAZGg5ARYQ38uoph2': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_Mn0lXTb5V82GzBwWQh5ujRP2': [{'n': '104224', 'iso': '0', 'dmy_abbr': '34957', 'long_fmt': '34562', 'iso_ts': '34705'}], 'var_call_FrSvI6cJas4xVBZfYItF2VIB': [{'Index': 'IXIC', 'months': '257', 'first_month': '2000-01-01 00:00:00', 'last_month': '2021-05-01 00:00:00', 'total_shares': '0.09016994942659282', 'last_price': '13748.74023', 'final_value': '1239.723211218462', 'total_invested': '257.0', 'multiple': '4.823825724585455'}, {'Index': 'GDAXI', 'months': '257', 'first_month': '2000-01-01 00:00:00', 'last_month': '2021-05-01 00:00:00', 'total_shares': '0.032091706298093166', 'last_price': '18813.7784536', 'final_value': '603.7662524903246', 'total_invested': '257.0', 'multiple': '2.349285029145232'}, {'Index': 'NSEI', 'months': '165', 'first_month': '2007-09-01 00:00:00', 'last_month': '2021-05-01 00:00:00', 'total_shares': '2.486897570103978', 'last_price': '155.8279981', 'final_value': '387.5282698290573', 'total_invested': '165.0', 'multiple': '2.3486561807821653'}, {'Index': '399001.SZ', 'months': '258', 'first_month': '2000-01-01 00:00:00', 'last_month': '2021-06-01 00:00:00', 'total_shares': '0.2540011555680717', 'last_price': '2377.2656256', 'final_value': '603.8282159946549', 'total_invested': '258.0', 'multiple': '2.3404194418397477'}, {'Index': 'TWII', 'months': '257', 'first_month': '2000-01-01 00:00:00', 'last_month': '2021-05-01 00:00:00', 'total_shares': '0.8644440300265751', 'last_price': '682.7371876000001', 'final_value': '590.1880858979539', 'total_invested': '257.0', 'multiple': '2.2964516961009878'}]}

exec(code, env_args)
