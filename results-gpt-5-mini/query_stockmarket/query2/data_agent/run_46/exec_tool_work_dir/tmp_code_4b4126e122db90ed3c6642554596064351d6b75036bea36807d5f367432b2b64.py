code = """import json
# Load storage-provided variables
path_symbols = var_call_mwWfV56CQspzhVkLgPfShwWD
path_tables = var_call_TYsnYBbqsJoUwlZSBpmefIXP
with open(path_symbols, 'r') as f:
    symbols_list = json.load(f)
with open(path_tables, 'r') as f:
    tables_list = json.load(f)
# symbols_list is list of dicts with 'Symbol'
symbols = [d['Symbol'] for d in symbols_list]
# Intersection
tables_set = set(tables_list)
symbols_set = set(symbols)
intersection = sorted(list(symbols_set & tables_set))
# Candidates to check
candidates = ['SPY', 'VOO', 'IVV', 'DIA', 'QQQ']
present_candidates = [c for c in candidates if c in intersection]
output = {'num_etf_in_stockinfo_with_table': len(intersection), 'present_candidates': present_candidates, 'sample_intersection_first_50': intersection[:50]}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_mwWfV56CQspzhVkLgPfShwWD': 'file_storage/call_mwWfV56CQspzhVkLgPfShwWD.json', 'var_call_TYsnYBbqsJoUwlZSBpmefIXP': 'file_storage/call_TYsnYBbqsJoUwlZSBpmefIXP.json'}

exec(code, env_args)
