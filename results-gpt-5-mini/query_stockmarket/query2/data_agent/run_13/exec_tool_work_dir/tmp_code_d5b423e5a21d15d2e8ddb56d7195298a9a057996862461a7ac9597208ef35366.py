code = """import json
path = var_call_mCqsIFNoyoK2lFXc52KnIQg8
with open(path, 'r') as f:
    common = json.load(f)
batch_size = 200
batches = [common[i:i+batch_size] for i in range(0, len(common), batch_size)]
sqls = []
for batch in batches:
    selects = []
    for s in batch:
        selects.append("SELECT '{}' AS Symbol FROM \"{}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s, s))
    sql = 'SELECT Symbol FROM (\\n' + '\\nUNION ALL\\n'.join(selects) + '\\n) t;'
    sqls.append(sql)
print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_gCLBSTPQ665qBJjIJTfQJYcH': 'file_storage/call_gCLBSTPQ665qBJjIJTfQJYcH.json', 'var_call_Jmo2Rsfw5M21fWP4GV1aAB4V': 'file_storage/call_Jmo2Rsfw5M21fWP4GV1aAB4V.json', 'var_call_0iEfjRTHDhO80I1pTTWbbo9M': 'file_storage/call_0iEfjRTHDhO80I1pTTWbbo9M.json', 'var_call_mCqsIFNoyoK2lFXc52KnIQg8': 'file_storage/call_mCqsIFNoyoK2lFXc52KnIQg8.json'}

exec(code, env_args)
