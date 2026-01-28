code = """import json
path = var_call_ifdhidu4Chp0AVBiJhSHILEk
with open(path, 'r') as f:
    readmes = json.load(f)
# We'll create a mapping from repo_name to whether its README content contains 'copyright' (case-insensitive)
import re
repo_readme_copyright = {}
for r in readmes:
    repo = r.get('sample_repo_name')
    content = r.get('content') or ''
    has_copy = bool(re.search(r'copyright', content, flags=re.IGNORECASE))
    # Keep True if any README for the repo has copyright
    if repo in repo_readme_copyright:
        repo_readme_copyright[repo] = repo_readme_copyright[repo] or has_copy
    else:
        repo_readme_copyright[repo] = has_copy
# Convert to lists for passing
repo_names = sorted(list(repo_readme_copyright.keys()))
has_copyright_list = [repo_readme_copyright[r] for r in repo_names]
output = json.dumps({'repo_names': repo_names, 'has_copyright': has_copyright_list})
print('__RESULT__:')
print(output)"""

env_args = {'var_call_o9nNR0lnbP7iyPnxPMBkLHgN': 'file_storage/call_o9nNR0lnbP7iyPnxPMBkLHgN.json', 'var_call_EIqlZdmwFYSTOJlsAQbUJcfR': 'file_storage/call_EIqlZdmwFYSTOJlsAQbUJcfR.json', 'var_call_ifdhidu4Chp0AVBiJhSHILEk': 'file_storage/call_ifdhidu4Chp0AVBiJhSHILEk.json'}

exec(code, env_args)
