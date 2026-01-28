code = """import json

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

repos = load_var(var_call_GZhIb6Jtf18JVpacFoNO90Hj)
commits = load_var(var_call_kowTAx89GCgmAREUJ8e1L0rn)

repo_set = set()
for r in repos:
    if isinstance(r, dict) and 'repo_name' in r:
        repo_set.add(r['repo_name'])

count = 0
for c in commits:
    if not isinstance(c, dict):
        continue
    rn = c.get('repo_name')
    if rn not in repo_set:
        continue
    msg = c.get('message')
    if msg is None:
        continue
    try:
        msg_len = len(msg)
    except Exception:
        continue
    if msg_len >= 1000:
        continue
    s = msg.lstrip().lower()
    if s.startswith('merge') or s.startswith('update') or s.startswith('test'):
        continue
    count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_GZhIb6Jtf18JVpacFoNO90Hj': 'file_storage/call_GZhIb6Jtf18JVpacFoNO90Hj.json', 'var_call_kowTAx89GCgmAREUJ8e1L0rn': 'file_storage/call_kowTAx89GCgmAREUJ8e1L0rn.json'}

exec(code, env_args)
