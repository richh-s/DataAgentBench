code = """import json, re, pandas as pd, ast
from pathlib import Path

# Load full project_info
pi_path = Path(var_call_ejmb44MPjpr93TqNXNodpVXG)
with pi_path.open() as f:
    project_info = json.load(f)

rows = []
for rec in project_info:
    text = rec.get('Project_Information','')
    m_repo = re.search(r'project\s+([^\s]+/[^\s]+)', text)
    m_stars = re.search(r'(?:has|have|with)[^\.]*?([0-9,]+)\s+stars', text)
    if m_repo and m_stars:
        repo = m_repo.group(1).rstrip(',')
        stars = int(m_stars.group(1).replace(',',''))
        rows.append({'ProjectName': repo, 'Stars': stars})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

# Reload previous join data
pkg_path = Path(var_call_FAkwhCIksf6jnMIV6xVxkSr9)
with pkg_path.open() as f:
    packageinfo = json.load(f)
ppv_path = Path(var_call_i78NZ1MzeRNVx1JnNvPHXTC7)
with ppv_path.open() as f:
    project_packageversion = json.load(f)

pkg_df = pd.DataFrame(packageinfo)[['System','Name','Version','VersionInfo']]
ppv_df = pd.DataFrame(project_packageversion)[['System','Name','Version','ProjectName']]

# Parse VersionInfo

def parse_vi(s):
    try:
        return ast.literal_eval(s) if isinstance(s,str) else {}
    except Exception:
        return {}

vi = pkg_df['VersionInfo'].apply(parse_vi)
pkg_df['IsRelease'] = vi.apply(lambda d: d.get('IsRelease', True))
pkg_df['Ordinal'] = vi.apply(lambda d: d.get('Ordinal', 0))

npm_df = pkg_df[pkg_df['System']=='NPM'].copy()
releases = npm_df[npm_df['IsRelease']==True]
if releases.empty:
    cand = npm_df
else:
    cand = releases

cand_sorted = cand.sort_values(['Name','Ordinal'])
latest_pkg = cand_sorted.groupby('Name', as_index=False).tail(1)[['System','Name','Version']]

merged = latest_pkg.merge(ppv_df, on=['System','Name','Version'], how='inner')
merged_pi = merged.merge(pi_df, on='ProjectName', how='inner')

merged_pi_sorted = merged_pi.sort_values(['Stars','Name'], ascending=[False,True])
latest_by_name = merged_pi_sorted.groupby('Name', as_index=False).head(1)

top5 = latest_by_name.head(5)[['Name','Version','Stars']]

out = json.dumps(top5.to_dict(orient='records'))
print('__RESULT__:')
print(out)"""

env_args = {'var_call_FAkwhCIksf6jnMIV6xVxkSr9': 'file_storage/call_FAkwhCIksf6jnMIV6xVxkSr9.json', 'var_call_i78NZ1MzeRNVx1JnNvPHXTC7': 'file_storage/call_i78NZ1MzeRNVx1JnNvPHXTC7.json', 'var_call_yfLcLVspvZwxBVCpjCzcyA9H': {'project_names_sample': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0x6c38/srp', '0x6c38/srt', '0xsalah/tete', '1394/manipula', '1394/model', '1728954833/project-manager'], 'count_projects': 7853}, 'var_call_ejmb44MPjpr93TqNXNodpVXG': 'file_storage/call_ejmb44MPjpr93TqNXNodpVXG.json'}

exec(code, env_args)
