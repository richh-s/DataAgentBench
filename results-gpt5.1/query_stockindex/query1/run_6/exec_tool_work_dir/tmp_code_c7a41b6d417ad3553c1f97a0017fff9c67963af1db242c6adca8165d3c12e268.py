code = """import json
# Map Asia-region exchanges to their main indices based on domain knowledge and available symbols
asia_mapping = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': 'NSEI',
    'Korea Exchange': None,  # no direct index symbol present in index_trade list
    'Taiwan Stock Exchange': 'TWII'
}

asia_indices = sorted({idx for idx in asia_mapping.values() if idx is not None})

result = json.dumps({"asia_indices": asia_indices})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4914CCCT8ojSE8x7sELIRbjg': ['index_info'], 'var_call_vyocvVs7DlTTEZUxJIRc2p0w': ['index_trade'], 'var_call_U1PR7Aorhu96xtF2ry8rj2Kq': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_vzmKuR61dKH6HhondX7sVftU': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}]}

exec(code, env_args)
