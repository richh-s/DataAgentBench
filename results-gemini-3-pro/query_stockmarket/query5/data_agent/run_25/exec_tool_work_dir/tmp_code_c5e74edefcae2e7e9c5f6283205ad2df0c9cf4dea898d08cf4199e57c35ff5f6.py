code = """import json

path1 = locals()['var_function-call-15016460926965200659']
path2 = locals()['var_function-call-570738584850609366']

with open(path1, 'r') as f:
    d1 = json.load(f)
    
s_set = set()
for x in d1:
    s_set.add(x['Symbol'])

with open(path2, 'r') as f:
    d2 = json.load(f)

valid = []
for s in d2:
    if s in s_set:
        valid.append(s)

sqls = []
for s in valid:
    # Use format to avoid concatenation errors
    # Query: SELECT 'SYM' as Symbol, COUNT(*) as cnt FROM "SYM" WHERE ...
    q = "SELECT '{0}' as Symbol, COUNT(*) as cnt FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low".format(s)
    sqls.append(q)

final_q = ""
if len(sqls) > 0:
    final_q = " UNION ALL ".join(sqls)
    final_q = final_q + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
# Print the query string. If it's huge, it will be stored in a file.
print(json.dumps(final_q))"""

env_args = {'var_function-call-15016460926965200659': 'file_storage/function-call-15016460926965200659.json', 'var_function-call-570738584850609366': 'file_storage/function-call-570738584850609366.json', 'var_function-call-533584454606138071': 'file_storage/function-call-533584454606138071.json'}

exec(code, env_args)
