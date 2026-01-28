code = """import json
with open(var_call_7ayJpBJjIgtxiWcxwSbdLBKo, 'r') as f:
    data = json.load(f)
symbols = data['symbols']

selects = []
for s in symbols:
    sel = f'SELECT "{s}" AS symbol, COUNT(*) AS cnt FROM "{s}" WHERE "Date" >= \"2019-01-01\" AND "Date" <= \"2019-12-31\" AND ("High" - "Low") > 0.2 * "Low"'
    selects.append(sel)

# create batches of 100
batch_size = 100
batches = [selects[i:i+batch_size] for i in range(0, len(selects), batch_size)]
batch_sqls = []
for batch in batches:
    sql = ' UNION ALL '.join(batch) + ' ORDER BY cnt DESC;'
    batch_sqls.append(sql)

print("__RESULT__:")
print(json.dumps(batch_sqls))"""

env_args = {'var_call_0E5QaHvjoVMRvwUB85CQmhze': 'file_storage/call_0E5QaHvjoVMRvwUB85CQmhze.json', 'var_call_djPIRwcWq4NijOTf6t11m3o0': 'file_storage/call_djPIRwcWq4NijOTf6t11m3o0.json', 'var_call_7ayJpBJjIgtxiWcxwSbdLBKo': 'file_storage/call_7ayJpBJjIgtxiWcxwSbdLBKo.json', 'var_call_v8BoQ4byq3LbAndnRgRGtWW6': 'file_storage/call_v8BoQ4byq3LbAndnRgRGtWW6.json'}

exec(code, env_args)
