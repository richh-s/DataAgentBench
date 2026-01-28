code = """import json, pandas as pd

# load nyse non-etf symbols
src = var_call_gYJbskZiMLDqMqhJmUIqMw5P
nyse_rows = json.load(open(src)) if isinstance(src,str) else src
nyse = pd.DataFrame(nyse_rows)

# load trade table names
src2 = var_call_3AGovKZPBrPjNydrZXEKhl8p
trade_rows = json.load(open(src2)) if isinstance(src2,str) else src2
trade = pd.DataFrame(trade_rows)

# candidates
cands = sorted(set(nyse['Symbol']).intersection(set(trade['table_name'])))

# chunk into groups of 25 to keep SQL manageable
chunks = [cands[i:i+25] for i in range(0,len(cands),25)]

queries = []
for ch in chunks:
    parts=[]
    for s in ch:
        tbl='"'+s.replace('"','""')+'"'
        parts.append("SELECT '{sym}' AS Symbol, SUM(CASE WHEN Date>='2017-01-01' AND Date<'2018-01-01' AND Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Date>='2017-01-01' AND Date<'2018-01-01' AND Close<Open THEN 1 ELSE 0 END) AS down_days FROM {tbl}".format(sym=s,tbl=tbl))
    queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'candidate_count': len(cands), 'chunk_count': len(queries), 'first_chunk_sql': queries[0]}))"""

env_args = {'var_call_gYJbskZiMLDqMqhJmUIqMw5P': 'file_storage/call_gYJbskZiMLDqMqhJmUIqMw5P.json', 'var_call_yC5xzU04KLrHiVtr69INvnjw': 'file_storage/call_yC5xzU04KLrHiVtr69INvnjw.json', 'var_call_QMPBqXPWLwySAtjtee9Dfswo': [{'ok': '1'}], 'var_call_thxfhxgNSq8k5FJe15SsP7jX': 'ok', 'var_call_hc4U3LZxcsHuRmDa5rqsakaf': "SELECT 'A' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days FROM ", 'var_call_PiWIfet4rL88PmAUCQowq6SY': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_3AGovKZPBrPjNydrZXEKhl8p': 'file_storage/call_3AGovKZPBrPjNydrZXEKhl8p.json', 'var_call_mgSxAdDmGnBoXPwD8MLfXvPY': [{'up_days': '111.0', 'down_days': '136.0'}]}

exec(code, env_args)
