code = """import json

path1 = locals()['var_function-call-15016460926965200659']
path2 = locals()['var_function-call-570738584850609366']

with open(path1, 'r') as f:
    d1 = json.load(f)
s_set = set(x['Symbol'] for x in d1)

with open(path2, 'r') as f:
    d2 = json.load(f)
valid = [s for s in d2 if s in s_set]

sqls = []
for s in valid:
    # Construct query parts
    # SELECT 'SYM' as Symbol, COUNT(*) as cnt FROM "SYM" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low
    
    # We build it safely
    part1 = "SELECT '" + s + "' as Symbol, COUNT(*) as cnt FROM "
    part2 = '"' + s + '"'
    part3 = " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
    
    sqls.append(part1 + part2 + part3)

final_q = ""
if sqls:
    final_q = " UNION ALL ".join(sqls) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-15016460926965200659': 'file_storage/function-call-15016460926965200659.json', 'var_function-call-570738584850609366': 'file_storage/function-call-570738584850609366.json', 'var_function-call-533584454606138071': 'file_storage/function-call-533584454606138071.json'}

exec(code, env_args)
