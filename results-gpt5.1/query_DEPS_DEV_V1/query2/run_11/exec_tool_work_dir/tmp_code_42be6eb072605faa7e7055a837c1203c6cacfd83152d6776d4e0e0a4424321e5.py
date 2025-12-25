code = """import json, re, pandas as pd

# Load full datasets from files
pkg_path = var_call_kra3udGTLHYU7U6ltBdO4XBm
ppv_path = var_call_cwnXVObxTvH46vSFLz9fBEzj
pi_path = var_call_X18ipqIb3jX4XVvSAxukeSqM

with open(pkg_path) as f:
    pkg = json.load(f)
with open(ppv_path) as f:
    ppv = json.load(f)
with open(pi_path) as f:
    pi = json.load(f)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# join NPM MIT-release packages with project_packageversion
merged = pkg_df.merge(ppv_df, on=["System","Name","Version"], how="inner")

# keep only GitHub projects
merged = merged[merged["ProjectType"] == "GITHUB"]

# extract project name from Project_Information text
# pattern like 'The project lodash/lodash on GitHub' or 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart'
name_patterns = [
    r"The project ([^\s]+/[^\s]+) on GitHub",
    r"The project ([^\s]+/[^\s]+) is hosted on GitHub",
    r"hosted on GitHub under the name ([^,]+)",
    r"hosted on GITHUB under the name ([^,]+)",
    r"named ([^\s]+/[^\s]+) on GitHub",
]

names = []
for txt in pi_df["Project_Information"]:
    mname = None
    for pat in name_patterns:
        m = re.search(pat, txt)
        if m:
            mname = m.group(1).strip()
            break
    names.append(mname)

pi_df["ProjectName"] = names
pi_df = pi_df.dropna(subset=["ProjectName"])  # keep rows where name found

# extract fork count from text: patterns like '5782 forks' or 'and 0 forks.'
fork_patterns = [
    r"(\d+) forks",
]

forks = []
for txt in pi_df["Project_Information"]:
    fcount = None
    for pat in fork_patterns:
        m = re.search(pat, txt)
        if m:
            fcount = int(m.group(1))
            break
    forks.append(fcount)

pi_df["Forks"] = forks
pi_df = pi_df.dropna(subset=["Forks"])  # must have fork count

# now join merged (packages) with pi_df on ProjectName
merged2 = merged.merge(pi_df[["ProjectName","Forks"]], on="ProjectName", how="inner")

# get top 5 by Forks (distinct projects)
merged2 = merged2.sort_values("Forks", ascending=False)

top_projects = merged2.drop_duplicates(subset=["ProjectName"])[["ProjectName","Forks"]].head(5)

result = top_projects.to_dict(orient="records")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kra3udGTLHYU7U6ltBdO4XBm': 'file_storage/call_kra3udGTLHYU7U6ltBdO4XBm.json', 'var_call_cwnXVObxTvH46vSFLz9fBEzj': 'file_storage/call_cwnXVObxTvH46vSFLz9fBEzj.json', 'var_call_X18ipqIb3jX4XVvSAxukeSqM': 'file_storage/call_X18ipqIb3jX4XVvSAxukeSqM.json'}

exec(code, env_args)
