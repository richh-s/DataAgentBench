code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7)
ppv = load_records(var_call_1QGSqqyNDZo8Y66QbYUHuHcC)
pi = load_records(var_call_BNfD7Iir4yoYI4yI3g4ncWcN)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest_df = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
             .groupby('Name', as_index=False)
             .tail(1)
             .loc[:, ['Name','Version','UpstreamPublishedAt']]
             .copy())
latest_df['System'] = 'NPM'

j = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

rows=[]
star_re = re.compile(r'\b([0-9][0-9,]*)\s+stars\b', re.IGNORECASE)
repo_re = re.compile(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')
for rec in pi:
    s = rec.get('Project_Information') or ''
    m_repo = repo_re.search(s)
    m_star = star_re.search(s)
    if not (m_repo and m_star):
        continue
    rows.append({'ProjectName': m_repo.group(1), 'Stars': int(m_star.group(1).replace(',',''))})
pi_df = pd.DataFrame(rows)

print('__RESULT__:')
print(json.dumps({'j_cols': list(j.columns), 'pi_cols': list(pi_df.columns), 'pi_empty': bool(pi_df.empty)}))"""

env_args = {'var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7': 'file_storage/call_Z2uGzLu5Ia6ztPh0oPzFXIP7.json', 'var_call_1QGSqqyNDZo8Y66QbYUHuHcC': 'file_storage/call_1QGSqqyNDZo8Y66QbYUHuHcC.json', 'var_call_BNfD7Iir4yoYI4yI3g4ncWcN': 'file_storage/call_BNfD7Iir4yoYI4yI3g4ncWcN.json', 'var_call_H34KjCVgIe3d3GiJKx7oftTE': {'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt']}, 'var_call_zHDlviuT3CoNrsEJ5d57gYia': {'j_cols': ['Name', 'Version', 'UpstreamPublishedAt', 'System', 'ProjectName'], 'j_head': [{'Name': '@discordx/music', 'Version': '6.0.2', 'UpstreamPublishedAt': 1687719264000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'UpstreamPublishedAt': 1687719264000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'UpstreamPublishedAt': 1677444438000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}]}}

exec(code, env_args)
