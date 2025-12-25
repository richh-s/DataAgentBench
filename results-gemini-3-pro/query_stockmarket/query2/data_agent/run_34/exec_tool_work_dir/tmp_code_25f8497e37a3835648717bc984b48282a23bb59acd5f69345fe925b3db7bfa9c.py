code = """import json
with open(locals()['var_function-call-18110408372543862567'], 'r') as f:
    symbols = json.load(f)
print("__RESULT__:")
print(json.dumps(symbols[-400:]))"""

env_args = {'var_function-call-5893355739321017328': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-7854825807515924036': 'file_storage/function-call-7854825807515924036.json', 'var_function-call-78437376934120291': 'file_storage/function-call-78437376934120291.json', 'var_function-call-18110408372543862567': 'file_storage/function-call-18110408372543862567.json', 'var_function-call-5586898870354241742': 1435, 'var_function-call-14458840651299677807': [{'Date': '2018-08-15'}]}

exec(code, env_args)
