code = """import json
path = var_call_ag71332u9wgnohnfuiB1TsY7
with open(path,'r') as f:
    obj = json.load(f)
syms_avail = obj['syms_avail']

# build union all in smaller pieces to avoid syntax issues
parts = []
for s in syms_avail:
    parts.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))

# chunk unions
chunks=[]
for i in range(0,len(parts),100):
    chunks.append(" UNION ALL ".join(parts[i:i+100]))

union_all = " UNION ALL ".join(["("+c+")" for c in chunks])
sql = "SELECT symbol, max_adj_close FROM (" + union_all + ") t WHERE max_adj_close > 200 ORDER BY symbol"

print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_rtrl8RNO3l8To1mSqWStympT': 'file_storage/call_rtrl8RNO3l8To1mSqWStympT.json', 'var_call_YeDPrvgXGIqbJWv3usn3iXl3': 'file_storage/call_YeDPrvgXGIqbJWv3usn3iXl3.json', 'var_call_ag71332u9wgnohnfuiB1TsY7': 'file_storage/call_ag71332u9wgnohnfuiB1TsY7.json'}

exec(code, env_args)
