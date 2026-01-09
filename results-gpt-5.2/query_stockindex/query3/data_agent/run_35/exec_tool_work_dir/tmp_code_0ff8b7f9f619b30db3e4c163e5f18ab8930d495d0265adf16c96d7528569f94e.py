code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_HzrCtmrWwxRAejmxutozgnng)

# map index symbol to exchange name and country (inferred)
map_info = {
    'IXIC': {'Exchange':'NASDAQ','Country':'United States'},
    'GDAXI': {'Exchange':'Frankfurt Stock Exchange','Country':'Germany'},
    'NSEI': {'Exchange':'National Stock Exchange of India','Country':'India'},
    '399001.SZ': {'Exchange':'Shenzhen Stock Exchange','Country':'China'},
    'TWII': {'Exchange':'Taiwan Stock Exchange','Country':'Taiwan'},
}

def enrich(row):
    d = map_info.get(row['Index'], {})
    return pd.Series({'Exchange': d.get('Exchange'), 'Country': d.get('Country')})

enriched = top5.join(top5.apply(enrich, axis=1))

# format return multiple and percent
enriched['ReturnMultiple'] = enriched['ReturnMultiple'].astype(float)
enriched['OverallReturnPct'] = (enriched['ReturnMultiple'] - 1.0) * 100.0

out = enriched[['Index','Country','ReturnMultiple','OverallReturnPct']].copy()
out['ReturnMultiple'] = out['ReturnMultiple'].map(lambda x: round(x,4))
out['OverallReturnPct'] = out['OverallReturnPct'].map(lambda x: round(x,2))

print('__RESULT__:')
print(out.to_json(orient='records'))"""

env_args = {'var_call_1oDxJjpBDh0FKEVZMMEQl2Mo': ['index_info'], 'var_call_0TRAH6EA7OhvVx9PgRtUmyHO': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_PYWVyhefplIODCHHDPhUaLuv': 'file_storage/call_PYWVyhefplIODCHHDPhUaLuv.json', 'var_call_nBk5CM0aVrJwGLqG7dFRFsi3': {'parsed_ok': 50, 'examples': [{'raw': '31 Dec 1986, 00:00', 'parsed': '1986-12-31'}, {'raw': 'January 02, 1987 at 12:00 AM', 'parsed': '1987-01-02'}, {'raw': '1987-01-05 00:00:00', 'parsed': '1987-01-05'}, {'raw': '06 Jan 1987, 00:00', 'parsed': '1987-01-06'}, {'raw': '07 Jan 1987, 00:00', 'parsed': '1987-01-07'}, {'raw': '1987-01-08 00:00:00', 'parsed': '1987-01-08'}, {'raw': '1987-01-09 00:00:00', 'parsed': '1987-01-09'}, {'raw': '1987-01-12 00:00:00', 'parsed': '1987-01-12'}, {'raw': '1987-01-13 00:00:00', 'parsed': '1987-01-13'}, {'raw': '1987-01-14 00:00:00', 'parsed': '1987-01-14'}]}, 'var_call_NCn27vrRETPgRTdWTyTds7w8': 'file_storage/call_NCn27vrRETPgRTdWTyTds7w8.json', 'var_call_HzrCtmrWwxRAejmxutozgnng': [{'Index': 'IXIC', 'MonthsAvailable': 257, 'Invested': 257.0, 'FinalValue': 1239.7232112185, 'ReturnMultiple': 4.8238257246}, {'Index': 'GDAXI', 'MonthsAvailable': 257, 'Invested': 257.0, 'FinalValue': 603.7662524903, 'ReturnMultiple': 2.3492850291}, {'Index': 'NSEI', 'MonthsAvailable': 165, 'Invested': 165.0, 'FinalValue': 387.5282698291, 'ReturnMultiple': 2.3486561808}, {'Index': '399001.SZ', 'MonthsAvailable': 258, 'Invested': 258.0, 'FinalValue': 603.8282159947, 'ReturnMultiple': 2.3404194418}, {'Index': 'TWII', 'MonthsAvailable': 257, 'Invested': 257.0, 'FinalValue': 590.188085898, 'ReturnMultiple': 2.2964516961}], 'var_call_Klc2iA9WKpAftJjSOHAPKqC7': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
