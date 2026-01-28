code = """import json
# Accessing previous query results available as variables
records_info = var_call_TZxC3NP1j53VlyZLHFrm4pvn
records_trade = var_call_F0jvmrUcBoUnOsSlzV5gmD3m

# Extract company info
symbol = records_info[0].get('Symbol')
company_desc = records_info[0].get('Company Description')
# Try to extract company name before ' is' if present
company_name = company_desc.split(' is')[0] if company_desc and ' is' in company_desc else company_desc

# Extract max adjusted close
max_adj_str = records_trade[0].get('max_adj_close')
max_adj = None
if max_adj_str is not None:
    try:
        max_adj = float(max_adj_str)
    except:
        max_adj = None

result = {
    'symbol': symbol,
    'company_name': company_name,
    'year': 2020,
    'max_adj_close': max_adj
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TZxC3NP1j53VlyZLHFrm4pvn': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_F0jvmrUcBoUnOsSlzV5gmD3m': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
