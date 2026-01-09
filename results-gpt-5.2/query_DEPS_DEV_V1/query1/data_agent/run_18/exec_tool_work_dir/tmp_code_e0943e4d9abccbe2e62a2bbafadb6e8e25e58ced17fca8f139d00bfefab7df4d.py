code = """import json, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_EksUhU1xiPQrFqfdLOVJVIbg)
ppv = load(var_call_b0aW5QJqLdpcS6Osu14vkirC)
pi = load(var_call_NjLXcy3XFwhltqubXOvRhPGY)

pkg_df = pd.DataFrame(pkg)
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
pkg_df = pkg_df.dropna(subset=['UpstreamPublishedAt'])
pkg_df = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False])
latest = pkg_df.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]

ppv_df = pd.DataFrame(ppv)[['Name','Version','ProjectName']].dropna()

# parse project_info
import re
name_re = re.compile(r'project(?:\s+named)?\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)', re.I)
stars_re = re.compile(r'(\d+[\d,]*)\s+stars', re.I)
rows=[]
for rec in pi:
    s = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not s:
        continue
    mn = name_re.search(s)
    ms = stars_re.search(s)
    if mn and ms:
        rows.append({'ProjectName': mn.group(1), 'Stars': int(ms.group(1).replace(',',''))})
proj_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'], keep='first')

merged = latest.merge(ppv_df, on=['Name','Version'], how='inner')
merged = merged.merge(proj_df, on='ProjectName', how='inner')
# keep max stars per package (in case multiple repos)
merged = merged.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')

top5 = merged.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
out = top5[['Name','Version','Stars','ProjectName']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6uggoPVDtK2VSjqJ1z9HzbHl': ['packageinfo'], 'var_call_hSF0CM4usTrZKTgQznJUgOim': ['project_info', 'project_packageversion'], 'var_call_EksUhU1xiPQrFqfdLOVJVIbg': 'file_storage/call_EksUhU1xiPQrFqfdLOVJVIbg.json', 'var_call_b0aW5QJqLdpcS6Osu14vkirC': 'file_storage/call_b0aW5QJqLdpcS6Osu14vkirC.json', 'var_call_NjLXcy3XFwhltqubXOvRhPGY': 'file_storage/call_NjLXcy3XFwhltqubXOvRhPGY.json', 'var_call_7pRH6XMB4EEFZrXa77geByhQ': {'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt'], 'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'proj_cols': [], 'proj_sample': []}, 'var_call_2aa6PKgYXIdcoS2eytfAPdtW': {'n': 0, 'sample': []}, 'var_call_Z0xDwkxmk1V5XgpQujN731fR': {'count': 770, 'examples': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.']}, 'var_call_AZMOSUpiyyVZa5D6jBbwaEUJ': [{'cands': [], 'stars': '0', 'text': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'cands': [], 'stars': '38715', 'text': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'cands': [], 'stars': '417', 'text': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}], 'var_call_O31rW6lWPvkVfIIy29zQXmPD': {'n': 550, 'sample': [{'ProjectName': 'mui-org/material-ui', 'Stars': 89398}, {'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'ProjectName': 'quilljs/quill', 'Stars': 42407}]}}

exec(code, env_args)
