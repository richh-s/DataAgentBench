code = """import json, pandas as pd, os

# load symbol list for NASDAQ Capital Market from stockinfo query
path = var_call_27OZ5X7c07iVF4YQv2tkxwVi
with open(path, 'r') as f:
    stockinfo = json.load(f)

df_info = pd.DataFrame(stockinfo)
# symbols we care about
symbols = sorted(df_info['Symbol'].unique().tolist())

# load all available trade tables
path_tables = var_call_MrkNbn6l6PQHlzA0ui9E6OYt
with open(path_tables, 'r') as f:
    all_tables = json.load(f)

symbols_available = [s for s in symbols if s in set(all_tables)]

result = {
    'symbols': symbols_available[:50],
    'total_symbols_capital_market': len(symbols),
    'total_symbols_with_trades': len(symbols_available)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MrkNbn6l6PQHlzA0ui9E6OYt': 'file_storage/call_MrkNbn6l6PQHlzA0ui9E6OYt.json', 'var_call_27OZ5X7c07iVF4YQv2tkxwVi': 'file_storage/call_27OZ5X7c07iVF4YQv2tkxwVi.json'}

exec(code, env_args)
