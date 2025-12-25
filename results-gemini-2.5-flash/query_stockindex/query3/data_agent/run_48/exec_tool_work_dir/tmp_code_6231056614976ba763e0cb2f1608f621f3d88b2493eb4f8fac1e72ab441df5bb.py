code = """import json

top_indices_data = locals()['var_function-call-11995912372844846335']

index_country_map = {
    "IXIC": "United States",
    "GDAXI": "Germany",
    "NSEI": "India",
    "399001.SZ": "China",
    "TWII": "Taiwan"
}

result = []
for item in top_indices_data:
    index_symbol = item['Index']
    country = index_country_map.get(index_symbol, "N/A")
    result.append({"Index": index_symbol, "OverallReturn": item['OverallReturn'], "Country": country})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-1641922140904638122': 'file_storage/function-call-1641922140904638122.json', 'var_function-call-11995912372844846335': [{'Index': 'IXIC', 'OverallReturn': 3.8238257246}, {'Index': 'GDAXI', 'OverallReturn': 1.3492850291}, {'Index': 'NSEI', 'OverallReturn': 1.3486561808}, {'Index': '399001.SZ', 'OverallReturn': 1.3404194418}, {'Index': 'TWII', 'OverallReturn': 1.2964516961}], 'var_function-call-6188804342383102955': ['index_info'], 'var_function-call-17241174972976713909': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
