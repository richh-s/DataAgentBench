code = """import json
rows = var_call_i49X01IpDmELAXevs4g4q92e
ans = [r['Index'] for r in rows if float(r['up_days']) > float(r['down_days'])]
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_sSElGZ4drcCj4irFUQxu5wrT': ['index_info'], 'var_call_n7wXAafBki9ZgUXVhtJONtLJ': ['index_trade'], 'var_call_NqUtJCluVuecQSwZfOfyGlNw': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_WzO3fe01rQyfAK9TaamUqnAG': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_i49X01IpDmELAXevs4g4q92e': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
