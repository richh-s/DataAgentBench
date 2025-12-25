code = """import json, pandas as pd
from pathlib import Path

# Load full results
stockinfo_path = Path(var_call_AyPOOrIlL5o3ojsXXwDdZxTl)
with open(stockinfo_path, 'r') as f:
    stockinfo = json.load(f)

tradetables_path = Path(var_call_ZCLf2ylxrmjdigaJTvg9JVo9)
with open(tradetables_path, 'r') as f:
    tradetables = json.load(f)

# Create DataFrame of NASDAQ Capital Market symbols
si_df = pd.DataFrame(stockinfo)
cap_syms = set(si_df['Symbol'].astype(str))

# Filter trade tables to those symbols
trade_syms = [row['table_name'] for row in tradetables]
common_syms = sorted(list(set(trade_syms) & cap_syms))

result = json.dumps(common_syms)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_5l6oHm16DoLVVFmWujUfK2dK': 'file_storage/call_5l6oHm16DoLVVFmWujUfK2dK.json', 'var_call_AyPOOrIlL5o3ojsXXwDdZxTl': 'file_storage/call_AyPOOrIlL5o3ojsXXwDdZxTl.json', 'var_call_ZCLf2ylxrmjdigaJTvg9JVo9': 'file_storage/call_ZCLf2ylxrmjdigaJTvg9JVo9.json'}

exec(code, env_args)
