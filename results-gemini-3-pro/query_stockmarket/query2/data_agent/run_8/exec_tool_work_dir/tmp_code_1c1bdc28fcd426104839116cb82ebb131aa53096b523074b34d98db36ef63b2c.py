code = """import json

path = locals().get('var_function-call-6325032711824725866')
with open(path, 'r') as f:
    symbols = json.load(f)

# Batch size 30
batch_size = 30
all_queries = []
dq = chr(34)

for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        q = "(SELECT '{0}' as Symbol FROM {1}{0}{1} WHERE {1}Adj Close{1} > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1)".format(s, dq)
        parts.append(q)
    full_query = " UNION ALL ".join(parts)
    all_queries.append(full_query)

with open('all_queries_v2.json', 'w') as f:
    json.dump(all_queries, f)

print("__RESULT__:")
print(json.dumps(f"Generated {len(all_queries)} queries."))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json', 'var_function-call-6325032711824725866': 'file_storage/function-call-6325032711824725866.json', 'var_function-call-16713880611030902886': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_function-call-16160768990026222278': 'file_storage/function-call-16160768990026222278.json', 'var_function-call-1491270065845566597': 1435, 'var_function-call-17396258014626583881': 'file_storage/function-call-17396258014626583881.json', 'var_function-call-7300643933908133279': {'files': ['tmp_code_cf8b44ffeee1945fa4640e50eccd685e7103e77217a78432b62e478e07649d69.py', 'tmp_code_b0867fca649fb71522c7678465812e567030c4dc63883f16ec349fc4c4b618c9.py', 'tmp_code_441c637fee024c0246589a826f7e1ae66406714f18f10f54a07e443ee92fb4f3.py', 'tmp_code_88648664c2d333a20bf767879d5cfd0f075d692e6897fff44615d69e649f9701.py', 'tmp_code_40b3fa2e9272f9898fe17acad3ec761037c4bc66dd6f483269aa1ccbce8ac0e7.py', 'tmp_code_41ed701c94d4df8f2f8f1b4f16b25f99ede94ea672816cd56a5b7eb13b67d842.py', 'tmp_code_8f78065b48851b231093b86f855c6bc922e98c40595dcffe8e1606a0b5bf7678.py', 'file_storage', 'tmp_code_f9092369a0ba8a4fe71b3666100c903a671d1cedcf883c791e1e57042760c93b.py', 'tmp_code_d00e30b58e69fc30e468cc928e3785a0fdc88ac6f20fd03aceba859199187dcc.py', 'tmp_code_25fdc76b45611ff94c6672a1fb568eb01a8b3e6c9003db1f2df9dd38e579e9d8.py', 'tmp_code_668cf4039d04f1cdcd73e4fd37a27cd94c15c86a7c5398383debd7946f81bd3c.py', 'tmp_code_39d177cc6219defff55fd7e25cecd2e7984c61fac7ca2933791648f88c20b106.py'], 'duckdb': 'Not installed'}, 'var_function-call-10062044764401212850': [], 'var_function-call-5755553482351360603': [{'Nasdaq Traded': 'Y', 'Symbol': 'IVV', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "iShares Core S&P 500 ETF offers investors a diversified portfolio by tracking the performance of 500 leading U.S. companies, providing a convenient way to invest in the American economy's top sectors."}], 'var_function-call-5001349875292925541': [], 'var_function-call-963216838837618258': 'Generated 29 queries.', 'var_function-call-15239771824596289412': 'file_storage/function-call-15239771824596289412.json', 'var_function-call-13508597669421163573': [{'Nasdaq Traded': 'Y', 'Symbol': 'TZA', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Direxion Small Cap Bear 3X Shares offers investors a way to profit from declining markets by providing leveraged exposure to the inverse performance of small-cap companies.'}], 'var_function-call-10840183252316027490': [{'Date': '2015-09-29', 'Open': '272.6000061035156', 'High': '282.20001220703125', 'Low': '266.20001220703125', 'Close': '278.0', 'Adj Close': '272.6275939941406', 'Volume': '903900'}]}

exec(code, env_args)
