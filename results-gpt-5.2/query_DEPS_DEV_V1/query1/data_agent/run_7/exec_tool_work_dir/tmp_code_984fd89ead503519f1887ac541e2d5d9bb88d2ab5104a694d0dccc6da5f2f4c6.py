code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_records(var_call_BNfD7Iir4yoYI4yI3g4ncWcN)

# adjusted repo regex to allow deeper paths but capture owner/repo; handle dot in repo
repo_re = re.compile(r'\b([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)\b')
star_re = re.compile(r'\b([0-9][0-9,]*)\s+stars\b', re.IGNORECASE)

rows=[]
for rec in pi:
    s = rec.get('Project_Information') or ''
    m_star = star_re.search(s)
    m_repo = repo_re.search(s)
    if not (m_star and m_repo):
        continue
    owner, repo = m_repo.group(1), m_repo.group(2)
    rows.append({'ProjectName': owner + '/' + repo, 'Stars': int(m_star.group(1).replace(',',''))})

print('__RESULT__:')
print(json.dumps({'parsed': len(rows), 'sample': rows[:5]}))"""

env_args = {'var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7': 'file_storage/call_Z2uGzLu5Ia6ztPh0oPzFXIP7.json', 'var_call_1QGSqqyNDZo8Y66QbYUHuHcC': 'file_storage/call_1QGSqqyNDZo8Y66QbYUHuHcC.json', 'var_call_BNfD7Iir4yoYI4yI3g4ncWcN': 'file_storage/call_BNfD7Iir4yoYI4yI3g4ncWcN.json', 'var_call_H34KjCVgIe3d3GiJKx7oftTE': {'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt']}, 'var_call_zHDlviuT3CoNrsEJ5d57gYia': {'j_cols': ['Name', 'Version', 'UpstreamPublishedAt', 'System', 'ProjectName'], 'j_head': [{'Name': '@discordx/music', 'Version': '6.0.2', 'UpstreamPublishedAt': 1687719264000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'UpstreamPublishedAt': 1687719264000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'UpstreamPublishedAt': 1677444438000000.0, 'System': 'NPM', 'ProjectName': 'discordx-ts/discordx'}]}, 'var_call_SDWyjt3izuereIjVjcwni6lk': {'j_cols': ['Name', 'Version', 'UpstreamPublishedAt', 'System', 'ProjectName'], 'pi_cols': [], 'pi_empty': True}, 'var_call_DXqiDT85lec4G3rUs2E4ub2Y': {'first_len': 770, 'example_found': False, 'example': None, 'first10': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.']}}

exec(code, env_args)
