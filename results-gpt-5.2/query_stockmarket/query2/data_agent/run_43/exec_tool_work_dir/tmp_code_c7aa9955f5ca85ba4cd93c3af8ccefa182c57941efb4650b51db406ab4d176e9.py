code = """import json, pandas as pd

# Load NYSE Arca ETFs
arca_path = var_call_zjYjRfp8wuGsrjishFwvDIsi
with open(arca_path, 'r') as f:
    arca = json.load(f)

df_arca = pd.DataFrame(arca)

# Load available price tables list
trade_list_path = var_call_z2cyof62djNmQtjHxGguLbb9
with open(trade_list_path, 'r') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in df_arca['Symbol'].dropna().astype(str).tolist() if s in trade_tables]

# Return for querying
out = json.dumps({"symbols": symbols, "missing_price_table_count": int(len(df_arca)-len(symbols))})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zjYjRfp8wuGsrjishFwvDIsi': 'file_storage/call_zjYjRfp8wuGsrjishFwvDIsi.json', 'var_call_z2cyof62djNmQtjHxGguLbb9': 'file_storage/call_z2cyof62djNmQtjHxGguLbb9.json'}

exec(code, env_args)
