code = """import json

# Load results from previous queries. The storage keys are available as variables.
def load_var(v):
    if isinstance(v, str):
        # v is a file path to a JSON file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

repos = load_var(var_call_fSm2ju4W7EDucc5QvsPqzH5q)
commits = load_var(var_call_jyU3YmQUDjKduCT8MY9TLbO6)

# Build set of target repo names
repo_set = set()
for r in repos:
    name = r.get('repo_name')
    if name:
        repo_set.add(name)

count = 0
for c in commits:
    rn = c.get('repo_name')
    if rn not in repo_set:
        continue
    msg = c.get('message')
    if msg is None:
        continue
    # Ensure message is shorter than 1000 characters and non-empty when stripped
    if len(msg) >= 1000:
        continue
    if msg.strip() == '':
        continue
    # Check beginning after trimming leading whitespace, case-insensitive
    if msg.lstrip().lower().startswith(('merge', 'update', 'test')):
        continue
    count += 1

import json
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_fSm2ju4W7EDucc5QvsPqzH5q': 'file_storage/call_fSm2ju4W7EDucc5QvsPqzH5q.json', 'var_call_jyU3YmQUDjKduCT8MY9TLbO6': 'file_storage/call_jyU3YmQUDjKduCT8MY9TLbO6.json'}

exec(code, env_args)
