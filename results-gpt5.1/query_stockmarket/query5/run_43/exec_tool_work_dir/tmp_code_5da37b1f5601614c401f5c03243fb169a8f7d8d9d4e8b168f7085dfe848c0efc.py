code = """import json, pandas as pd
from pathlib import Path

symbols_info = json.load(open(var_call_WBOyChqARAlD8jzRvTJbm8eW))
cap_df = pd.DataFrame(symbols_info)
cap_symbols = set(cap_df['Symbol'])

all_tables = json.load(open(var_call_XKuyIBXOaMFNaGiYK67GWhRC))
common = sorted(list(cap_symbols.intersection(all_tables)))

result = json.dumps(common)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_XKuyIBXOaMFNaGiYK67GWhRC': 'file_storage/call_XKuyIBXOaMFNaGiYK67GWhRC.json', 'var_call_WBOyChqARAlD8jzRvTJbm8eW': 'file_storage/call_WBOyChqARAlD8jzRvTJbm8eW.json'}

exec(code, env_args)
