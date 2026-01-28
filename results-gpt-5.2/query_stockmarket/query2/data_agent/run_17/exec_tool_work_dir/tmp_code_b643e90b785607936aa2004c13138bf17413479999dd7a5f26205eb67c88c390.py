code = """import json
p = var_call_Bfz9N9zfoJmlwqpZohglpiFe
# this is already a dict
values_sql = p['values_sql_preview'] if isinstance(p, dict) else None

# reconstruct full values_sql
p_full = var_call_iOvFCGkDaV3qO2tUthxmFcC2
if isinstance(p_full, str):
    with open(p_full,'r') as f:
        etfs = json.load(f)
else:
    etfs = p_full
sym_desc = {r['Symbol']: r.get('company_description') for r in etfs}

p2 = var_call_yb7NMQCKe3VpgSr6Ll3fPIXi
if isinstance(p2, str):
    with open(p2,'r') as f:
        tables = json.load(f)
else:
    tables = p2
trade_set = set([r['table_name'] for r in tables])
syms = sorted([s for s in sym_desc if s in trade_set])

values_sql = ','.join(["('"+s.replace("'","''")+"')" for s in syms])

query = """
WITH etf_syms(Symbol) AS (VALUES {values}),
per_symbol AS (
  SELECT s.Symbol,
         (SELECT MAX(\"Adj Close\") FROM query_table(s.Symbol)
          WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01') AS max_adj_close_2015
  FROM etf_syms s
)
SELECT Symbol, max_adj_close_2015
FROM per_symbol
WHERE max_adj_close_2015 > 200
ORDER BY Symbol;
""".format(values=values_sql)

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_iOvFCGkDaV3qO2tUthxmFcC2': 'file_storage/call_iOvFCGkDaV3qO2tUthxmFcC2.json', 'var_call_PJXWtX99zzhlp0cs6kTsGt48': 'file_storage/call_PJXWtX99zzhlp0cs6kTsGt48.json', 'var_call_RectN9RWDgCsxQrjTdI0Ybp0': {'n_syms': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_yb7NMQCKe3VpgSr6Ll3fPIXi': 'file_storage/call_yb7NMQCKe3VpgSr6Ll3fPIXi.json', 'var_call_hZy9NLepwdEqLRpFMwlmH9jt': [{'Symbol': 'AAAU'}], 'var_call_Bfz9N9zfoJmlwqpZohglpiFe': {'values_sql_len': 12364, 'n_syms': 1435, 'values_sql_preview': "('AAAU'),('AADR'),('ABEQ'),('ACSG'),('ACWF'),('AFK'),('AFLG'),('AFMC'),('AFSM'),('AFTY'),('AGG'),('AGGP'),('AGGY'),('AGQ'),('AGZ'),('AIEQ'),('AIIQ'),('AMLP'),('AMOM'),('AMZA'),('AOA'),('AOK'),('AOM'),"}, 'var_call_9b3Q3tHLMRY46I6KZuPUplKm': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}]}

exec(code, env_args)
