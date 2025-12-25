code = """import json, pandas as pd
from pathlib import Path

# Load full results from files
pkg_file = Path(var_call_vJ81a7Pvn4B2U7ovplMzsUl3)
projpkg_file = Path(var_call_MHkyt52pdtgWB3bsAfRSZajE)
projinfo_file = Path(var_call_t2mcJyZMoGFI2a16b6fDpQl0)

packages = json.loads(pkg_file.read_text())
projpkgs = json.loads(projpkg_file.read_text())
projinfos = json.loads(projinfo_file.read_text())

pkg_df = pd.DataFrame(packages)
projpkg_df = pd.DataFrame(projpkgs)
projinfo_df = pd.DataFrame(projinfos)

# Join NPM MIT release packages with project_packageversion
merged = pkg_df.merge(projpkg_df, on=["System","Name","Version"], how="inner")

# We only care about GitHub projects
merged = merged[merged["ProjectType"] == "GITHUB"]

# Extract ProjectName list
project_names = merged["ProjectName"].dropna().unique().tolist()

# From project_info, filter rows whose Project_Information mentions the project name and a forks count.
# We'll try to extract owner/repo and fork count via simple parsing.

records = []
for _, row in projinfo_df.iterrows():
    info = row["Project_Information"]
    if not isinstance(info, str):
        continue
    # try to find pattern 'The project <owner>/<repo>' or 'The GitHub project <owner>/<repo>' or 'on GitHub, named <owner>/<repo>'
    text = info
    # crude search for owner/repo by looking for ' on GitHub' and taking preceding token
    repo = None
    if " on GitHub" in text:
        prefix = text.split(" on GitHub")[0]
        parts = prefix.split()
        if parts:
            repo = parts[-1]
    if not repo and " is hosted on GitHub" in text:
        prefix = text.split(" is hosted on GitHub")[0]
        parts = prefix.split()
        if parts:
            repo = parts[-1]
    if not repo and " named " in text and " on GitHub" in text:
        mid = text.split(" named ",1)[1]
        repo = mid.split(" on GitHub",1)[0]
    if not repo:
        continue
    repo = repo.strip(',.')
    if repo not in project_names:
        continue
    # extract forks count by looking for 'forks' and taking preceding number
    forks = None
    if "forks" in text:
        before_forks = text.split("forks",1)[0]
        tokens = before_forks.strip().split()
        if tokens:
            last = tokens[-1].replace(',','')
            try:
                forks = int(last)
            except ValueError:
                pass
    if forks is None:
        continue
    records.append({"ProjectName": repo, "Forks": forks})

forks_df = pd.DataFrame(records).drop_duplicates(subset=["ProjectName"])  # one entry per project

# Now filter to projects actually in merged
forks_df = forks_df[forks_df["ProjectName"].isin(project_names)]

# Get top 5 by forks
top5 = forks_df.sort_values("Forks", ascending=False).head(5)

result = top5.to_dict(orient="records")

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_vJ81a7Pvn4B2U7ovplMzsUl3': 'file_storage/call_vJ81a7Pvn4B2U7ovplMzsUl3.json', 'var_call_m70FtqY4nUUV6YNirKmeAAGI': ['project_info', 'project_packageversion'], 'var_call_MHkyt52pdtgWB3bsAfRSZajE': 'file_storage/call_MHkyt52pdtgWB3bsAfRSZajE.json', 'var_call_t2mcJyZMoGFI2a16b6fDpQl0': 'file_storage/call_t2mcJyZMoGFI2a16b6fDpQl0.json'}

exec(code, env_args)
