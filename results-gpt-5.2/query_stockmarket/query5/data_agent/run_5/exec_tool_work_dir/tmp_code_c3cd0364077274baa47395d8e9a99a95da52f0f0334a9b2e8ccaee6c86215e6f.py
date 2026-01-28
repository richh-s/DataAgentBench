code = """import json, pandas as pd
path = var_call_YZCMnQZ9llzwejyPLHTIQZN1
with open(path,'r') as f:
    info = json.load(f)

tickers = sorted({r['Symbol'] for r in info if r.get('Symbol')})
# filter to likely common stocks only: exclude symbols with non-alpha chars or length>5 (warrants/units/preferred)
common = [t for t in tickers if t.isalpha() and 1 <= len(t) <= 5]
print('__RESULT__:')
print(json.dumps({'tickers': common, 'n': len(common)}))"""

env_args = {'var_call_YZCMnQZ9llzwejyPLHTIQZN1': 'file_storage/call_YZCMnQZ9llzwejyPLHTIQZN1.json'}

exec(code, env_args)
