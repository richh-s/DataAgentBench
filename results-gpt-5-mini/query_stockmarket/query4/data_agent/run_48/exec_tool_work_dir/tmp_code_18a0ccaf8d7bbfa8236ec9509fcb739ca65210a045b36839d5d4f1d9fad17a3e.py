code = """import json
# Load the results from previous tool calls
with open(var_call_pyOoEGpOxhNwP3LyQHJlWoSD, 'r') as f:
    stockinfo_rows = json.load(f)
with open(var_call_TfPSbNGVVQC96WKbJa5JME5v, 'r') as f:
    table_list = json.load(f)

# Extract symbols present in both
table_set = set(table_list)
filtered = []
for r in stockinfo_rows:
    sym = r.get('Symbol')
    if sym in table_set:
        filtered.append({'Symbol': sym, 'Company Description': r.get('Company Description')})

import json
print("__RESULT__:")
print(json.dumps(filtered))"""

env_args = {'var_call_pyOoEGpOxhNwP3LyQHJlWoSD': 'file_storage/call_pyOoEGpOxhNwP3LyQHJlWoSD.json', 'var_call_TfPSbNGVVQC96WKbJa5JME5v': 'file_storage/call_TfPSbNGVVQC96WKbJa5JME5v.json'}

exec(code, env_args)
