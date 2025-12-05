code = """import json

with open(var_call_OSNNOYm0lqN4WogObQE3LcKG, 'r') as f:
    data = json.load(f)
chunks = data['chunks']

queries = []
for chunk in chunks:
    symbols_list = ', '.join([f'"{s}"' for s in chunk])
    q = f"SELECT symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM (" + " UNION ALL ".join([f'SELECT "Adj Close", \"{s}\" as symbol FROM \"{s}\" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\'' for s in chunk]) + ") GROUP BY symbol HAVING max_adj_close_2015 > 200;"
    queries.append(q)

print("__RESULT__:")
print(json.dumps({"num_queries": len(queries), "first_query": queries[0]}))"""

env_args = {'var_call_hIL8Xy8C1hmn7bVZNvodAPez': 'file_storage/call_hIL8Xy8C1hmn7bVZNvodAPez.json', 'var_call_YK1NgylmpGBizcdp2FJuJkJI': 'file_storage/call_YK1NgylmpGBizcdp2FJuJkJI.json', 'var_call_OSNNOYm0lqN4WogObQE3LcKG': 'file_storage/call_OSNNOYm0lqN4WogObQE3LcKG.json', 'var_call_9Fvj2ltwIzkxt1FMgcTojwmt': {'num_chunks': 29, 'first_chunk': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
