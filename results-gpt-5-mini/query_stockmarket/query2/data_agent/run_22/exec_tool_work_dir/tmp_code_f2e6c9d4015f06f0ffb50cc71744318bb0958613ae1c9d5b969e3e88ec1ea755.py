code = """import json, os
# Access previous storage variables
data_stockinfo = var_call_DG3QOs7vOSoK4UcA4sepoE72
data_stocktrade_tables = var_call_IZXraRyNaZHsPImlQfrnZ3PY
# load from file if necessary
if isinstance(data_stockinfo, str) and os.path.exists(data_stockinfo):
    with open(data_stockinfo, 'r', encoding='utf-8') as f:
        stockinfo_symbols = json.load(f)
else:
    stockinfo_symbols = data_stockinfo
if isinstance(data_stocktrade_tables, str) and os.path.exists(data_stocktrade_tables):
    with open(data_stocktrade_tables, 'r', encoding='utf-8') as f:
        trade_tables = json.load(f)
else:
    trade_tables = data_stocktrade_tables
# compute intersection keeping only symbols that are valid table names in trade_tables
set_stockinfo = set(stockinfo_symbols)
set_trade = set(trade_tables)
intersection = sorted(list(set_stockinfo & set_trade))
print("__RESULT__:")
print(json.dumps(intersection))"""

env_args = {'var_call_qPWkYeKXPqjNVSXJnmDnWape': 'file_storage/call_qPWkYeKXPqjNVSXJnmDnWape.json', 'var_call_DG3QOs7vOSoK4UcA4sepoE72': 'file_storage/call_DG3QOs7vOSoK4UcA4sepoE72.json', 'var_call_IZXraRyNaZHsPImlQfrnZ3PY': 'file_storage/call_IZXraRyNaZHsPImlQfrnZ3PY.json'}

exec(code, env_args)
