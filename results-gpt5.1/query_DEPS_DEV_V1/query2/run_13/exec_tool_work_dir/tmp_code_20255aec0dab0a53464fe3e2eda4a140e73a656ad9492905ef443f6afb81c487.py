code = """import json, re, pandas as pd

# Load data from storage
pkg_path = var_call_3T5p9ECEVwwp1Els1Z9zQuw9
projpkg_path = var_call_iEIxoJwGMesyOzqAiN7lxWaD
projinfo_path = var_call_Sxk7ctsMutXjKB6ngupPqh8q

pkg = pd.read_json(pkg_path)
projpkg = pd.read_json(projpkg_path)
projinfo = pd.read_json(projinfo_path)

# Join packages (NPM, MIT, release) with project_packageversion on System, Name, Version
merged = pkg.merge(projpkg, on=["System", "Name", "Version"], how="inner")
merged = merged[merged["ProjectType"] == "GITHUB"]

# Project_Information has project name and forks; parse ProjectName and fork count
pattern = re.compile(r"project ([^ ]+/[^ ]+).+?forks?[, ]+and|project ([^ ]+/[^ ]+).+?and [0-9,]+ forks|named ([^ ]+/[^ ]+).+?forks|under the name ([^ ]+/[^ ]+).+?forks", re.IGNORECASE)

projinfo["ProjectName"] = None
projinfo["Forks"] = None

for idx, row in projinfo.iterrows():
    text = row["Project_Information"]
    # Extract project name (owner/repo)
    m_name = re.search(r"(?:project|repository|named|under the name) ([\w.-]+/[\w.-]+)", text, re.IGNORECASE)
    if m_name:
        projinfo.at[idx, "ProjectName"] = m_name.group(1)
    # Extract forks count
    m_forks = re.search(r"(\d[\d,]*) forks", text)
    if m_forks:
        forks = int(m_forks.group(1).replace(",", ""))
        projinfo.at[idx, "Forks"] = forks

projinfo_clean = projinfo.dropna(subset=["ProjectName", "Forks"])

# Merge merged (package->project) with projinfo_clean on ProjectName
full = merged.merge(projinfo_clean[["ProjectName", "Forks"]], on="ProjectName", how="inner")

# Aggregate by project (some projects may map to multiple package versions)
agg = full.groupby("ProjectName")["Forks"].max().reset_index()

# Get top 5 by forks
top5 = agg.sort_values("Forks", ascending=False).head(5)

result = top5.to_dict(orient="records")

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3T5p9ECEVwwp1Els1Z9zQuw9': 'file_storage/call_3T5p9ECEVwwp1Els1Z9zQuw9.json', 'var_call_iEIxoJwGMesyOzqAiN7lxWaD': 'file_storage/call_iEIxoJwGMesyOzqAiN7lxWaD.json', 'var_call_Sxk7ctsMutXjKB6ngupPqh8q': 'file_storage/call_Sxk7ctsMutXjKB6ngupPqh8q.json'}

exec(code, env_args)
