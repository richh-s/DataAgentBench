code = """import json

p1 = locals()['var_function-call-13664371360467966876']
with open(p1, 'r') as f:
    d = json.load(f)
syms = set(i['Symbol'] for i in d)

p2 = locals()['var_function-call-9828464466004639384']
with open(p2, 'r') as f:
    t = json.load(f)
tabs = set(t)

valid = sorted(list(syms.intersection(tabs)))
print('__RESULT__:')
print(json.dumps(valid))"""

env_args = {'var_function-call-277767683765402362': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}], 'var_function-call-13664371360467966876': 'file_storage/function-call-13664371360467966876.json', 'var_function-call-2894604771842111862': 86, 'var_function-call-9828464466004639384': 'file_storage/function-call-9828464466004639384.json', 'var_function-call-9364308099402691955': [{'Date': '2018-08-15'}]}

exec(code, env_args)
