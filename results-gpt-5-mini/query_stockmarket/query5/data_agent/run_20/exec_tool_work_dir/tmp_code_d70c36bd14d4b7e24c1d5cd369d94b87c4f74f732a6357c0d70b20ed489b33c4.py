code = """import json
# Load the SQL query string from previous result file
with open(var_call_v8BoQ4byq3LbAndnRgRGtWW6, 'r') as f:
    sql = json.load(f)

# Because the SQL is very long, we'll split into batches to avoid exceeding query size limits.
# Split by ' UNION ALL ' into individual SELECTs
parts = sql.split(' UNION ALL ')

# We'll run in batches of 200 selects
batches = [parts[i:i+200] for i in range(0, len(parts), 200)]
results = []
import math

for batch in batches:
    batch_sql = ' UNION ALL '.join(batch) + ' ORDER BY cnt DESC;'
    res = __call__("functions.query_db", {"db_name": "stocktrade_database", "query": batch_sql})
    # store results from the tool call
    results.append(res)

# Save results to a temp file and print path
with open('/tmp/batch_results.json', 'w') as f:
    json.dump(results, f)

print("__RESULT__:")
print(json.dumps('/tmp/batch_results.json'))"""

env_args = {'var_call_0E5QaHvjoVMRvwUB85CQmhze': 'file_storage/call_0E5QaHvjoVMRvwUB85CQmhze.json', 'var_call_djPIRwcWq4NijOTf6t11m3o0': 'file_storage/call_djPIRwcWq4NijOTf6t11m3o0.json', 'var_call_7ayJpBJjIgtxiWcxwSbdLBKo': 'file_storage/call_7ayJpBJjIgtxiWcxwSbdLBKo.json', 'var_call_v8BoQ4byq3LbAndnRgRGtWW6': 'file_storage/call_v8BoQ4byq3LbAndnRgRGtWW6.json'}

exec(code, env_args)
