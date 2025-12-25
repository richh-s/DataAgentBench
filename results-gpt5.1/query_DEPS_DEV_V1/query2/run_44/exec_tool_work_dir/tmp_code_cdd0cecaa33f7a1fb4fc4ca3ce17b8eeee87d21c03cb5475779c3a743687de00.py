code = """import json, pandas as pd
from pathlib import Path

# Load full results from files
pkg_file = Path(var_call_zgGdMPcWoW65Vag8ZjuiRhbo)
proj_file = Path(var_call_9z3jmMPl2hL56ues2lcFtVYS)

with pkg_file.open() as f:
    pkg_data = json.load(f)
with proj_file.open() as f:
    proj_data = json.load(f)

pkg_df = pd.DataFrame(pkg_data)[['System','Name','Version']].drop_duplicates()
proj_df = pd.DataFrame(proj_data)[['System','Name','Version','ProjectName','Project_Information']].drop_duplicates()

merged = pkg_df.merge(proj_df, on=['System','Name','Version'], how='inner')

# extract fork count from Project_Information text
import re

def extract_forks(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"(forks|fork count)[: ]+([0-9]+)", text)
    if m:
        return int(m.group(2))
    m = re.search(r"([0-9]+) forks", text)
    if m:
        return int(m.group(1))
    return None

merged['Forks'] = merged['Project_Information'].apply(extract_forks)

# group by project to get max forks per project
proj_forks = merged.dropna(subset=['Forks']).groupby('ProjectName', as_index=False)['Forks'].max()

# top 5 by forks
top5 = proj_forks.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zgGdMPcWoW65Vag8ZjuiRhbo': 'file_storage/call_zgGdMPcWoW65Vag8ZjuiRhbo.json', 'var_call_NEi9IHFsuBGj6QjuP7MArIyM': ['project_info', 'project_packageversion'], 'var_call_9z3jmMPl2hL56ues2lcFtVYS': 'file_storage/call_9z3jmMPl2hL56ues2lcFtVYS.json'}

exec(code, env_args)
