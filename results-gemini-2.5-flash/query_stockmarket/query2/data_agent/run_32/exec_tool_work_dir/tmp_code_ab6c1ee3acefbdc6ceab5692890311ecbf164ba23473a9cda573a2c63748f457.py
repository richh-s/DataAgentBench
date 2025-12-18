code = """import json
import pandas as pd

with open(locals()['var_function-call-16027928627600003546'], 'r') as f:
    arca_etfs = json.load(f)

arca_etf_symbols = [d['Symbol'] for d in arca_etfs]

__RESULT__:
print(json.dumps(arca_etf_symbols[:5]))"""

env_args = {'var_function-call-16027928627600003546': 'file_storage/function-call-16027928627600003546.json'}

exec(code, env_args)
