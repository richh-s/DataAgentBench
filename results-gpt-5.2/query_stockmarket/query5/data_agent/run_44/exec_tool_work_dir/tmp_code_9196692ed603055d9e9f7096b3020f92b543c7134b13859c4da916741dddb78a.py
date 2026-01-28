code = """import json, pandas as pd

# load symbols & names
with open(var_call_4aGwTzh70bt8xarEObPHR1xp, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_ptTAFVhG5hNvbNHxEpsBJBbz, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

info_df = info_df[info_df['Symbol'].isin(tables_set)].copy()
syms = info_df['Symbol'].tolist()

# chunk to avoid huge SQL
chunk_size = 200
chunks = [syms[i:i+chunk_size] for i in range(0, len(syms), chunk_size)]

queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        parts.append("SELECT '{s}' AS Symbol, COUNT(*)::BIGINT AS days FROM \"{s}\" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND Low > 0 AND High > 1.2*Low".format(s=sym))
    q = "SELECT Symbol, days FROM (" + " UNION ALL ".join(parts) + ") t"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'n_chunks': len(chunks), 'first_query_preview': queries[0][:500]}))"""

env_args = {'var_call_4aGwTzh70bt8xarEObPHR1xp': 'file_storage/call_4aGwTzh70bt8xarEObPHR1xp.json', 'var_call_ptTAFVhG5hNvbNHxEpsBJBbz': 'file_storage/call_ptTAFVhG5hNvbNHxEpsBJBbz.json', 'var_call_SyGavGLV4s4xf2xrjw3y2Oxj': [{'ok': '1'}], 'var_call_FJJXnZfewVba9mByDiy69JB4': [{'Date': '2018-04-18', 'Open': '5.75', 'High': '7.5', 'Low': '5.010000228881836', 'Close': '6.300000190734863', 'Adj Close': '6.300000190734863', 'Volume': '291800'}], 'var_call_pM5XfJD5vwc9WGvZ3VtqjrlV': [{'Symbol': 'AGMH', 'days': '13'}], 'var_call_bxQ94D76MCpgJLzhH0fEHW9Z': {'ok': True}, 'var_call_6HtbLlXYKQVzRe8rcIfFmab9': {'s': 'abc'}, 'var_call_wyXHp1gi3FGX4G6jMoTnDHYP': [{'Symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}], 'var_call_McFkmzP0Ev3R48Pm0NNQmcdZ': [{'Symbol': 'AGMH', 'days': '13'}, {'Symbol': 'BCLI', 'days': '0'}]}

exec(code, env_args)
