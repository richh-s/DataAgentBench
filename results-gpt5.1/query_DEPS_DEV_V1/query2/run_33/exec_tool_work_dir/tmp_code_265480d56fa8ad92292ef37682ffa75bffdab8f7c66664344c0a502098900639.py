code = """import json, pandas as pd

# Load MIT release NPM packages
file_path = var_call_rJPlMWitrcHif3XQ0PAzG27G
with open(file_path, 'r') as f:
    mit_packages = json.load(f)

# Load project-package mappings with project info
file_path2 = var_call_gFawU8JLRdSrNJ9XTsNiM7Rc
with open(file_path2, 'r') as f:
    project_pk = json.load(f)

pkg_df = pd.DataFrame(mit_packages)
proj_df = pd.DataFrame(project_pk)

# Join on System, Name, Version
merged = pkg_df.merge(proj_df, on=['System','Name','Version'], how='inner')

# Extract fork counts from Project_Information text
import re

def extract_forks(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"(forks count of|forks,|forks\.|forks\))\s*(\d+)", text)
    if m:
        return int(m.group(2))
    m2 = re.search(r"(\d+) fork", text)
    if m2:
        return int(m2.group(1))
    return None

merged['Forks'] = merged['Project_Information'].apply(extract_forks)

# Aggregate by project (ProjectName) taking max forks seen
agg = merged.dropna(subset=['Forks']).groupby('ProjectName').agg({'Forks':'max'}).reset_index()

# Top 5 by forks
Top5 = agg.sort_values('Forks', ascending=False).head(5)

result = Top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rJPlMWitrcHif3XQ0PAzG27G': 'file_storage/call_rJPlMWitrcHif3XQ0PAzG27G.json', 'var_call_i5UfgfjGUUT6Tg4ITpB8daxq': ['project_info', 'project_packageversion'], 'var_call_gFawU8JLRdSrNJ9XTsNiM7Rc': 'file_storage/call_gFawU8JLRdSrNJ9XTsNiM7Rc.json'}

exec(code, env_args)
