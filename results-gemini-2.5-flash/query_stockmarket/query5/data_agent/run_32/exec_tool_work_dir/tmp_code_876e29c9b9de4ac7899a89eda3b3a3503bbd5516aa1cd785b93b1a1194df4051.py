code = """import json
import pandas as pd

file_path = locals()['var_function-call-11315543107436198562']
with open(file_path, 'r') as f:
    nasdaq_capital_market_stocks = json.load(f)

df_nasdaq = pd.DataFrame(nasdaq_capital_market_stocks)
print("__RESULT__:")
print(df_nasdaq.to_json(orient='records'))"""

env_args = {'var_function-call-11315543107436198562': 'file_storage/function-call-11315543107436198562.json'}

exec(code, env_args)
