code = """import json
p1 = locals()['var_function-call-13405563423262500002']
p2 = locals()['var_function-call-13405563423262501427']
with open(p1, 'r') as f: i_data = json.load(f)
with open(p2, 'r') as f: t_data = json.load(f)

t_set = set(t_data)
valid = [x['Symbol'] for x in i_data if x['Symbol'] in t_set]

test_valid = valid[:5]
parts = []
for s in test_valid:
    q = "SELECT '{0}' as Symbol, COUNT(*) as Days FROM \"{0}\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)".format(s)
    parts.append(q)

full = " UNION ALL ".join(parts)
final = "SELECT Symbol, Days FROM (" + full + ") ORDER BY Days DESC"

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_function-call-13405563423262500002': 'file_storage/function-call-13405563423262500002.json', 'var_function-call-13405563423262501427': 'file_storage/function-call-13405563423262501427.json', 'var_function-call-7452566899761960412': 'file_storage/function-call-7452566899761960412.json', 'var_function-call-3890797748317389803': 'file_storage/function-call-3890797748317389803.json', 'var_function-call-18275851553321309294': "SELECT Symbol, Days FROM (SELECT 'AGMH' as Symbol, COUNT(*) as Days FROM  + s +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as Days FROM  + s +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as Days FROM  + s +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ANDA' as Symbol, COUNT(*) as Days FROM  + s +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low) UNI"}

exec(code, env_args)
