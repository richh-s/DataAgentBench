code = """import json, pandas as pd

# load symbol list
with open(var_call_q7oLujAQPcdluZq4wIf6UcE4,'r') as f:
    symbols = [r['symbol'] for r in json.load(f)]
# load table list
with open(var_call_xKK2gQkeQKeKmrdma80MfrG0,'r') as f:
    tables = set(json.load(f))

symbols = [s for s in symbols if s in tables]

# limit to 2015 exists and adj close > 200 using UNION ALL, but build in chunks and execute via query_db (not inside python via functions)
# Here: just output list of symbols to be processed externally (tool loop not possible). We'll instead process in python by generating queries and calling query_db is not allowed.

print('__RESULT__:')
print(json.dumps({'n_symbols':len(symbols), 'first10':symbols[:10]}))"""

env_args = {'var_call_q7oLujAQPcdluZq4wIf6UcE4': 'file_storage/call_q7oLujAQPcdluZq4wIf6UcE4.json', 'var_call_xKK2gQkeQKeKmrdma80MfrG0': 'file_storage/call_xKK2gQkeQKeKmrdma80MfrG0.json', 'var_call_jJUBPAtNoi8bQ9MNZXglcH03': {'note': 'debug'}, 'var_call_HjxlIEC3cbHYpkUPYIoXy2d7': [{'symbol': 'TEST', 'max_adj_close_2015': 'nan'}]}

exec(code, env_args)
