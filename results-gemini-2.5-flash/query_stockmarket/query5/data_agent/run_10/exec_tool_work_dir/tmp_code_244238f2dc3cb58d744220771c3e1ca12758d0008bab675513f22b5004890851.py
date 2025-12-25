code = """import json
import pandas as pd

with open(locals()['var_function-call-17136481753764545298'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)

symbols_and_descriptions = {company['Symbol']: company['Company Description'] for company in nasdaq_capital_market_companies}

print("__RESULT__:")
print(json.dumps(symbols_and_descriptions))"""

env_args = {'var_function-call-17136481753764545298': 'file_storage/function-call-17136481753764545298.json'}

exec(code, env_args)
