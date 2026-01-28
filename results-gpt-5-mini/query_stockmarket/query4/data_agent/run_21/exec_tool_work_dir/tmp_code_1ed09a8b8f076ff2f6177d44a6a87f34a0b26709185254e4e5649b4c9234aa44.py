code = """import json
with open(var_call_rRmEOQdBJdvZ2MWsGvcVRR1D, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_TNNo3PG04ccYq62LaQbnWW9w, 'r') as f:
    trade_tables = json.load(f)
symbols = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)
symbols_in_trade = [s for s in symbols if s in trade_set]
parts = []
for s in symbols_in_trade:
    tbl = '"' + s.replace('"', '""') + '"'
    safe_s = s.replace("'", "''")
    part = ("SELECT '{sym}' AS symbol, "
            "SUM(CASE WHEN \"Close\">\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) AS up, "
            "SUM(CASE WHEN \"Close\"<\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) AS down "
            "FROM {tbl}").format(sym=safe_s, tbl=tbl)
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts)
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_rRmEOQdBJdvZ2MWsGvcVRR1D': 'file_storage/call_rRmEOQdBJdvZ2MWsGvcVRR1D.json', 'var_call_TNNo3PG04ccYq62LaQbnWW9w': 'file_storage/call_TNNo3PG04ccYq62LaQbnWW9w.json'}

exec(code, env_args)
