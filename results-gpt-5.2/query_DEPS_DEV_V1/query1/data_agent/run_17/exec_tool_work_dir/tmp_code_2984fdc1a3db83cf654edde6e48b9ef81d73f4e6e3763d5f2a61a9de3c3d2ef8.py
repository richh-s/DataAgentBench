code = """import json, re, pandas as pd

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_result(var_call_Fi1wFc4bNDxpc6JYbInRKORR)
ppv = load_result(var_call_CTiWb1knml6oh0fz10VSrtOc)
pi = load_result(var_call_nix68Vi01ClSxHYXMRDoDs0U)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package name based on VersionInfo.IsRelease true and max Ordinal

def is_release(vinfo):
    try:
        o = json.loads(vinfo)
        return bool(o.get('IsRelease', False)), o.get('Ordinal', None)
    except Exception:
        return False, None

rels = pkg_df['VersionInfo'].apply(is_release)
pkg_df['IsRelease'] = rels.apply(lambda x: x[0])
pkg_df['Ordinal'] = rels.apply(lambda x: x[1] if x[1] is not None else -1)

latest = (pkg_df[pkg_df['IsRelease'] == True]
          .sort_values(['Name','Ordinal','UpstreamPublishedAt'], ascending=[True, False, False])
          .drop_duplicates(subset=['Name'], keep='first')[['Name','Version']])

# join to github projects mapping
m = latest.merge(ppv_df, on=['Name','Version'], how='inner')

# parse stars and project name from Project_Information
pat = re.compile(r"project\s+([^\s]+/[^\s]+)\s+.*?\b([0-9][0-9,]*)\s+stars\b", re.IGNORECASE)

def parse_pi(text):
    if text is None:
        return None, None
    mt = pat.search(text)
    if not mt:
        return None, None
    proj = mt.group(1).strip().rstrip('.')
    stars = int(mt.group(2).replace(',',''))
    return proj, stars

pi_df[['ParsedProject','Stars']] = pi_df['Project_Information'].apply(lambda t: pd.Series(parse_pi(t)))
pi_map = pi_df.dropna(subset=['ParsedProject','Stars']).drop_duplicates(subset=['ParsedProject'])[['ParsedProject','Stars']]

m2 = m.merge(pi_map, left_on='ProjectName', right_on='ParsedProject', how='left')

# For packages mapping to multiple repos, take max stars
agg = (m2.dropna(subset=['Stars'])
       .groupby(['Name','Version'], as_index=False)
       .agg(GithubRepo=('ProjectName','first'), GithubStars=('Stars','max')))

top5 = agg.sort_values(['GithubStars','Name'], ascending=[False, True]).head(5)

out_lines = []
for _, r in top5.iterrows():
    out_lines.append(f"{r['Name']}@{r['Version']} — {int(r['GithubStars'])} GitHub stars")

result = "\n".join(out_lines) if out_lines else "No matching NPM latest-release packages with GitHub star info found."
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Fi1wFc4bNDxpc6JYbInRKORR': 'file_storage/call_Fi1wFc4bNDxpc6JYbInRKORR.json', 'var_call_CTiWb1knml6oh0fz10VSrtOc': 'file_storage/call_CTiWb1knml6oh0fz10VSrtOc.json', 'var_call_nix68Vi01ClSxHYXMRDoDs0U': 'file_storage/call_nix68Vi01ClSxHYXMRDoDs0U.json'}

exec(code, env_args)
