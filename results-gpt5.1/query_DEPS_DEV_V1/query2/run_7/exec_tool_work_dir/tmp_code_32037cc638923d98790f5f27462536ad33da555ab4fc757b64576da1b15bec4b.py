code = """import json, pandas as pd
from pathlib import Path

# Load full results from files
pkg_file = Path(var_call_Zswc2tEnkXR0EIUgMpmrwLyK)
proj_file = Path(var_call_XMyb3cE84C7bB6t4DTJxNUHJ)

packages = json.loads(pkg_file.read_text())
projects = json.loads(proj_file.read_text())

pkg_df = pd.DataFrame(packages)
proj_df = pd.DataFrame(projects)

# Join on System, Name, Version
merged = pkg_df.merge(proj_df, on=['System','Name','Version'], how='inner')

# Extract fork count from Project_Information text
import re

def get_forks(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"forks? count of (\d+)|has (\d+) forks", text)
    if not m:
        return None
    return int(m.group(1) or m.group(2))

merged['Forks'] = merged['Project_Information'].apply(get_forks)

# Aggregate by project (ProjectName) taking max forks observed
agg = (merged.dropna(subset=['Forks'])
            .groupby('ProjectName', as_index=False)
            .agg({'Forks':'max'}))

# Get top 5 by forks
Top5 = agg.sort_values('Forks', ascending=False).head(5)

result = Top5.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Zswc2tEnkXR0EIUgMpmrwLyK': 'file_storage/call_Zswc2tEnkXR0EIUgMpmrwLyK.json', 'var_call_xChKEvXtRuu2HLgWT1O2K7s4': ['project_info', 'project_packageversion'], 'var_call_XMyb3cE84C7bB6t4DTJxNUHJ': 'file_storage/call_XMyb3cE84C7bB6t4DTJxNUHJ.json'}

exec(code, env_args)
