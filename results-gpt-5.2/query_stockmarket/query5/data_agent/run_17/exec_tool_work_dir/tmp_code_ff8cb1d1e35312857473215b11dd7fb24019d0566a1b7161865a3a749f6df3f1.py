code = """import json
from pathlib import Path

symbols_data = json.loads(Path(var_call_JTHspwQDIinhSAQ1zuyKmlbC).read_text())
cap_syms = set(symbols_data['symbols'])

trade_tables = json.loads(Path(var_call_2g7LJVqzIFBNA2vkawUDopgn).read_text())
trade_set = set(trade_tables)

usable = sorted(cap_syms & trade_set)
missing = sorted(cap_syms - trade_set)

out = {'usable_symbols': usable, 'n_usable': len(usable), 'n_missing': len(missing)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qdLIKDynnEUet9nJTfF5AaTo': 'file_storage/call_qdLIKDynnEUet9nJTfF5AaTo.json', 'var_call_JTHspwQDIinhSAQ1zuyKmlbC': 'file_storage/call_JTHspwQDIinhSAQ1zuyKmlbC.json', 'var_call_2g7LJVqzIFBNA2vkawUDopgn': 'file_storage/call_2g7LJVqzIFBNA2vkawUDopgn.json'}

exec(code, env_args)
