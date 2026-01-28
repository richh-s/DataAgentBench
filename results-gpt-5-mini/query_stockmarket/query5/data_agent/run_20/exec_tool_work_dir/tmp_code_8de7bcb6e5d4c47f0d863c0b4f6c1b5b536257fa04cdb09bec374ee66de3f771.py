code = """import json
# Read the filtered stockinfo->symbols mapping from previous tool result file
with open(var_call_7ayJpBJjIgtxiWcxwSbdLBKo, 'r') as f:
    data = json.load(f)
symbols = data['symbols']

# Build a UNION ALL SQL query to count days in 2019 where (High - Low) > 0.2 * Low for each symbol
selects = []
for s in symbols:
    # Use double quotes around table name to be safe
    sel = f'SELECT "{s}" AS symbol, COUNT(*) AS cnt FROM "{s}" WHERE "Date" >= \"2019-01-01\" AND "Date" <= \"2019-12-31\" AND ("High" - "Low") > 0.2 * "Low"'
    selects.append(sel)

sql = ' UNION ALL '.join(selects) + ' ORDER BY cnt DESC;'

# Print the SQL string as JSON
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_0E5QaHvjoVMRvwUB85CQmhze': 'file_storage/call_0E5QaHvjoVMRvwUB85CQmhze.json', 'var_call_djPIRwcWq4NijOTf6t11m3o0': 'file_storage/call_djPIRwcWq4NijOTf6t11m3o0.json', 'var_call_7ayJpBJjIgtxiWcxwSbdLBKo': 'file_storage/call_7ayJpBJjIgtxiWcxwSbdLBKo.json'}

exec(code, env_args)
