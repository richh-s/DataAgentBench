code = """import json, os
# load helper
def load_var(v):
    if isinstance(v, str) and v.endswith('.json') and os.path.exists(v):
        with open(v, 'r') as f:
            return json.load(f)
    return v
var_mapping = load_var(var_call_Zgu0dlOfqao34ryZI7bLTHJA)
var_projinfo = load_var(var_call_iEEmLfxD9Rf5lxvvk0JlBkg4)
mapping = var_mapping.get('mapping') if isinstance(var_mapping, dict) else var_mapping
projinfo = var_projinfo
# extract project names from mapping
map_projects = sorted(list({m['ProjectName'] for m in mapping if m.get('ProjectName')}))
# extract repo names from project_info via regex
import re
projinfo_repos = set()
for entry in projinfo:
    pi = entry.get('Project_Information') or ''
    m = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
    if m:
        projinfo_repos.add(m.group(1))
projinfo_repos = sorted(list(projinfo_repos))
# compute intersection
inter = sorted(list(set(map_projects).intersection(set(projinfo_repos))) )
# prepare sample outputs
result = {
    'num_mapping_projects': len(map_projects),
    'num_projinfo_repos': len(projinfo_repos),
    'intersection_count': len(inter),
    'intersection_sample': inter[:50],
    'mapping_sample': map_projects[:50],
    'projinfo_sample': projinfo_repos[:50]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wTx4WUlrMN0IMwtp8pOPhILg': 'file_storage/call_wTx4WUlrMN0IMwtp8pOPhILg.json', 'var_call_dFPubGgWvKq7qBzs9pPNNtw9': 'file_storage/call_dFPubGgWvKq7qBzs9pPNNtw9.json', 'var_call_Zgu0dlOfqao34ryZI7bLTHJA': 'file_storage/call_Zgu0dlOfqao34ryZI7bLTHJA.json', 'var_call_iEEmLfxD9Rf5lxvvk0JlBkg4': 'file_storage/call_iEEmLfxD9Rf5lxvvk0JlBkg4.json', 'var_call_DGJ043ob5YIr5XE6gfKQH2bj': []}

exec(code, env_args)
