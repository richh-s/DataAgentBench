code = """import json
# Load results from previous query_db calls (file paths are stored in these vars)
p_repos = var_call_uw0sCp8qNYGkuHPZmnk43Lat
p_commits = var_call_nEgJdq2JcrsPsJugrSRh4OHr

with open(p_repos, 'r') as f:
    repos = json.load(f)
with open(p_commits, 'r') as f:
    commits = json.load(f)

repo_set = set(r['repo_name'] for r in repos if 'repo_name' in r)
count = sum(1 for c in commits if c.get('repo_name') in repo_set)

import json
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_uw0sCp8qNYGkuHPZmnk43Lat': 'file_storage/call_uw0sCp8qNYGkuHPZmnk43Lat.json', 'var_call_nEgJdq2JcrsPsJugrSRh4OHr': 'file_storage/call_nEgJdq2JcrsPsJugrSRh4OHr.json'}

exec(code, env_args)
