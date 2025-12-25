code = """import json
from pathlib import Path

nyse_meta = json.loads(Path(var_call_MWllCGhgDvLPK7utbFrlPQzp).read_text())
all_symbols = json.loads(Path(var_call_L21RBjxbdpdjmXKi1A5TMTG3).read_text())

nyse_symbols = {row['Symbol'] for row in nyse_meta}

common = sorted(list(nyse_symbols.intersection(all_symbols)))

print("__RESULT__:")
print(json.dumps(common))"""

env_args = {'var_call_z3w05wE5Ypxfbtq7ucO6JvyI': 'file_storage/call_z3w05wE5Ypxfbtq7ucO6JvyI.json', 'var_call_MWllCGhgDvLPK7utbFrlPQzp': 'file_storage/call_MWllCGhgDvLPK7utbFrlPQzp.json', 'var_call_L21RBjxbdpdjmXKi1A5TMTG3': 'file_storage/call_L21RBjxbdpdjmXKi1A5TMTG3.json'}

exec(code, env_args)
