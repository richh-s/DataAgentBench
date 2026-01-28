code = """import json
import os

def load_maybe_path(var):
    if isinstance(var, str) and os.path.exists(var):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

stockinfo_records = load_maybe_path(var_call_WieKl7aHdSZW9WQUOPcwhEKt)
trade_tables = load_maybe_path(var_call_VgonKm8xOr3QKnin3IPr4pvT)

out = {
    'type_stockinfo': type(stockinfo_records).__name__,
    'len_stockinfo': len(stockinfo_records) if hasattr(stockinfo_records, '__len__') else None,
    'type_trade_tables': type(trade_tables).__name__,
    'len_trade_tables': len(trade_tables) if hasattr(trade_tables, '__len__') else None
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json'}

exec(code, env_args)
