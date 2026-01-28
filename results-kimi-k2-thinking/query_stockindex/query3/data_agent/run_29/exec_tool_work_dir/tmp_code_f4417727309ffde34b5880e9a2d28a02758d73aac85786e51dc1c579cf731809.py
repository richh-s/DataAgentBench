code = """import json

# Load the partial results we've received
index_info = var_functions.list_db:0
partial_index_data = var_functions.list_db:4
sample_n225 = var_functions.list_db:6
all_indices = var_functions.list_db:8

print('__RESULT__:')
print(json.dumps({
    "index_info_sample": index_info,
    "all_indices": all_indices
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225', 'Date': '01 Apr 1971, 00:00', 'CloseUSD': '24.14040039'}, {'Index': 'N225', 'Date': '01 Apr 1976, 00:00', 'CloseUSD': '45.81819824'}, {'Index': 'N225', 'Date': '01 Apr 1977, 00:00', 'CloseUSD': '50.08379883'}, {'Index': 'N225', 'Date': '01 Apr 1980, 00:00', 'CloseUSD': '65.02799805'}, {'Index': 'N225', 'Date': '01 Apr 1981, 00:00', 'CloseUSD': '73.89990234'}, {'Index': 'N225', 'Date': '01 Apr 1982, 00:00', 'CloseUSD': '72.93669922000001'}, {'Index': 'N225', 'Date': '01 Apr 1987, 00:00', 'CloseUSD': '220.4017969'}, {'Index': 'N225', 'Date': '01 Apr 1988, 00:00', 'CloseUSD': '261.042207'}, {'Index': 'N225', 'Date': '01 Apr 1992, 00:00', 'CloseUSD': '185.8178906'}, {'Index': 'N225', 'Date': '01 Apr 1998, 00:00', 'CloseUSD': '162.4166016'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
