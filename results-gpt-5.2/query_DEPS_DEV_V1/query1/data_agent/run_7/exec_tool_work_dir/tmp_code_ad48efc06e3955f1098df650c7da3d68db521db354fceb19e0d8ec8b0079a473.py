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

repo_re = re.compile(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
star_re = re.compile(r'([0-9][0-9,]*)\s+stars', re.IGNORECASE)

rows=[]
for rec in pi:
    s = rec.get('Project_Information') or ''
    m_repo = repo_re.search(s)
    m_star = star_re.search(s)
    if not (m_repo and m_star):
        continue
    rows.append({'ProjectName': m_repo.group(1), 'Stars': int(m_star.group(1).replace(',',''))})
pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

j2 = j.merge(pi_df, on='ProjectName', how='inner')

agg = j2.groupby(['Name','Version'], as_index=False)['Stars'].max()

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

print('__RESULT__:')
print(json.dumps(top5.to_dict(orient='records')))"""

env_args = {'var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7': 'file_storage/call_Z2uGzLu5Ia6ztPh0oPzFXIP7.json', 'var_call_1QGSqqyNDZo8Y66QbYUHuHcC': 'file_storage/call_1QGSqqyNDZo8Y66QbYUHuHcC.json', 'var_call_BNfD7Iir4yoYI4yI3g4ncWcN': 'file_storage/call_BNfD7Iir4yoYI4yI3g4ncWcN.json', 'var_call_H34KjCVgIe3d3GiJKx7oftTE': {'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt']}, 'var_call_zHDlviuT3CoNrsEJ5d57gYia': {'j_cols': ['Name', 'Version', 'UpstreamPublishedAt', 'System', 'ProjectName'], 'j_head': [{'Name': '@discordx/music', 'Version': '6.0.2', 'UpstreamPublishedAt': 1687719264000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'UpstreamPublishedAt': 1687719264000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'UpstreamPublishedAt': 1677444438000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}]}, 'var_call_SDWyjt3izuereIjVjcwni6lk': {'j_cols': ['Name', 'Version', 'UpstreamPublishedAt', 'System', 'ProjectName'], 'pi_cols': [], 'pi_empty': True}, 'var_call_DXqiDT85lec4G3rUs2E4ub2Y': {'first_len': 770, 'example_found': False, 'example': None, 'first10': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.']}, 'var_call_wPRbz6WTRbvXqcprxDdeo66i': {'parsed': 0, 'sample': []}, 'var_call_Z66vkyi68payBgTsPjC4mjkB': {'s': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'segment': 'ject leaflet/leaflet on G', 'codes': [106, 101, 99, 116, 32, 108, 101, 97, 102, 108, 101, 116, 47, 108, 101, 97, 102, 108, 101, 116, 32, 111, 110, 32, 71]}, 'var_call_qwHIx74zamL7ylBETCiBKpdo': {'repo': None, 'stars': None}, 'var_call_D5zDau3tTIie3nwIQXHkwbq4': {'repo': 'leaflet/leaflet', 'stars': '38715'}}

exec(code, env_args)
