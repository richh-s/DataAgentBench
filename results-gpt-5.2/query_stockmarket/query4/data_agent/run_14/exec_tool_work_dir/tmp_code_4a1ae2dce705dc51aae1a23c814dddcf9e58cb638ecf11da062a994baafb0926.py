code = """import json
src = var_call_pSlDq3Iya59P4L94vtKPK8Li
if isinstance(src, str):
    with open(src,'r') as f:
        obj = json.load(f)
else:
    obj = src

duck_query = obj['duck_query']
# Wrap to compute top 5 by (up_days - down_days) among those with more ups than downs
final_query = "SELECT Symbol FROM (" + duck_query + ") t WHERE up_days > down_days ORDER BY (up_days - down_days) DESC, up_days DESC, Symbol ASC LIMIT 5"
print('__RESULT__:')
print(json.dumps({'final_query': final_query, 'name_map': obj['name_map']}))"""

env_args = {'var_call_R5Fm9qBHEnIjJw8IdgrwecTb': 'file_storage/call_R5Fm9qBHEnIjJw8IdgrwecTb.json', 'var_call_9KkYakqJdaS1o0ssxYdG90nb': 'file_storage/call_9KkYakqJdaS1o0ssxYdG90nb.json', 'var_call_pSlDq3Iya59P4L94vtKPK8Li': 'file_storage/call_pSlDq3Iya59P4L94vtKPK8Li.json'}

exec(code, env_args)
