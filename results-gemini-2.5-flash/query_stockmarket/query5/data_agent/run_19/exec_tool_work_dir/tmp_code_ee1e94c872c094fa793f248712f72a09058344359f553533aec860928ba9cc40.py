code = """import json

with open(locals()['var_function-call-1323294415120040832'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)

symbols = [company["Symbol"] for company in nasdaq_capital_market_companies]
company_names = {company["Symbol"]: company["Company Description"] for company in nasdaq_capital_market_companies}

print("__RESULT__:")
print(json.dumps({'symbols': symbols, 'company_names': company_names}))"""

env_args = {'var_function-call-1323294415120040832': 'file_storage/function-call-1323294415120040832.json'}

exec(code, env_args)
