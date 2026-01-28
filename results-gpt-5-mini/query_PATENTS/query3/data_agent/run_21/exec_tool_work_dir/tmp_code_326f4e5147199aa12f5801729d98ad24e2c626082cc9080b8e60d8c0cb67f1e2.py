code = """import json
results = json.load(open(var_call_P6u7UTLjRT3xZAh6jMePdi59, 'r'))
# Filter out entries with empty titleFull
filtered = [r for r in results if r.get('titleFull')]
# Format as simple list of "Assignee — Title"
out_lines = [f"{r['assignee']} — {r['titleFull']}" for r in filtered]
print('__RESULT__:')
print(json.dumps(out_lines))"""

env_args = {'var_call_FWaq87obpvltPwUmTRpRaycV': 'file_storage/call_FWaq87obpvltPwUmTRpRaycV.json', 'var_call_xPULEoxuCI0R7gn4s9WmVLxr': 'file_storage/call_xPULEoxuCI0R7gn4s9WmVLxr.json', 'var_call_tgrM8QNXraQ65lKZy8S0oDdF': 'file_storage/call_tgrM8QNXraQ65lKZy8S0oDdF.json', 'var_call_HmYwVsetvOZ1SrWOkNrDbW1h': 'file_storage/call_HmYwVsetvOZ1SrWOkNrDbW1h.json', 'var_call_uwJ71UCjoN6nJceaFvGl4TYY': 'file_storage/call_uwJ71UCjoN6nJceaFvGl4TYY.json', 'var_call_yibhjuQuYNVfbsvGJV2uRdwv': 'file_storage/call_yibhjuQuYNVfbsvGJV2uRdwv.json', 'var_call_P6u7UTLjRT3xZAh6jMePdi59': 'file_storage/call_P6u7UTLjRT3xZAh6jMePdi59.json'}

exec(code, env_args)
