code = """import json
import pandas as pd

with open(locals()['var_function-call-17280610348183466263'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)

symbols_and_descriptions = {}
for company in nasdaq_capital_market_companies:
    symbols_and_descriptions[company['Symbol']] = company['Company Description']

print("__RESULT__:")
print(json.dumps(symbols_and_descriptions))"""

env_args = {'var_function-call-6559681987713389032': 'file_storage/function-call-6559681987713389032.json', 'var_function-call-17280610348183466263': 'file_storage/function-call-17280610348183466263.json'}

exec(code, env_args)
