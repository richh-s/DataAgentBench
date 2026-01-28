code = """import json
with open(var_call_cOi9OMUYcXvqMM1mSCci0y6k, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_ppF3FrkgSKRwnihegO5SvHTe, 'r') as f:
    tables = json.load(f)
symbols_s = [rec['Symbol'] for rec in stockinfo if rec.get('Market Category') == 'S']
symbols_s = [s.strip() for s in symbols_s]
tables_set = set(tables)
symbols_to_query = sorted([s for s in symbols_s if s in tables_set])
# Output as JSON list
print('__RESULT__:')
print(json.dumps(symbols_to_query))"""

env_args = {'var_call_cOi9OMUYcXvqMM1mSCci0y6k': 'file_storage/call_cOi9OMUYcXvqMM1mSCci0y6k.json', 'var_call_ppF3FrkgSKRwnihegO5SvHTe': 'file_storage/call_ppF3FrkgSKRwnihegO5SvHTe.json'}

exec(code, env_args)
