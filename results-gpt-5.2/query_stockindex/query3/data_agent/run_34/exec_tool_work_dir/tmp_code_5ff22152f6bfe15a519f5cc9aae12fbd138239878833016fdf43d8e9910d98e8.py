code = """import json, pandas as pd

top5 = pd.DataFrame(var_call_coFBUQp1finfavd7WrvUEMxQ)

# Map index symbols to countries using domain knowledge
country_map = {
    'IXIC': ('United States','NASDAQ'),
    '399001.SZ': ('China','Shenzhen Stock Exchange'),
    'GDAXI': ('Germany','Frankfurt Stock Exchange'),
    'NSEI': ('India','National Stock Exchange of India'),
    'TWII': ('Taiwan','Taiwan Stock Exchange'),
}

rows = []
for _, r in top5.iterrows():
    idx = r['Index']
    country, exchange = country_map.get(idx, (None, None))
    rows.append({
        'Index': idx,
        'Country': country,
        'Exchange': exchange,
        'Return_multiple': float(r['return_multiple'])
    })

out = pd.DataFrame(rows)
print('__RESULT__:')
print(out.to_json(orient='records'))"""

env_args = {'var_call_I3GA65myriws3fN22g6de269': ['index_info'], 'var_call_vsEUnteGtULYALcrd1eL5dL1': ['index_trade'], 'var_call_PSPcRSNzr4WJP46HFvE1NFxm': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '2346'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'n': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'n': '8438'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '8492'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '12690'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '13947'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '5869'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'n': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'n': '5760'}], 'var_call_dpuvcPccQaymeGPOROpcMOiA': 'file_storage/call_dpuvcPccQaymeGPOROpcMOiA.json', 'var_call_coFBUQp1finfavd7WrvUEMxQ': [{'Index': 'IXIC', 'return_multiple': 4.823838, 'months': 257, 'last_dt': '2021-05-28'}, {'Index': '399001.SZ', 'return_multiple': 2.372903, 'months': 258, 'last_dt': '2021-06-01'}, {'Index': 'GDAXI', 'return_multiple': 2.354205, 'months': 257, 'last_dt': '2021-05-25'}, {'Index': 'NSEI', 'return_multiple': 2.334174, 'months': 165, 'last_dt': '2021-05-28'}, {'Index': 'TWII', 'return_multiple': 2.2973, 'months': 257, 'last_dt': '2021-05-31'}], 'var_call_gfV01c4LCQvfr0eRV4xSBLTE': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
