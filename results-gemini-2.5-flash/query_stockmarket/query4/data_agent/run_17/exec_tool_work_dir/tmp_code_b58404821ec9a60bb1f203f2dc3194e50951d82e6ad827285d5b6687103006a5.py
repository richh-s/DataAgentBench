code = """import json

with open(locals()['var_function-call-10628036944453422318'], 'r') as f:
    stock_info_dict = json.load(f)

symbols = list(stock_info_dict.keys())

print("__RESULT__:")
print(json.dumps(symbols))"""

env_args = {'var_function-call-15043543411406400120': [], 'var_function-call-10707248306571797415': ['stockinfo'], 'var_function-call-3590572963787279885': [{'cid': '0', 'name': 'Nasdaq Traded', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Symbol', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Listing Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Market Category', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'ETF', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Round Lot Size', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'Test Issue', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Financial Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'NextShares', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'Company Description', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15219700771644574740': [{"'Listing Exchange'": 'Listing Exchange'}], 'var_function-call-12878043852616683498': 'file_storage/function-call-12878043852616683498.json', 'var_function-call-10628036944453422318': 'file_storage/function-call-10628036944453422318.json'}

exec(code, env_args)
