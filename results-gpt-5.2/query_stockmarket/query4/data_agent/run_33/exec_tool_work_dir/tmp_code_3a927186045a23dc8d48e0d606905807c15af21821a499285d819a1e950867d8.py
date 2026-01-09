code = """import json
from pathlib import Path

sym_data = json.loads(Path(var_call_oIR00k72R1HbHiVAZ5Jsi8oa).read_text())
nyse_syms = set(sym_data['symbols'])

trade_tables = json.loads(Path(var_call_7Pp9E0aiz2wVfAj9focr1xtx).read_text())
trade_set = set(trade_tables)

symbols_in_trade = sorted(list(nyse_syms & trade_set))

print('__RESULT__:')
print(json.dumps({'symbols_in_trade': symbols_in_trade, 'name_map': sym_data['name_map']}))"""

env_args = {'var_call_TWmoaj5nxzkNWCttpzyMj9Oo': 'file_storage/call_TWmoaj5nxzkNWCttpzyMj9Oo.json', 'var_call_oIR00k72R1HbHiVAZ5Jsi8oa': 'file_storage/call_oIR00k72R1HbHiVAZ5Jsi8oa.json', 'var_call_7Pp9E0aiz2wVfAj9focr1xtx': 'file_storage/call_7Pp9E0aiz2wVfAj9focr1xtx.json'}

exec(code, env_args)
