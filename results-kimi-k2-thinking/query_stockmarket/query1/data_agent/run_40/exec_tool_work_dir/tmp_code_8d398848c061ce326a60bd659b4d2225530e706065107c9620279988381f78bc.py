code = """import json
result = locals()['var_functions.query_db:6']
price = float(result[0]['max_adj_close'])
print('__RESULT__:')
print("%.2f" % price)"""

env_args = {'var_functions.query_db:0': [{'Nasdaq Traded': 'Y', 'Symbol': 'REAL', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:6': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
