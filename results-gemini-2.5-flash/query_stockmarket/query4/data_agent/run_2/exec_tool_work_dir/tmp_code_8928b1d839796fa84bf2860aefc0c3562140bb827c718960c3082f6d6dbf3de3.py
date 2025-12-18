code = """import json
import pandas as pd

with open(locals()['var_function-call-7787057665248036889'], 'r') as f:
    nyse_non_etf_stocks = json.load(f)

# Extract symbols and company descriptions
symbols_and_descriptions = {item['Symbol']: item['Company Description'] for item in nyse_non_etf_stocks}
symbols = list(symbols_and_descriptions.keys())

print("__RESULT__:")
print(json.dumps(symbols_and_descriptions))"""

env_args = {'var_function-call-7787057665248036889': 'file_storage/function-call-7787057665248036889.json'}

exec(code, env_args)
