code = """import json

stockinfo = var_call_SeXupNw6DsT1VNeUn1bKELw8
if isinstance(stockinfo, str):
    with open(stockinfo, 'r') as f:
        stockinfo = json.load(f)

trade_tables = var_call_1GnYSdFpnccSXbSJ7xwvth9J
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

trade_set = {r['table_name'] for r in trade_tables}
cap_syms = sorted({r['Symbol'] for r in stockinfo}.intersection(trade_set))

parts = []
for sym in cap_syms[:5]:
    parts.append(
        "SELECT '{sym}' AS Symbol, COUNT(*) AS days_cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2".format(sym=sym)
    )

q = "SELECT Symbol, SUM(days_cnt) AS days_cnt FROM (" + " UNION ALL ".join(parts) + ") t GROUP BY Symbol"

print('__RESULT__:')
print(json.dumps({'q': q}))"""

env_args = {'var_call_SeXupNw6DsT1VNeUn1bKELw8': 'file_storage/call_SeXupNw6DsT1VNeUn1bKELw8.json', 'var_call_gpTwhozJJCqsFlGd5pxfoNdo': 'file_storage/call_gpTwhozJJCqsFlGd5pxfoNdo.json', 'var_call_1GnYSdFpnccSXbSJ7xwvth9J': 'file_storage/call_1GnYSdFpnccSXbSJ7xwvth9J.json', 'var_call_lOps8w1NMQeMPVzEnrnKBspg': [{'Symbol': 'AGMH', 'days_cnt': '13'}]}

exec(code, env_args)
