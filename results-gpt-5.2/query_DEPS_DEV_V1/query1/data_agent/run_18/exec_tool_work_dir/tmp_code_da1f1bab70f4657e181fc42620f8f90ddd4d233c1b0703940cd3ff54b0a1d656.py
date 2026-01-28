code = """import json, re

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pi = load(var_call_NjLXcy3XFwhltqubXOvRhPGY)
star_re = re.compile(r'\b([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)\b')
stars_re = re.compile(r'(\d+[\d,]*)\s+stars')

hits=[]
for rec in pi[:5000]:
    s = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not s:
        continue
    mstars = stars_re.search(s)
    if mstars:
        cands = star_re.findall(s)
        hits.append({'cands': cands[:3], 'stars': mstars.group(1), 'text': s})
        if len(hits)>=3:
            break

print('__RESULT__:')
print(json.dumps(hits))"""

env_args = {'var_call_6uggoPVDtK2VSjqJ1z9HzbHl': ['packageinfo'], 'var_call_hSF0CM4usTrZKTgQznJUgOim': ['project_info', 'project_packageversion'], 'var_call_EksUhU1xiPQrFqfdLOVJVIbg': 'file_storage/call_EksUhU1xiPQrFqfdLOVJVIbg.json', 'var_call_b0aW5QJqLdpcS6Osu14vkirC': 'file_storage/call_b0aW5QJqLdpcS6Osu14vkirC.json', 'var_call_NjLXcy3XFwhltqubXOvRhPGY': 'file_storage/call_NjLXcy3XFwhltqubXOvRhPGY.json', 'var_call_7pRH6XMB4EEFZrXa77geByhQ': {'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt'], 'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'proj_cols': [], 'proj_sample': []}, 'var_call_2aa6PKgYXIdcoS2eytfAPdtW': {'n': 0, 'sample': []}, 'var_call_Z0xDwkxmk1V5XgpQujN731fR': {'count': 770, 'examples': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.']}}

exec(code, env_args)
