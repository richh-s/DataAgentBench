code = """import json

p = var_call_UwpHvTHhKmFFho4uRXrrlDB9
with open(p,'r') as f:
    d = json.load(f)

symbols = d['symbols_in_both']
parts = []
for s in symbols:
    t = '"' + s.replace('"','""') + '"'
    parts.append("SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM " + t + " WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

union_query = "\nUNION ALL\n".join(parts)
final_query = "SELECT Symbol, max_adj_close_2015 FROM (\n" + union_query + "\n) WHERE max_adj_close_2015 > 200 ORDER BY Symbol;"

print('__RESULT__:')
print(json.dumps({'query': final_query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_sk5XKsNrqckiS1jjOTMbwfDa': 'file_storage/call_sk5XKsNrqckiS1jjOTMbwfDa.json', 'var_call_wUZv4P1r1qG7d8sTKMa3SlIi': 'file_storage/call_wUZv4P1r1qG7d8sTKMa3SlIi.json', 'var_call_UwpHvTHhKmFFho4uRXrrlDB9': 'file_storage/call_UwpHvTHhKmFFho4uRXrrlDB9.json', 'var_call_5pWrO0RncV5IEKbmdFJ0TdmL': 'file_storage/call_5pWrO0RncV5IEKbmdFJ0TdmL.json'}

exec(code, env_args)
