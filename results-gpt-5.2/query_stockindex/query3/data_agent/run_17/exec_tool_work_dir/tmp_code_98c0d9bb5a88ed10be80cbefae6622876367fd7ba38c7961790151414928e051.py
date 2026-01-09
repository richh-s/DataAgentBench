code = """import json, pandas as pd
trade_top5 = pd.DataFrame(var_call_SMZdOVXT3HLzzXzdOQLuyQQt)
info = pd.DataFrame(var_call_xW9LNqU9frSzm4NpRZGjnHoz)

# Map index symbols to exchanges (and countries inferred)
map_rows = [
    {'Index':'IXIC','Exchange':'NASDAQ','Country':'United States'},
    {'Index':'NYA','Exchange':'New York Stock Exchange','Country':'United States'},
    {'Index':'000001.SS','Exchange':'Shanghai Stock Exchange','Country':'China'},
    {'Index':'399001.SZ','Exchange':'Shenzhen Stock Exchange','Country':'China'},
    {'Index':'NSEI','Exchange':'National Stock Exchange of India','Country':'India'},
]
map_df = pd.DataFrame(map_rows)

out = trade_top5.merge(map_df, on='Index', how='left')
out['growth_multiple'] = out['growth_multiple'].astype(float)
out = out.sort_values('growth_multiple', ascending=False)

result = out[['Index','Exchange','Country','growth_multiple','start_month','end_month']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dmF62sWFKbfLMtvdvCxlGMWh': ['index_trade'], 'var_call_1mHmOmFLmqJwF2qIdSI4yQRn': ['index_info'], 'var_call_qT2DGeKA4fIqjUE7f2QbMaiu': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_HhSxx9tmCWWnPaCIE5Ekz1j4': [{'total': '104224', 'null_dt': '0.0'}], 'var_call_SMZdOVXT3HLzzXzdOQLuyQQt': [{'Index': '399001.SZ', 'start_month': '2000-01-01 00:00:00', 'end_month': '2021-06-01 00:00:00', 'start_close': '632.38558592', 'end_close': '2377.2656256', 'n_months': '258', 'growth_multiple': '3.7592027372691192'}, {'Index': 'IXIC', 'start_month': '2000-01-01 00:00:00', 'end_month': '2021-05-01 00:00:00', 'start_close': '3940.350098', 'end_close': '13748.74023', 'n_months': '257', 'growth_multiple': '3.4892179344618226'}, {'Index': 'NSEI', 'start_month': '2007-09-01 00:00:00', 'end_month': '2021-05-01 00:00:00', 'start_close': '50.21350098', 'end_close': '155.8279981', 'n_months': '165', 'growth_multiple': '3.1033087727156525'}, {'Index': 'NYA', 'start_month': '2000-01-01 00:00:00', 'end_month': '2021-05-01 00:00:00', 'start_close': '6574.009766', 'end_close': '16555.66016', 'n_months': '257', 'growth_multiple': '2.5183504055050103'}, {'Index': '000001.SS', 'start_month': '2000-01-01 00:00:00', 'end_month': '2021-05-01 00:00:00', 'start_close': '245.59951168', 'end_close': '578.4767968', 'n_months': '257', 'growth_multiple': '2.3553662336011367'}], 'var_call_xW9LNqU9frSzm4NpRZGjnHoz': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
