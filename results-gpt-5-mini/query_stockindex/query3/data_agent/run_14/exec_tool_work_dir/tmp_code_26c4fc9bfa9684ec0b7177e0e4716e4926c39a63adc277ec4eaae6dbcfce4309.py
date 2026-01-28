code = """import json
# Load previous python result
res = var_call_09bUlRfDIrwsiI7y7wNU4D8t
# Prepare a human-readable summary
summary = [{
    'Rank': i+1,
    'Index': item['Index'],
    'Country': item['Country'],
    'Total_Return_Multiple': item['ReturnRatio'],
    'Months_Invested': item['MonthsInvested']
} for i, item in enumerate(res)]
print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_call_okGt5idIWo1siSDYc8JssgyE': ['index_trade'], 'var_call_Qvc4LUsFOIcKZFPVWNiGVtot': ['index_info'], 'var_call_cAzhJMG6j7PvYHn4yXzVqKQ4': 'file_storage/call_cAzhJMG6j7PvYHn4yXzVqKQ4.json', 'var_call_Ng4nGyOQYlktMOjm8DzStW5o': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_YxwzToo8MlrBTjBhODPwuBPI': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_09bUlRfDIrwsiI7y7wNU4D8t': [{'Index': 'IXIC', 'Country': 'United States', 'MonthsInvested': 241, 'FinalValue': 1196.109114, 'Invested': 241.0, 'ReturnRatio': 4.963108}, {'Index': 'GDAXI', 'Country': 'Germany', 'MonthsInvested': 240, 'FinalValue': 566.274694, 'Invested': 240.0, 'ReturnRatio': 2.359478}, {'Index': 'NSEI', 'Country': 'India', 'MonthsInvested': 152, 'FinalValue': 357.293996, 'Invested': 152.0, 'ReturnRatio': 2.350618}, {'Index': '399001.SZ', 'Country': 'China', 'MonthsInvested': 228, 'FinalValue': 523.749485, 'Invested': 228.0, 'ReturnRatio': 2.297147}, {'Index': 'TWII', 'Country': 'Taiwan', 'MonthsInvested': 244, 'FinalValue': 559.431115, 'Invested': 244.0, 'ReturnRatio': 2.29275}]}

exec(code, env_args)
