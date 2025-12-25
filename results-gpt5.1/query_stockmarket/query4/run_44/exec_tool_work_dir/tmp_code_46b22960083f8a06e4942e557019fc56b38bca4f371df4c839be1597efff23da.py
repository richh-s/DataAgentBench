code = """import json
import pandas as pd

symbols_path = var_call_R5hudPl6aQNRDhoIcMWWjp6K
with open(symbols_path, 'r') as f:
    all_symbols = json.load(f)

nyse_records_path = var_call_9qYsRCRBG6lqGuefPsqjksr5
with open(nyse_records_path, 'r') as f:
    nyse_records = json.load(f)

nyse_symbols = {r['Symbol'] for r in nyse_records}
valid_symbols = [s for s in all_symbols if s in nyse_symbols]

batch_size = 200
batches = [valid_symbols[i:i+batch_size] for i in range(0, len(valid_symbols), batch_size)]

result = json.dumps({'batches': batches[:10]})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_R5hudPl6aQNRDhoIcMWWjp6K': 'file_storage/call_R5hudPl6aQNRDhoIcMWWjp6K.json', 'var_call_9qYsRCRBG6lqGuefPsqjksr5': 'file_storage/call_9qYsRCRBG6lqGuefPsqjksr5.json'}

exec(code, env_args)
