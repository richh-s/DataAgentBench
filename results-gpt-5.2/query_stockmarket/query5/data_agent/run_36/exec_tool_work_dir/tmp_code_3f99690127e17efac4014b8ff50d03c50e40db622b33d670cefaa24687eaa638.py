code = """import json
path_info = var_call_3V4pDyazC1sjaV9hP91bTGvn
with open(path_info,'r',encoding='utf-8') as f:
    info = json.load(f)
syms = [r['Symbol'] for r in info if r.get('Symbol')]

chunk_size = 40
queries = []
for i in range(0, len(syms), chunk_size):
    ch = syms[i:i+chunk_size]
    parts = []
    for s in ch:
        parts.append("SELECT '{}' AS Symbol, COUNT(*) AS days_over_20pct FROM \"{}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(s, s))
    q = 'SELECT Symbol, days_over_20pct FROM (' + ' UNION ALL '.join(parts) + ') t'
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_chunks': len(queries), 'sample_query': queries[0][:500]}))"""

env_args = {'var_call_3V4pDyazC1sjaV9hP91bTGvn': 'file_storage/call_3V4pDyazC1sjaV9hP91bTGvn.json', 'var_call_qOs1fzOEpiJx3S8lGuMBNaoX': 'file_storage/call_qOs1fzOEpiJx3S8lGuMBNaoX.json', 'var_call_hO8l2lcmHa3DyjwriKzvGDOb': [{'n': '493'}], 'var_call_aSvXQY3yfOBY2wQF9AdCjif5': [{'n': '361'}], 'var_call_MPClvZIbTUZ4zi5BLQXQFq6b': [{'n': '4150'}], 'var_call_YlB2fxK7ASBfuCwMMGsbgVZc': {'ok': True}, 'var_call_UDFmuRH1ztuAxZ3A0qwTOR6k': [{'Symbol': 'AGMH', 'days_over_20pct': '13'}, {'Symbol': 'ALACU', 'days_over_20pct': '0'}]}

exec(code, env_args)
