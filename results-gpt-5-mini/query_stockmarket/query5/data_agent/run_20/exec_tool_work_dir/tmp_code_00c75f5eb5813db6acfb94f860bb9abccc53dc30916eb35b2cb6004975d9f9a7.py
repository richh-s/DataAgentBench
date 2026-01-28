code = """import json
with open(var_call_7ayJpBJjIgtxiWcxwSbdLBKo, 'r') as f:
    data = json.load(f)
symbols = data['symbols']

# split into two batches
mid = len(symbols)//2
batch1 = symbols[:mid]
batch2 = symbols[mid:]

def make_sql(batch):
    parts = []
    for s in batch:
        parts.append(f'SELECT "{s}" AS symbol, COUNT(*) AS cnt FROM "{s}" WHERE "Date" >= \"2019-01-01\" AND "Date" <= \"2019-12-31\" AND ("High" - "Low") > 0.2 * "Low"')
    return ' UNION ALL '.join(parts) + ' ORDER BY cnt DESC;'

sqls = [make_sql(batch1), make_sql(batch2)]
print("__RESULT__:")
print(json.dumps(sqls))"""

env_args = {'var_call_0E5QaHvjoVMRvwUB85CQmhze': 'file_storage/call_0E5QaHvjoVMRvwUB85CQmhze.json', 'var_call_djPIRwcWq4NijOTf6t11m3o0': 'file_storage/call_djPIRwcWq4NijOTf6t11m3o0.json', 'var_call_7ayJpBJjIgtxiWcxwSbdLBKo': 'file_storage/call_7ayJpBJjIgtxiWcxwSbdLBKo.json', 'var_call_v8BoQ4byq3LbAndnRgRGtWW6': 'file_storage/call_v8BoQ4byq3LbAndnRgRGtWW6.json', 'var_call_9k7cEmQHYN2yAjaZ2Wu7qsw5': 'file_storage/call_9k7cEmQHYN2yAjaZ2Wu7qsw5.json'}

exec(code, env_args)
