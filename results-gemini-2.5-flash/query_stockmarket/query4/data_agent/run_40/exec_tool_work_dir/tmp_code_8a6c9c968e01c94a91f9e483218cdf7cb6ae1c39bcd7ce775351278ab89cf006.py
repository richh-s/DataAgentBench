code = """import json
import pandas as pd

with open(locals()['var_function-call-16320646233867090762'], 'r') as f:
    stock_info = json.load(f)

nyse_non_etf_stocks = {}
for stock in stock_info:
    nyse_non_etf_stocks[stock['Symbol']] = stock['Company Description']

print("__RESULT__:")
print(json.dumps(nyse_non_etf_stocks))"""

env_args = {'var_function-call-16320646233867090762': 'file_storage/function-call-16320646233867090762.json'}

exec(code, env_args)
