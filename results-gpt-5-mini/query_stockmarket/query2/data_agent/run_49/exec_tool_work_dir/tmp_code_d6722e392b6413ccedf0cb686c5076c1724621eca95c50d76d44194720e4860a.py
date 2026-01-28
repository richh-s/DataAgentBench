code = """import json
with open(var_call_n7eyBtU9JJA5p4IL6Klc9EyV, 'r') as f:
    data = json.load(f)
symbols = data['symbols_to_check']

# Create SQL chunks of ~250 symbols per query
chunk_size = 250
chunks = [symbols[i:i+chunk_size] for i in range(0, len(symbols), chunk_size)]

sqls = []
for chunk in chunks:
    parts = []
    for s in chunk:
        parts.append('SELECT "' + s + '" AS Symbol, Date, "Adj Close" FROM "' + s + '" WHERE Date >= \"2015-01-01\" AND Date <= \"2015-12-31\" AND "Adj Close" > 200')
    sqls.append(' UNION ALL '.join(parts) + ' ORDER BY Symbol, Date;')

# print the first SQL length and how many queries
output = {'num_sqls': len(sqls), 'first_sql_len': len(sqls[0])}
print('__RESULT__:')
print(json.dumps(output))

# Save SQLs to files for manual use outside? but we will now run the first one via query_db in a subsequent tool call.

# Also save the sqls into the storage by writing to files
import os
for idx, sql in enumerate(sqls):
    fname = f"/tmp/sql_chunk_{idx}.sql"
    with open(fname, 'w') as f:
        f.write(sql)

print('__RESULT__:')
print(json.dumps({'files_created': len(sqls)}))"""

env_args = {'var_call_RWOznzhcAB1bqpucDN0isQ8n': 'file_storage/call_RWOznzhcAB1bqpucDN0isQ8n.json', 'var_call_J6gHfxFPYsOEKD6kPD74HU0X': 'file_storage/call_J6gHfxFPYsOEKD6kPD74HU0X.json', 'var_call_n7eyBtU9JJA5p4IL6Klc9EyV': 'file_storage/call_n7eyBtU9JJA5p4IL6Klc9EyV.json', 'var_call_us9VTGKcI5dFIGrFrPcnV5Iq': {'sql_list_count': 8, 'sql_list_sample_first_len': 27652}, 'var_call_E6pzyfJ84827TUyoSs5QQLrT': {'num_sqls': 6}}

exec(code, env_args)
