code = """import json
# Build SQL in chunks to avoid syntax issues
common_path = var_call_mCqsIFNoyoK2lFXc52KnIQg8
with open(common_path, 'r') as f:
    common = json.load(f)
# We'll prepare SQL that unions SELECTs; but DuckDB may have many tables; to avoid too long queries, limit per batch
batch_size = 200
batches = [common[i:i+batch_size] for i in range(0, len(common), batch_size)]
sql_batches = []
for batch in batches:
    selects = []
    for s in batch:
        sel = f"SELECT '{s}' AS Symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        selects.append(sel)
    sql = 'SELECT Symbol FROM (\n' + '\nUNION ALL\n'.join(selects) + '\n) t;'
    sql_batches.append(sql)
print('__RESULT__:')
print(json.dumps(sql_batches))"""

env_args = {'var_call_gCLBSTPQ665qBJjIJTfQJYcH': 'file_storage/call_gCLBSTPQ665qBJjIJTfQJYcH.json', 'var_call_Jmo2Rsfw5M21fWP4GV1aAB4V': 'file_storage/call_Jmo2Rsfw5M21fWP4GV1aAB4V.json', 'var_call_0iEfjRTHDhO80I1pTTWbbo9M': 'file_storage/call_0iEfjRTHDhO80I1pTTWbbo9M.json', 'var_call_mCqsIFNoyoK2lFXc52KnIQg8': 'file_storage/call_mCqsIFNoyoK2lFXc52KnIQg8.json'}

exec(code, env_args)
