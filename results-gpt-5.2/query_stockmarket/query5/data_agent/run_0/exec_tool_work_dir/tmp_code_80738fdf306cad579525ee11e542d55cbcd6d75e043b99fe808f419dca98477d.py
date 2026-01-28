code = """import json
stockinfo = var_call_SeXupNw6DsT1VNeUn1bKELw8
if isinstance(stockinfo, str):
    with open(stockinfo,'r') as f:
        stockinfo = json.load(f)
trade_tables = var_call_1GnYSdFpnccSXbSJ7xwvth9J
if isinstance(trade_tables, str):
    with open(trade_tables,'r') as f:
        trade_tables = json.load(f)
trade_set = {r['table_name'] for r in trade_tables}
cap_syms = sorted({r['Symbol'] for r in stockinfo}.intersection(trade_set))

# map symbol->company
sym2name = {r['Symbol']: r.get('company_name') or r.get('Company Description') for r in stockinfo}

queries = []
for sym in cap_syms:
    queries.append("SELECT '{sym}' AS Symbol, COUNT(*)::INTEGER AS days_cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(sym=sym))

chunk=40
sqls=[]
for i in range(0,len(queries),chunk):
    union = " UNION ALL ".join(queries[i:i+chunk])
    sqls.append("SELECT Symbol, SUM(days_cnt)::INTEGER AS days_cnt FROM (" + union + ") t GROUP BY Symbol")

print('__RESULT__:')
print(json.dumps({'cap_syms': cap_syms, 'sqls': sqls, 'sym2name': sym2name}))"""

env_args = {'var_call_SeXupNw6DsT1VNeUn1bKELw8': 'file_storage/call_SeXupNw6DsT1VNeUn1bKELw8.json', 'var_call_gpTwhozJJCqsFlGd5pxfoNdo': 'file_storage/call_gpTwhozJJCqsFlGd5pxfoNdo.json', 'var_call_1GnYSdFpnccSXbSJ7xwvth9J': 'file_storage/call_1GnYSdFpnccSXbSJ7xwvth9J.json', 'var_call_lOps8w1NMQeMPVzEnrnKBspg': [{'Symbol': 'AGMH', 'days_cnt': '13'}], 'var_call_Poa1BtcP0bPCKl0338KsDxOu': {'n': 86, 'sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_V0iNv4Dkn9k9JXlBIpJNP0Sl': {'ok': True}, 'var_call_tB216l7OVv3RxW71LvBieNlW': [{'Symbol': 'AGMH', 'days_cnt': '13'}], 'var_call_7GxBgjDEQ5Dm6VsdbwMeilKQ': [{'Symbol': 'ALACU', 'days_cnt': '0'}], 'var_call_e02GVg1qxex3HrPAWflmrlfJ': [{'Symbol': 'AMHC', 'days_cnt': '0'}], 'var_call_p7zl21YvzUz5h3ldaOYqCY6q': [{'Symbol': 'ANDA', 'days_cnt': '0'}], 'var_call_8UvCgx42ZAxXd5rUM5zkPDpC': [{'Symbol': 'APEX', 'days_cnt': '15'}]}

exec(code, env_args)
