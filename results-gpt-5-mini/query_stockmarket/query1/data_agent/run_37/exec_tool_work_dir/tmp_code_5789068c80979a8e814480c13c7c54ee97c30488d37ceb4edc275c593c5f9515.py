code = """import json
# Access previous query results from storage
rec_info = var_call_IQ05VhiAPKecEwL6KCJhsoEP[0]
rec_price = var_call_ZCbgWcAZ5lT7kvO7g8NFExLD[0]
# Extract company name (take text before ' is ' to get the official name)
company_desc = rec_info.get('Company Description', '')
company_name = company_desc.split(' is ')[0] if ' is ' in company_desc else company_desc
# Extract and format max adjusted close
max_adj = float(rec_price.get('max_adj_close'))
max_adj_rounded = round(max_adj, 2)
output = {
    'symbol': rec_info.get('Symbol'),
    'company': company_name,
    'year': 2020,
    'max_adj_close': max_adj_rounded
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_IQ05VhiAPKecEwL6KCJhsoEP': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_ZCbgWcAZ5lT7kvO7g8NFExLD': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
