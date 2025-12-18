code = """import json
import pandas as pd

with open(locals()['var_function-call-12239073285659472984'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)

symbol_company_map = {company['Symbol']: company['Company Description'] for company in nasdaq_capital_market_companies}

print("__RESULT__:")
print(json.dumps(list(symbol_company_map.keys())[:10])) # Print first 10 symbols to check, then proceed"""

env_args = {'var_function-call-12239073285659472984': 'file_storage/function-call-12239073285659472984.json'}

exec(code, env_args)
