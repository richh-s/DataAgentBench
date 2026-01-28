code = """import json
# Load ETF symbols and available trade tables from previous calls
path_etfs = var_call_Jmo2Rsfw5M21fWP4GV1aAB4V
path_tables = var_call_0iEfjRTHDhO80I1pTTWbbo9M
with open(path_etfs, 'r') as f:
    etf_symbols = json.load(f)
with open(path_tables, 'r') as f:
    trade_tables = json.load(f)
# Intersection of ETFs that have trade tables
symbols = [s for s in etf_symbols if s in trade_tables]
selects = []
for s in symbols:
    # Build a select that returns the symbol if any 2015 adj close > 200
    sel = "SELECT '{}' AS Symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s, s)
    selects.append(sel)
if selects:
    sql = 'SELECT Symbol FROM (\n' + '\nUNION ALL\n'.join(selects) + '\n) t;'
else:
    sql = "SELECT '' AS Symbol WHERE 1=0;"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_gCLBSTPQ665qBJjIJTfQJYcH': 'file_storage/call_gCLBSTPQ665qBJjIJTfQJYcH.json', 'var_call_Jmo2Rsfw5M21fWP4GV1aAB4V': 'file_storage/call_Jmo2Rsfw5M21fWP4GV1aAB4V.json', 'var_call_0iEfjRTHDhO80I1pTTWbbo9M': 'file_storage/call_0iEfjRTHDhO80I1pTTWbbo9M.json'}

exec(code, env_args)
