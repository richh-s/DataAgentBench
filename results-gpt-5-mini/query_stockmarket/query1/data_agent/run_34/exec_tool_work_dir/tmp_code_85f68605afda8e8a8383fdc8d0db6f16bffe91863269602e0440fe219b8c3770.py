code = """import json

# Use the stored query results
# var_call_gRcmBudsWj9pJY241lF12Mz9 and var_call_yFjdGrs4Nbv575bqyYQyDux7 are available in the environment

# Extract symbol and company description
metadata = var_call_gRcmBudsWj9pJY241lF12Mz9
trade_result = var_call_yFjdGrs4Nbv575bqyYQyDux7

symbol = metadata[0]['Symbol'] if metadata else None
company = metadata[0]['Company Description'] if metadata else None

max_adj_close_str = trade_result[0]['max_adj_close'] if trade_result else None
try:
    max_adj_close = float(max_adj_close_str) if max_adj_close_str is not None else None
except:
    max_adj_close = None

output = {
    'symbol': symbol,
    'company': company,
    'max_adjusted_close_2020': max_adj_close
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_gRcmBudsWj9pJY241lF12Mz9': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_yFjdGrs4Nbv575bqyYQyDux7': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
