code = """import json

# load symbols and info
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

queries = []
for sym in cap_syms:
    q = "SELECT '{sym}' AS Symbol, COUNT(*) AS days_cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2".format(sym=sym)
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n': len(queries)}))"""

env_args = {'var_call_SeXupNw6DsT1VNeUn1bKELw8': 'file_storage/call_SeXupNw6DsT1VNeUn1bKELw8.json', 'var_call_gpTwhozJJCqsFlGd5pxfoNdo': 'file_storage/call_gpTwhozJJCqsFlGd5pxfoNdo.json', 'var_call_1GnYSdFpnccSXbSJ7xwvth9J': 'file_storage/call_1GnYSdFpnccSXbSJ7xwvth9J.json', 'var_call_lOps8w1NMQeMPVzEnrnKBspg': [{'Symbol': 'AGMH', 'days_cnt': '13'}], 'var_call_Poa1BtcP0bPCKl0338KsDxOu': {'n': 86, 'sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
