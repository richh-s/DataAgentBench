code = """import json
p1 = var_call_1d7c5AowR62QJgtP4olPNN6Q
p2 = var_call_p7naLRdF4ukJrrkgYysxWr3r
with open(p1,'r') as f:
    stockinfo = json.load(f)
with open(p2,'r') as f:
    tradetables = json.load(f)
symbols_stockinfo = [r['Symbol'] for r in stockinfo]
symbols_trade = set(tradetables)
intersection = sorted([s for s in symbols_stockinfo if s in symbols_trade])
# build SQL union
selects = []
for s in intersection:
    tbl = s
    # double-quote table name
    sel = f'SELECT "{tbl}" AS symbol, SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down_days FROM "{tbl}" WHERE "Date">='"'2017-01-01'"' AND "Date"<='"'2017-12-31'"''
    selects.append(sel)
sql = '\nUNION ALL\n'.join(selects)
sql = 'SELECT symbol, up_days, down_days FROM (\n' + sql + '\n) WHERE up_days>down_days ORDER BY up_days DESC LIMIT 5;'
out = {'num_symbols': len(intersection), 'sql_preview_len': len(sql), 'sql_first_1000': sql[:1000]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1d7c5AowR62QJgtP4olPNN6Q': 'file_storage/call_1d7c5AowR62QJgtP4olPNN6Q.json', 'var_call_p7naLRdF4ukJrrkgYysxWr3r': 'file_storage/call_p7naLRdF4ukJrrkgYysxWr3r.json', 'var_call_vJHhpJtUjdPfYk3kx6niCwRC': {'count_intersection': 234, 'symbols_sample_first_50': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}}

exec(code, env_args)
