code = """import json, pandas as pd

info = var_call_wgw92BVAntb683am8PU9CuoP
if isinstance(info, str):
    with open(info, 'r') as f:
        info = json.load(f)
trade_tables = var_call_1ua2Y7QX3q0bbYnH7DZgKC2b
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

etf_symbols = sorted(set(pd.DataFrame(info)['symbol']).intersection(trade_tables))
chunks = [etf_symbols[i:i+200] for i in range(0, len(etf_symbols), 200)]
queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        parts.append("SELECT '{s}' AS symbol, MAX(Adj Close) AS max_adj_close FROM {s} WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'".format(s=sym))
    q = "SELECT symbol, max_adj_close FROM (" + " UNION ALL ".join(parts) + ") t WHERE max_adj_close > 200"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'num_chunks': len(queries), 'first_len': len(queries[0]), 'last_len': len(queries[-1])}))"""

env_args = {'var_call_wgw92BVAntb683am8PU9CuoP': 'file_storage/call_wgw92BVAntb683am8PU9CuoP.json', 'var_call_1ua2Y7QX3q0bbYnH7DZgKC2b': 'file_storage/call_1ua2Y7QX3q0bbYnH7DZgKC2b.json', 'var_call_LcZdQORHsdFywW8kfXLs8ogr': {'test': 'ok'}, 'var_call_Xfvd67ZxRXS1nJxPeBIqrjpb': 'file_storage/call_Xfvd67ZxRXS1nJxPeBIqrjpb.json', 'var_call_s7asqScoZqD7HnSZF7Y06mHX': [], 'var_call_ZrZYcvabocduQmgMH4vatf0f': {'num_candidate_etfs': 1435, 'num_needs_quote': 0, 'examples_needs_quote': []}, 'var_call_SFsbIn2KwZiDjqoJJ6QNACzW': {'num_candidate_etfs': 1435, 'num_chunks': 10, 'first_query_len': 18851, 'first_query_preview': "SELECT symbol, max_adj_close FROM (SELECT 'AAAU' AS symbol, MAX(Adj Close) AS max_adj_close FROM AAAU WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' UNION ALL SELECT 'AADR' AS symbol, MAX(Adj Close) AS max_adj_close FROM AADR WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' UNION ALL SELECT 'ABEQ' AS symbol, MAX(Adj Close) AS max_adj_close FROM ABEQ WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' UNION ALL SELECT 'ACSG' AS symbol, MAX(Adj Close) AS max_adj_close FROM ACSG WHERE Date BETWEEN '"}, 'var_call_1CCpFNKRgGMYxxYZ5UwyTiKk': [], 'var_call_s1PFlFTa6SEiyQ96e0iZrsDi': {'num_etfs_arca': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_tRJQFFjbKjnhjUBO8rYbeYZW': [{'max_adj_close': '193.3121490478516'}], 'var_call_vNV9nwEi11qUiFxkDQrSWa4o': [{'max_adj_close': '131.44960021972656'}], 'var_call_SDPDZw1RqgZuhe8GH4IfWx5M': [{'max_adj_close': '125.2300033569336'}], 'var_call_m3vGuErKuMXfxXv5Fw2kPxoY': [{'max_adj_close': '121.58584594726562'}], 'var_call_W3rSHV1rg70HmyKBgJOeGaUi': [{'max_adj_close': '163.6190185546875'}], 'var_call_MtjQnNf0K7cVZcEDkQGruOo2': {'num_candidate_etfs': 1435, 'num_chunks': 10, 'first_query_len': 18851, 'first_query_preview': "SELECT symbol, max_adj_close FROM (SELECT 'AAAU' AS symbol, MAX(Adj Close) AS max_adj_close FROM AAAU WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' UNION ALL SELECT 'AADR' AS symbol, MAX(Adj Close) AS max_adj_close FROM AADR WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' UNION ALL SELECT 'ABEQ' AS symbol, MAX(Adj Close) AS max_adj_close FROM ABEQ WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' UNION ALL SELECT 'ACSG' AS symbol, MAX(Adj Close) AS max_adj_close FROM ACSG WHERE Date BETWEEN '"}}

exec(code, env_args)
