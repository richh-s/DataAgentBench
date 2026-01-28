code = """import json
with open(var_call_h7weTyR1OHJUYmUz3zTOdl67, 'r') as f:
    symbols = json.load(f)
# batch size
batch_size = 100
sql_list = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        parts.append("SELECT '{}' AS Symbol, (SELECT MAX(\"Adj Close\") FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31') AS max_adj".format(s, s))
    sql = "SELECT Symbol FROM (" + " UNION ALL ".join(parts) + ") AS t WHERE max_adj > 200 ORDER BY Symbol;"
    sql_list.append(sql)
print("__RESULT__:")
print(json.dumps(sql_list))"""

env_args = {'var_call_tRlSKUeszajxFebpOVmuqsde': ['stockinfo'], 'var_call_DG0vN5pLFilWu9tTK6nlcgSy': 'file_storage/call_DG0vN5pLFilWu9tTK6nlcgSy.json', 'var_call_UpFSKAxq4enQyFMneNysTLNi': 'file_storage/call_UpFSKAxq4enQyFMneNysTLNi.json', 'var_call_kkqKOJniybxDUtWEO6yDgShT': 'file_storage/call_kkqKOJniybxDUtWEO6yDgShT.json', 'var_call_h7weTyR1OHJUYmUz3zTOdl67': 'file_storage/call_h7weTyR1OHJUYmUz3zTOdl67.json', 'var_call_jQ3Ior45LCV2Zl5R1U39TK2X': [], 'var_call_lZ8Ds29T4XA3QxaViNpnYAa9': 1435, 'var_call_yeWf6Yo30qtS5OWMbBhN67xN': [{'max_adj': '193.3121490478516'}]}

exec(code, env_args)
