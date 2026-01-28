code = """import json

# Load the large Case query result from the provided storage path
path = var_call_81qCXhrIirIMkLjSQmtstroQ
with open(path, 'r') as f:
    cases = json.load(f)

# target
target = '500Wt00000DDyznIAD'

def normalize(idv):
    if idv is None:
        return None
    s = str(idv)
    s = s.strip()
    if s.startswith('#'):
        s = s[1:]
    return s

matches = []
for c in cases:
    nid = normalize(c.get('id'))
    if nid is None:
        continue
    if nid.lower() == target.lower() or 'ddyzn iad'.replace(' ', '') in nid.lower():
        matches.append(c)
    # also check if contains the suffix
    if 'ddyzn' in nid.lower() and nid.lower().endswith('iad'):
        if c not in matches:
            matches.append(c)
    # check if target appears anywhere
    if target.lower() in nid.lower() and c not in matches:
        matches.append(c)

# If not found directly, try fuzzy by checking if any id contains 'DDyznIAD'
if not matches:
    for c in cases:
        if 'ddyzniad' in str(c.get('id','')).lower():
            matches.append(c)

# Prepare output: list of matching ids (raw)
out = [m.get('id') for m in matches]

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_s1lNhDjFiycvs4aDFcZmLIc4': [], 'var_call_81qCXhrIirIMkLjSQmtstroQ': 'file_storage/call_81qCXhrIirIMkLjSQmtstroQ.json'}

exec(code, env_args)
