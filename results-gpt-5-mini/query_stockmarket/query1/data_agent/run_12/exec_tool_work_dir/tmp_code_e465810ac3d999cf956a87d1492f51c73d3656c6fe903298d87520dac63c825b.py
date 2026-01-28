code = """import json
# var_call_eBAWygYYqPfUdUflYJ535mz0 and var_call_YA1XHDIQjfWS8pESZrUXUZ9k are available from storage
result_record = var_call_YA1XHDIQjfWS8pESZrUXUZ9k[0]
max_adj = float(result_record['max_adj_close']) if result_record['max_adj_close'] is not None else None
output = {
    'ticker': var_call_eBAWygYYqPfUdUflYJ535mz0[0]['Symbol'],
    'company': var_call_eBAWygYYqPfUdUflYJ535mz0[0]['Company Description'],
    'year': 2020,
    'max_adjusted_close': max_adj
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_eBAWygYYqPfUdUflYJ535mz0': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_YA1XHDIQjfWS8pESZrUXUZ9k': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
