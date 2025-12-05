code = """import json
import pandas as pd
from pathlib import Path

symbols = json.loads(Path(var_call_z3w05wE5Ypxfbtq7ucO6JvyI).read_text())

print("__RESULT__:")
print(json.dumps(symbols))"""

env_args = {'var_call_z3w05wE5Ypxfbtq7ucO6JvyI': 'file_storage/call_z3w05wE5Ypxfbtq7ucO6JvyI.json', 'var_call_MWllCGhgDvLPK7utbFrlPQzp': 'file_storage/call_MWllCGhgDvLPK7utbFrlPQzp.json'}

exec(code, env_args)
