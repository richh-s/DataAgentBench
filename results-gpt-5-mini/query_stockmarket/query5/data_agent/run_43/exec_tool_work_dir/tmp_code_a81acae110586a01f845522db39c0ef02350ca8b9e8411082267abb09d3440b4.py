code = """import json, os

def load_maybe_path(var):
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

stockinfo_records = load_maybe_path(var_call_WieKl7aHdSZW9WQUOPcwhEKt)
trade_tables = load_maybe_path(var_call_VgonKm8xOr3QKnin3IPr4pvT)

sym_to_company = {}
for rec in stockinfo_records:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if sym:
        sym_to_company[sym.upper()] = desc

available_tables = [t.upper() for t in trade_tables]

symbols = sorted([s for s in sym_to_company.keys() if s in available_tables])

out = {'symbols': symbols, 'mapping': {s: sym_to_company[s] for s in symbols}}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json', 'var_call_9kEodSYCb5yj1kZ4zEVqvNCc': {'type_stockinfo': 'list', 'len_stockinfo': 86, 'type_trade_tables': 'list', 'len_trade_tables': 2753}}

exec(code, env_args)
