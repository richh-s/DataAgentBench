code = """import json
# Read ETF list from stockinfo query result file
with open(var_call_uujsuC1CCLMoXiLygvLHw84R, 'r') as f:
    stockinfo_etfs = json.load(f)
# Read trade tables list
with open(var_call_NMGGKIDoDKAikS77E1C3am3R, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [rec['Symbol'] for rec in stockinfo_etfs]
# Filter to those present in trade DB
symbols_in_trade_db = [s for s in etf_symbols if s in trade_tables]

selects = []
for s in symbols_in_trade_db:
    # Protect table/column names with double quotes
    sel = f"SELECT '{s}' AS Symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    selects.append(sel)

if selects:
    sql = '\nUNION ALL\n'.join(selects)
    sql = f"SELECT DISTINCT Symbol FROM (\n{sql}\n) as t;"
else:
    sql = "SELECT DISTINCT NULL AS Symbol WHERE false;"

output = {'sql': sql, 'symbols_checked': len(symbols_in_trade_db)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_Xbn6LlMeaJI4TuDuO6U1lrKA': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_call_uujsuC1CCLMoXiLygvLHw84R': 'file_storage/call_uujsuC1CCLMoXiLygvLHw84R.json', 'var_call_NMGGKIDoDKAikS77E1C3am3R': 'file_storage/call_NMGGKIDoDKAikS77E1C3am3R.json', 'var_call_vOvpTPTh22GcZEIT2EmmuKDH': 'file_storage/call_vOvpTPTh22GcZEIT2EmmuKDH.json', 'var_call_uliy6p2kjUKT69HBvTrOr4xu': {'sql': None}}

exec(code, env_args)
