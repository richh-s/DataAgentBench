code = """import json
# Load the stockinfo ETF list (stored as a JSON file path in var_call_uujsuC1CCLMoXiLygvLHw84R)
with open(var_call_uujsuC1CCLMoXiLygvLHw84R, 'r') as f:
    stockinfo_etfs = json.load(f)
# Load the stocktrade tables list (stored as a JSON file path in var_call_NMGGKIDoDKAikS77E1C3am3R)
with open(var_call_NMGGKIDoDKAikS77E1C3am3R, 'r') as f:
    trade_tables = json.load(f)

# Extract ETF symbols from stockinfo results
etf_symbols = [rec['Symbol'] for rec in stockinfo_etfs]
# Compute intersection with trade tables
symbols_in_trade_db = [s for s in etf_symbols if s in trade_tables]

# Build SQL query that checks each symbol for any Adj Close > 200 during 2015
selects = []
for s in symbols_in_trade_db:
    # Quote table name to be safe
    sel = f"SELECT '{s}' AS Symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
    selects.append(sel)

if selects:
    sql = '\nUNION ALL\n'.join(selects)
    sql = f"SELECT DISTINCT Symbol FROM (\n{sql}\n) as t;"
else:
    sql = "SELECT DISTINCT NULL::VARCHAR AS Symbol WHERE false;"

output = {'sql': sql, 'symbols_to_check_count': len(symbols_in_trade_db)}
import json
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_Xbn6LlMeaJI4TuDuO6U1lrKA': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_call_uujsuC1CCLMoXiLygvLHw84R': 'file_storage/call_uujsuC1CCLMoXiLygvLHw84R.json', 'var_call_NMGGKIDoDKAikS77E1C3am3R': 'file_storage/call_NMGGKIDoDKAikS77E1C3am3R.json'}

exec(code, env_args)
