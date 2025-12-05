code = """import json, pandas as pd, re
from pathlib import Path

# Load full results for MIT release NPM packages
filepath_pkgs = Path(var_call_2treiK3zlZyGbcE4ukFJEHUx)
with filepath_pkgs.open() as f:
    pkgs = json.load(f)

filepath_proj = Path(var_call_01ADOceX1nhMvgBbzelczN48)
with filepath_proj.open() as f:
    proj = json.load(f)

pkgs_df = pd.DataFrame(pkgs)
proj_df = pd.DataFrame(proj)

# inner join on System, Name, Version
merged = pkgs_df.merge(proj_df, on=["System", "Name", "Version"], how="inner")

# Extract fork count from Project_Information text using regex
fork_counts = []
for txt in merged["Project_Information"].fillna(""):
    m = re.search(r"forks? count of (\d+)|forks?\." , txt)
    if m:
        if m.group(1):
            fork_counts.append(int(m.group(1)))
        else:
            # try pattern "and X forks"
            m2 = re.search(r"and (\d+) forks", txt)
            fork_counts.append(int(m2.group(1)) if m2 else 0)
    else:
        m2 = re.search(r"(\d+) forks", txt)
        fork_counts.append(int(m2.group(1)) if m2 else 0)

merged["ForkCount"] = fork_counts

# aggregate by ProjectName to get max fork count (project-level)
agg = merged.groupby("ProjectName", as_index=False)["ForkCount"].max()

# get top 5 by fork count
top5 = agg.sort_values("ForkCount", ascending=False).head(5)

result = top5.to_dict(orient="records")

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2treiK3zlZyGbcE4ukFJEHUx': 'file_storage/call_2treiK3zlZyGbcE4ukFJEHUx.json', 'var_call_fhXHltZKZ27DULLZKuB38VFx': ['project_info', 'project_packageversion'], 'var_call_01ADOceX1nhMvgBbzelczN48': 'file_storage/call_01ADOceX1nhMvgBbzelczN48.json'}

exec(code, env_args)
