code = """import json, pandas as pd

best = var_call_M9uVzw0R33XFtLqyYSGrXmSq
cpc_defs_path = var_call_IrVqEbdgOY8EMxXqILKIqbJw
with open(cpc_defs_path, 'r') as f:
    defs = json.load(f)

# build lookup for level-4 symbol titles
lookup = {d['symbol']: d['titleFull'] for d in defs}

for row in best:
    sym = row['group']
    row['titleFull'] = lookup.get(sym, '')

print("__RESULT__:")
print(json.dumps(best))"""

env_args = {'var_call_pJElfgQTTH7bcGaPvoq90XXA': 'file_storage/call_pJElfgQTTH7bcGaPvoq90XXA.json', 'var_call_IrVqEbdgOY8EMxXqILKIqbJw': 'file_storage/call_IrVqEbdgOY8EMxXqILKIqbJw.json', 'var_call_M9uVzw0R33XFtLqyYSGrXmSq': [{'group': 'C04', 'best_year': 2019, 'max_ema': 45.0}, {'group': 'H04', 'best_year': 2019, 'max_ema': 36.0}, {'group': 'F02', 'best_year': 2019, 'max_ema': 26.0}, {'group': 'B29', 'best_year': 2019, 'max_ema': 20.0}, {'group': 'H01', 'best_year': 2019, 'max_ema': 16.0}, {'group': 'F04', 'best_year': 2019, 'max_ema': 16.0}, {'group': 'G02', 'best_year': 2019, 'max_ema': 12.0}, {'group': 'F23', 'best_year': 2019, 'max_ema': 11.0}, {'group': 'A61', 'best_year': 2019, 'max_ema': 9.0}, {'group': 'F16', 'best_year': 2019, 'max_ema': 8.0}, {'group': 'Y02', 'best_year': 2019, 'max_ema': 6.0}, {'group': 'E02', 'best_year': 2019, 'max_ema': 6.0}, {'group': 'E21', 'best_year': 2019, 'max_ema': 5.0}, {'group': 'A43', 'best_year': 2019, 'max_ema': 5.0}, {'group': 'B60', 'best_year': 2019, 'max_ema': 4.0}, {'group': 'F01', 'best_year': 2019, 'max_ema': 4.0}, {'group': 'F24', 'best_year': 2019, 'max_ema': 3.0}, {'group': 'B41', 'best_year': 2019, 'max_ema': 3.0}, {'group': 'F42', 'best_year': 2019, 'max_ema': 2.0}, {'group': 'G07', 'best_year': 2019, 'max_ema': 2.0}]}

exec(code, env_args)
