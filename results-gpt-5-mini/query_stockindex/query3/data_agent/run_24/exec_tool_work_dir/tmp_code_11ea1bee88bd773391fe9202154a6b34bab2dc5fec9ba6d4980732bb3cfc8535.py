code = """import json
# Read previous result
res = var_call_4LAQ2WBmsqMqx9AU2oN0Wa8q
# Prepare a human-readable final answer string
lines = []
lines.append('Top 5 indices by overall return for monthly $1 investments since 2000:')
for i, r in enumerate(res, start=1):
    lines.append(f"{i}. {r['Index']} ({r['country']}): total invested ${r['total_invested']:.2f}, final value ${r['final_value']:.2f}, factor {r['factor']:.3f}x")
answer = '\n'.join(lines)
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_mQGpBKUyRPqrKkKLnN53YKk0': ['index_trade'], 'var_call_2nbhKfAWkCuFMBUpsQiDzrQ5': 'file_storage/call_2nbhKfAWkCuFMBUpsQiDzrQ5.json', 'var_call_c6eHGTP79UgbJVFw0qi1ZlAG': ['index_info'], 'var_call_uBloPhRHxhXExSUX346o3xBo': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_4LAQ2WBmsqMqx9AU2oN0Wa8q': [{'Index': 'IXIC', 'months': 257, 'final_value': 1240.4672172509984, 'total_invested': 257.0, 'factor': 4.826720689692601, 'country': 'United States'}, {'Index': 'NSEI', 'months': 165, 'final_value': 389.1416699402238, 'total_invested': 165.0, 'factor': 2.3584343632740836, 'country': 'India'}, {'Index': 'GDAXI', 'months': 257, 'final_value': 603.4975021282868, 'total_invested': 257.0, 'factor': 2.3482393078921664, 'country': 'Germany'}, {'Index': '399001.SZ', 'months': 258, 'final_value': 605.7656363738438, 'total_invested': 258.0, 'factor': 2.347928823154433, 'country': 'China'}, {'Index': 'TWII', 'months': 257, 'final_value': 590.2377706529562, 'total_invested': 257.0, 'factor': 2.2966450219959387, 'country': 'Taiwan'}]}

exec(code, env_args)
