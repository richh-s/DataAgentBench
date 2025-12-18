code = """import json

top_indices_data = json.loads(locals()['var_function-call-13217983303570001839'])
top_5_indices = top_indices_data['top_5_indices']
top_5_returns = top_indices_data['top_5_returns']

# Manually map indices to countries based on the database description and general knowledge.
# This mapping is derived from the 'Exchange' field in indexinfo_database and common knowledge.
index_to_country = {
    "399001.SZ": "China", # Shenzhen Stock Exchange
    "NSEI": "India", # National Stock Exchange of India
    "IXIC": "United States", # NASDAQ
    "NYA": "United States", # New York Stock Exchange
    "000001.SS": "China" # Shanghai Stock Exchange
}

answer_parts = []
for i, index in enumerate(top_5_indices):
    country = index_to_country.get(index, "Unknown")
    return_percentage = f'{top_5_returns[i]:.2f}%'
    answer_parts.append(f"{index} ({country}): {return_percentage}")

final_answer = "The 5 indices with the highest overall returns since 2000 are: " + "; ".join(answer_parts) + "."

print("__RESULT__:")
print(json.dumps(final_answer))"""

env_args = {'var_function-call-15490260447422397754': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}], 'var_function-call-1238247793098822744': 'file_storage/function-call-1238247793098822744.json', 'var_function-call-13217983303570001839': {'top_5_indices': ['399001.SZ', 'NSEI', 'IXIC', 'NYA', '000001.SS'], 'top_5_returns': [307.5615733668519, 239.52861132196577, 232.80661695049764, 152.10271160662933, 143.33195347149902]}, 'var_function-call-11092099957009546292': ['index_info'], 'var_function-call-18009278309044292823': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
