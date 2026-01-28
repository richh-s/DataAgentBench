code = """import json, os

def load(var):
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

stockinfo = load(var_call_WieKl7aHdSZW9WQUOPcwhEKt)
trade_tables = load(var_call_VgonKm8xOr3QKnin3IPr4pvT)

trade_upper = set([t.upper() for t in trade_tables])

symbols = []
for rec in stockinfo:
    s = rec.get('Symbol')
    if s:
        su = s.upper()
        if su in trade_upper:
            symbols.append(su)

print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json', 'var_call_9kEodSYCb5yj1kZ4zEVqvNCc': {'type_stockinfo': 'list', 'len_stockinfo': 86, 'type_trade_tables': 'list', 'len_trade_tables': 2753}, 'var_call_7L41ZFTbZeAqvr48T0bE1vD2': 'file_storage/call_7L41ZFTbZeAqvr48T0bE1vD2.json'}

exec(code, env_args)
