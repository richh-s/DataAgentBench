code = """import json
# load commits result file
path = var_call_fWMTTXKSyQYmQk3gHgrO9qa4
with open(path, 'r') as f:
    commits = json.load(f)
# Build a mapping of repo_name -> count of messages (we'll filter by repo set later)
from collections import defaultdict
repo_message_counts = defaultdict(int)
for r in commits:
    rn = r.get('repo_name')
    msg = r.get('message')
    if rn and msg is not None:
        # apply same filters as query did (already applied) but ensure trimming
        mstr = msg.lstrip()
        if len(mstr) < 1000 and mstr != '' and not mstr.lower().startswith(('merge','update','test')):
            repo_message_counts[rn] += 1
# Convert to list of dicts for further processing
repo_counts_list = [{'repo_name': k, 'count': v} for k,v in repo_message_counts.items()]
print('__RESULT__:')
print(json.dumps(repo_counts_list))"""

env_args = {'var_call_fNDvHPSqxhTTLn5V45C4wwjs': 'file_storage/call_fNDvHPSqxhTTLn5V45C4wwjs.json', 'var_call_jmqELJpiXJqDN2kbXqABdEVi': 'file_storage/call_jmqELJpiXJqDN2kbXqABdEVi.json', 'var_call_fWMTTXKSyQYmQk3gHgrO9qa4': 'file_storage/call_fWMTTXKSyQYmQk3gHgrO9qa4.json'}

exec(code, env_args)
