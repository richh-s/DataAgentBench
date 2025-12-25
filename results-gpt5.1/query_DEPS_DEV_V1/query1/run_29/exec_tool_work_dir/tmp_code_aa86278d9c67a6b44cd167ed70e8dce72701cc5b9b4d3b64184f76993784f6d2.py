code = """import json, re
import pandas as pd

# Load project names from latest NPM-linked projects
with open(var_call_VEkVgyd40pLJ92ASc83wBI8N, 'r') as f:
    project_names = json.load(f)
project_set = set(project_names)

# Load all project_info
with open(var_call_Ucy5sEOyBvfntuIylmDzkVAa, 'r') as f:
    proj_info_records = json.load(f)

rows = []
pattern = re.compile(r"project ([^ ]+/[^ ]+) .*? (?:has|currently has|is .*? with).*?([0-9,]+) stars", re.IGNORECASE)
for rec in proj_info_records:
    text = rec.get('Project_Information','')
    m = pattern.search(text)
    if not m:
        continue
    name = m.group(1)
    stars = int(m.group(2).replace(',',''))
    if name in project_set:
        rows.append({'ProjectName': name, 'Stars': stars})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

# Now join back to find corresponding NPM packages (latest only)
with open(var_call_thUZGQO7cklBnqSPETgcLstB, 'r') as f:
    latest_pkgs = json.load(f)
latest_df = pd.DataFrame(latest_pkgs)

with open(var_call_TI6QZntnSRfKQPPImVocHi1C, 'r') as f:
    proj_pkg = json.load(f)
pp_df = pd.DataFrame(proj_pkg)

merged = latest_df.merge(pp_df, on=['System','Name','Version'], how='inner')
merged = merged.merge(pi_df, on='ProjectName', how='inner')

# For each NPM package name, we consider popularity by Stars; sort and pick top 5
merged_top = merged.sort_values('Stars', ascending=False)

# Deduplicate by package Name, keeping highest stars
pkg_top = merged_top.drop_duplicates(subset=['Name']).head(5)

result = pkg_top[['Name','Version','Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BFLomqnIRVvA4BjveUhoTNXX': 'file_storage/call_BFLomqnIRVvA4BjveUhoTNXX.json', 'var_call_m9WhF5Har4VXBEpDM9NrHHVB': ['project_info', 'project_packageversion'], 'var_call_TI6QZntnSRfKQPPImVocHi1C': 'file_storage/call_TI6QZntnSRfKQPPImVocHi1C.json', 'var_call_thUZGQO7cklBnqSPETgcLstB': 'file_storage/call_thUZGQO7cklBnqSPETgcLstB.json', 'var_call_VEkVgyd40pLJ92ASc83wBI8N': 'file_storage/call_VEkVgyd40pLJ92ASc83wBI8N.json', 'var_call_Ucy5sEOyBvfntuIylmDzkVAa': 'file_storage/call_Ucy5sEOyBvfntuIylmDzkVAa.json'}

exec(code, env_args)
