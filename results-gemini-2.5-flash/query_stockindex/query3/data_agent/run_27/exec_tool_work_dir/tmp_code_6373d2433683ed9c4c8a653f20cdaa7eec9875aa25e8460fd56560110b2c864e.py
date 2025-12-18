code = """import json

top_indices_data = json.loads(locals()['var_function-call-12628723892102873515'])

index_to_country = {
    "IXIC": "United States",
    "NSEI": "India",
    "GDAXI": "Germany",
    "399001.SZ": "China",
    "TWII": "Taiwan"
}

result = []
for item in top_indices_data:
    index_symbol = item['Index']
    country = index_to_country.get(index_symbol, "N/A")
    result.append({'Index': index_symbol, 'OverallReturn': item['OverallReturn'], 'Country': country})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12624981542445449335': 'file_storage/function-call-12624981542445449335.json', 'var_function-call-12628723892102873515': [{'Index': 'IXIC', 'OverallReturn': 3.8220467671}, {'Index': 'NSEI', 'OverallReturn': 1.3608849755}, {'Index': 'GDAXI', 'OverallReturn': 1.3474623836}, {'Index': '399001.SZ', 'OverallReturn': 1.3445453364}, {'Index': 'TWII', 'OverallReturn': 1.2374061754}], 'var_function-call-13042017742281230765': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}]}

exec(code, env_args)
