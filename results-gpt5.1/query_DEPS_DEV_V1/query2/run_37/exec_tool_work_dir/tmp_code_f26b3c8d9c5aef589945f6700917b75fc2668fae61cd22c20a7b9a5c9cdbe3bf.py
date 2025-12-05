code = """import json, re, pandas as pd

# Load full results from files
import pathlib

pkg_path = pathlib.Path(var_call_zrT0DI51mGpUF4C8705IpbEa)
with pkg_path.open() as f:
    pkg_data = json.load(f)

projpkg_path = pathlib.Path(var_call_h55YWvEt697JBOPUaulHdlew)
with projpkg_path.open() as f:
    projpkg_data = json.load(f)

projinfo_path = pathlib.Path(var_call_PiwWpczvKvp1iOzrrjKpQYT0)
with projinfo_path.open() as f:
    projinfo_data = json.load(f)

pkg_df = pd.DataFrame(pkg_data)
projpkg_df = pd.DataFrame(projpkg_data)
projinfo_df = pd.DataFrame(projinfo_data)

# join packageinfo (MIT + release NPM) with project_packageversion on System, Name, Version
merged = pkg_df.merge(projpkg_df, on=["System", "Name", "Version"], how="inner")

# deduplicate by ProjectName (if multiple versions)
merged_unique = merged.drop_duplicates(subset=["ProjectName"])

# Project_Information does not include ProjectName explicitly in column, so we need to map by parsing owner/repo from text.
# Build a mapping from owner/repo to fork count
pattern = re.compile(r"project ([^\s/]+/[^\s ]+) .*? (?:forks count of (\d+)|forked (\d+) times|and (\d+) forks|, and (\d+) forks|, along with .* (\d+) forks|has been forked (\d+) times)", re.IGNORECASE)

proj_forks = {}
for row in projinfo_df["Project_Information"]:
    text = row
    m = pattern.search(text)
    if not m:
        continue
    repo = m.group(1)
    nums = [g for g in m.groups()[1:] if g is not None]
    if not nums:
        continue
    forks = int(nums[-1])
    proj_forks[repo] = forks

# Now compute fork counts for our MIT+release NPM projects
results = []
for _, r in merged_unique.iterrows():
    repo = r["ProjectName"]
    forks = proj_forks.get(repo)
    if forks is None:
        continue
    results.append({"ProjectName": repo, "Forks": forks})

res_df = pd.DataFrame(results)
if not res_df.empty:
    top5 = res_df.sort_values("Forks", ascending=False).drop_duplicates("ProjectName").head(5)
    out = top5.to_dict(orient="records")
else:
    out = []

result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_zrT0DI51mGpUF4C8705IpbEa': 'file_storage/call_zrT0DI51mGpUF4C8705IpbEa.json', 'var_call_h55YWvEt697JBOPUaulHdlew': 'file_storage/call_h55YWvEt697JBOPUaulHdlew.json', 'var_call_PiwWpczvKvp1iOzrrjKpQYT0': 'file_storage/call_PiwWpczvKvp1iOzrrjKpQYT0.json'}

exec(code, env_args)
