code = """import json
stockinfo = json.load(open(var_call_PD6sCKvQPl7XG930NCaPdWBb, 'r'))
trade_tables = json.load(open(var_call_KBnUpk3gZ8X5OUAmIGU1w97y, 'r'))
etf_symbols = [rec['Symbol'] for rec in stockinfo]
trade_tables_set = set(trade_tables)
symbols_to_check = [s for s in etf_symbols if s in trade_tables_set]

parts = []
for s in symbols_to_check:
    part = "SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)

if parts:
    union_sql = ' UNION ALL '.join(parts)
    sql = 'SELECT Symbol, max_adj FROM ( ' + union_sql + ' ) WHERE max_adj > 200;'
else:
    sql = "SELECT '' AS Symbol, NULL AS max_adj WHERE 1=0;"

out = {'sql': sql, 'symbols_count': len(symbols_to_check)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PD6sCKvQPl7XG930NCaPdWBb': 'file_storage/call_PD6sCKvQPl7XG930NCaPdWBb.json', 'var_call_KBnUpk3gZ8X5OUAmIGU1w97y': 'file_storage/call_KBnUpk3gZ8X5OUAmIGU1w97y.json', 'var_call_fpbnOjfeUPKdqEF9qV9H4SSo': {'count': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
