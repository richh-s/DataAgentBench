code = """import json
import pandas as pd
import re

with open(var_call_WP0QgvUXBGzndFHNwByxIEyu, 'r') as f:
    pkg_records = json.load(f)
with open(var_call_fqznU0TxJFLK3Yzy4SKeKJZG, 'r') as f:
    ppv_records = json.load(f)
with open(var_call_qcP1LhpfPW603FyG3wH2e8Jh, 'r') as f:
    pinfo_records = json.load(f)

pkg_df = pd.DataFrame(pkg_records)
ppv_df = pd.DataFrame(ppv_records)
pinfo_df = pd.DataFrame(pinfo_records)

for col in ['System','Name','Version']:
    if col in pkg_df.columns:
        pkg_df[col] = pkg_df[col].astype(str)
    if col in ppv_df.columns:
        ppv_df[col] = ppv_df[col].astype(str)

merged = pd.merge(pkg_df, ppv_df, on=['System','Name','Version'], how='inner')
project_names = merged['ProjectName'].dropna().astype(str).unique().tolist()
project_names_lc = [p.strip().lower() for p in project_names]

repo_to_forks = {}
repo_to_stars = {}

repo_pattern = re.compile(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
stars_pattern = re.compile(r"([0-9,]+)\s*stars", re.IGNORECASE)
forks_pattern = re.compile(r"([0-9,]+)\s*forks", re.IGNORECASE)

for rec in pinfo_records:
    pi = rec.get('Project_Information') or ''
    if not isinstance(pi, str):
        continue
    # find repo (first occurrence)
    m = repo_pattern.search(pi)
    if not m:
        continue
    repo = m.group(1).strip().lower()
    # find stars and forks
    ms = stars_pattern.search(pi)
    mf = forks_pattern.search(pi)
    def safe_int_str(s):
        try:
            s2 = s.replace(',','').strip()
            return s2
        except Exception:
            return ''
    stars = None
    forks = None
    if ms and ms.group(1):
        s = safe_int_str(ms.group(1))
        try:
            stars = int(s) if s!='' else None
        except:
            stars = None
    if mf and mf.group(1):
        s = safe_int_str(mf.group(1))
        try:
            forks = int(s) if s!='' else None
        except:
            forks = None
    # fallback: use numbers in text
    if forks is None or stars is None:
        nums_raw = re.findall(r"([0-9,]+)", pi)
        nums = []
        for n in nums_raw:
            try:
                val = int(n.replace(',',''))
                nums.append(val)
            except:
                continue
        if forks is None and len(nums)>0:
            forks = nums[-1]
        if stars is None and len(nums)>1:
            stars = nums[-2]
    repo_to_forks[repo] = forks
    repo_to_stars[repo] = stars

results = []
for orig, lc in zip(project_names, project_names_lc):
    forks = repo_to_forks.get(lc)
    stars = repo_to_stars.get(lc)
    if forks is None:
        # try partial match by repo name
        for repo, f in repo_to_forks.items():
            if repo.endswith('/' + lc.split('/')[-1]):
                forks = f
                stars = repo_to_stars.get(repo)
                break
    if forks is None:
        continue
    results.append({'ProjectName': orig, 'Forks': int(forks) if forks is not None else None, 'Stars': int(stars) if stars is not None else None})

if not results:
    top5 = []
else:
    dfr = pd.DataFrame(results)
    dfr = dfr.sort_values(['Forks','Stars'], ascending=[False, False])
    dfr = dfr.drop_duplicates(subset=['ProjectName'])
    top5 = dfr.head(5)[['ProjectName','Forks','Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_WP0QgvUXBGzndFHNwByxIEyu': 'file_storage/call_WP0QgvUXBGzndFHNwByxIEyu.json', 'var_call_fqznU0TxJFLK3Yzy4SKeKJZG': 'file_storage/call_fqznU0TxJFLK3Yzy4SKeKJZG.json', 'var_call_qcP1LhpfPW603FyG3wH2e8Jh': 'file_storage/call_qcP1LhpfPW603FyG3wH2e8Jh.json'}

exec(code, env_args)
