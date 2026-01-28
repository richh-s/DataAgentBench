code = """import json
from collections import defaultdict

# Load data from previous query result
path = var_call_4hKIMsx9lRKhpjytQ2cqbj4p
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# normalize helper
def normalize_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s == '' or s.lower() == 'none':
        return None
    # remove leading hashes
    while s.startswith('#'):
        s = s[1:]
    return s

# Filter owner assignment records within data
owner_records = [r for r in data if r.get('field__c') and str(r.get('field__c')).strip().lower() == 'owner assignment']

handled_cases = defaultdict(set)  # agent_id -> set(caseid)
transfer_counts = defaultdict(int)  # agent_id -> transfer count

for r in owner_records:
    caseid = r.get('caseid__c')
    if caseid is None:
        continue
    caseid = str(caseid).strip()
    old_raw = r.get('oldvalue__c')
    new_raw = r.get('newvalue__c')
    old = normalize_id(old_raw)
    new = normalize_id(new_raw)
    # handled: agent appears as new assignee
    if new is not None:
        handled_cases[new].add(caseid)
    # transfer counts: if old is an agent and new is an agent and different
    if old is not None and new is not None and old != new:
        transfer_counts[old] += 1

# Consider only agents who handled >0 cases
agents_with_handled = [agent for agent, cases in handled_cases.items() if len(cases) > 0]

if not agents_with_handled:
    result = None
else:
    # For each agent, get transfer count (default 0)
    agent_counts = [(agent, transfer_counts.get(agent, 0)) for agent in agents_with_handled]
    # find minimal transfer count
    min_count = min(c for a, c in agent_counts)
    # agents with min count
    candidates = [a for a, c in agent_counts if c == min_count]
    # deterministic tie-break: choose lexicographically smallest id
    chosen = sorted(candidates)[0]
    result = chosen

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_4hKIMsx9lRKhpjytQ2cqbj4p': 'file_storage/call_4hKIMsx9lRKhpjytQ2cqbj4p.json'}

exec(code, env_args)
