code = """import json
from pathlib import Path
# Load results from previous queries stored as JSON file paths
pck_path = var_call_JLX8fJISuf0VC1Ing7Ys81b2
ppv_path = var_call_zATBQxYiBHWJjzdye9isrU7I

with open(pck_path, 'r', encoding='utf-8') as f:
    packages = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppvs = json.load(f)

# Convert to dictionaries keyed by (System,Name,Version) for packages
pkg_keys = set((p['System'], p['Name'], p['Version']) for p in packages)

# Find matching project_packageversion rows
matches = [r for r in ppvs if (r['System'], r['Name'], r['Version']) in pkg_keys]

# Extract unique ProjectName values
project_names = sorted(list({r['ProjectName'] for r in matches if r.get('ProjectName')}))

result = {
    'num_packages_filtered': len(packages),
    'num_ppv_rows': len(ppvs),
    'num_matches': len(matches),
    'num_unique_project_names': len(project_names),
    'project_names_sample': project_names[:200],
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JLX8fJISuf0VC1Ing7Ys81b2': 'file_storage/call_JLX8fJISuf0VC1Ing7Ys81b2.json', 'var_call_zATBQxYiBHWJjzdye9isrU7I': 'file_storage/call_zATBQxYiBHWJjzdye9isrU7I.json'}

exec(code, env_args)
