code = """import json

top5 = var_call_MsUEIjP6aJ4YKbeVkmNepNtg['top5']

# manual mapping from index symbol to country and exchange
mapping = {
  'IXIC': {'country':'United States', 'exchange':'NASDAQ'},
  'GDAXI': {'country':'Germany', 'exchange':'Frankfurt Stock Exchange'},
  'NSEI': {'country':'India', 'exchange':'National Stock Exchange of India'},
  '399001.SZ': {'country':'China', 'exchange':'Shenzhen Stock Exchange'},
  'TWII': {'country':'Taiwan', 'exchange':'Taiwan Stock Exchange'},
}

out = []
for r in top5:
    idx = r['Index']
    m = mapping.get(idx, {'country': None, 'exchange': None})
    out.append({
        'Index': idx,
        'Country': m['country'],
        'Exchange': m['exchange'],
        'Return_multiple': r['return_multiple']
    })

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_0DZG2j9dPhmxscRPInlUtT6f': ['index_info'], 'var_call_jSJUx0zU6dMXUE6JeTPWQV2T': ['index_trade'], 'var_call_P50EATEDlOvBUR3rN7S02Pp0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_B5bea3BxTopzr7ZVcBPiEbyP': [{'Index': 'NYA', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '13947'}, {'Index': 'N225', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '13874'}, {'Index': 'IXIC', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '12690'}, {'Index': 'GSPTSE', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '10526'}, {'Index': 'HSI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '8492'}, {'Index': 'GDAXI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '8438'}, {'Index': 'SSMI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '7671'}, {'Index': 'TWII', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5869'}, {'Index': '000001.SS', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5791'}, {'Index': '399001.SZ', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5760'}, {'Index': 'N100', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '5474'}, {'Index': 'NSEI', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '3346'}, {'Index': 'J203.JO', 'min_date_iso': 'NaT', 'max_date_iso': 'NaT', 'n': '2346'}], 'var_call_u7r4lGgY4KXBKDARPT7oUAmY': [{'Date': '05 Feb 1971, 00:00'}, {'Date': '08 Feb 1971, 00:00'}, {'Date': '1971-02-09 00:00:00'}, {'Date': '1971-02-10 00:00:00'}, {'Date': '11 Feb 1971, 00:00'}], 'var_call_zftAiDpMqvyCLxtxTBcFmAHz': 'file_storage/call_zftAiDpMqvyCLxtxTBcFmAHz.json', 'var_call_MsUEIjP6aJ4YKbeVkmNepNtg': {'top5': [{'Index': 'IXIC', 'start_month': '2000-01-01', 'end_month': '2021-06-01', 'months': 258, 'final_value_per_1_monthly': 1239.7807667385002, 'invested': 258.0, 'return_multiple': 4.805351809063954}, {'Index': 'GDAXI', 'start_month': '2000-01-01', 'end_month': '2021-06-01', 'months': 258, 'final_value_per_1_monthly': 605.8573208840435, 'invested': 258.0, 'return_multiple': 2.348284189473037}, {'Index': 'NSEI', 'start_month': '2007-09-01', 'end_month': '2021-06-01', 'months': 166, 'final_value_per_1_monthly': 389.20135014316634, 'invested': 166.0, 'return_multiple': 2.34458644664558}, {'Index': '399001.SZ', 'start_month': '2000-01-01', 'end_month': '2021-06-01', 'months': 258, 'final_value_per_1_monthly': 603.7382312828528, 'invested': 258.0, 'return_multiple': 2.340070663887026}, {'Index': 'TWII', 'start_month': '2000-01-01', 'end_month': '2021-06-01', 'months': 258, 'final_value_per_1_monthly': 592.0766821570282, 'invested': 258.0, 'return_multiple': 2.2948708610737527}]}}

exec(code, env_args)
