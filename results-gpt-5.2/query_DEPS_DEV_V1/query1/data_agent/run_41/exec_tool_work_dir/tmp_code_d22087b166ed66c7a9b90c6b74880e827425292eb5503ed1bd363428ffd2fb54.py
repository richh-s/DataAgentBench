code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_records(var_call_LajdCAPb2uSJ0SAz2kAU0WNQ)
pi_pkg = load_records(var_call_1wT6UAnDXOxcDNXdx6YiPsiG)
pi_proj = load_records(var_call_vIQvk5bGQo5Ph1wraClQmUfy)

ppv_df = pd.DataFrame(ppv)
pkg_df = pd.DataFrame(pi_pkg)
proj_df = pd.DataFrame(pi_proj)

# filter to real NPM package names (exclude dependency path names containing '>')
ppv_df = ppv_df[(ppv_df['System']=='NPM') & (~ppv_df['Name'].astype(str).str.contains('>', regex=False))].copy()
pkg_df = pkg_df[(pkg_df['System']=='NPM') & (~pkg_df['Name'].astype(str).str.contains('>', regex=False))].copy()

# latest release per package by VersionInfo.Ordinal
rows=[]
for r in pkg_df.to_dict('records'):
    vi=r.get('VersionInfo')
    isrel=False
    ordv=None
    if isinstance(vi,str):
        try:
            o=json.loads(vi)
            isrel=bool(o.get('IsRelease'))
            ordv=o.get('Ordinal')
        except Exception:
            pass
    rows.append((r.get('System'), r.get('Name'), r.get('Version'), isrel, ordv))
rel_df=pd.DataFrame(rows, columns=['System','Name','Version','IsRelease','Ordinal'])
rel_df=rel_df[(rel_df['System']=='NPM') & (rel_df['IsRelease']==True)].copy()
rel_df['Ordinal']=pd.to_numeric(rel_df['Ordinal'], errors='coerce')
rel_df=rel_df.dropna(subset=['Ordinal'])
latest=rel_df.sort_values(['Name','Ordinal'], ascending=[True,False]).drop_duplicates(['System','Name'], keep='first')

join_df=latest.merge(ppv_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
join_df=join_df.dropna(subset=['ProjectName'])

# project stars parsing

def parse_owner_repo(text):
    if not isinstance(text,str):
        return None
    m=re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', text)
    return m.group(1) if m else None

def parse_stars(text):
    if not isinstance(text,str):
        return None
    m=re.search(r'([0-9][0-9,]*)\s+stars', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    return None

proj_df2=proj_df.copy()
proj_df2['Repo']=proj_df2['Project_Information'].apply(parse_owner_repo)
proj_df2['Stars']=proj_df2['Project_Information'].apply(parse_stars)
repo_stars=proj_df2[['Repo','Stars']].dropna(subset=['Repo','Stars']).drop_duplicates('Repo')

final=join_df.rename(columns={'ProjectName':'Repo'}).merge(repo_stars, on='Repo', how='left')
final=final.dropna(subset=['Stars'])
final['Stars']=pd.to_numeric(final['Stars'], errors='coerce')
final=final.dropna(subset=['Stars'])

# if multiple packages map to same repo, keep highest star but list per package; for top 5 packages, sort by Stars
out=final.sort_values(['Stars','Name'], ascending=[False, True]).drop_duplicates(['Name'], keep='first').head(5)
res=out[['Name','Version','Repo','Stars']].to_dict('records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_LajdCAPb2uSJ0SAz2kAU0WNQ': 'file_storage/call_LajdCAPb2uSJ0SAz2kAU0WNQ.json', 'var_call_1wT6UAnDXOxcDNXdx6YiPsiG': 'file_storage/call_1wT6UAnDXOxcDNXdx6YiPsiG.json', 'var_call_KKvwj99qU3IZ0eecUYNC9Fr4': ['project_info', 'project_packageversion'], 'var_call_xrPfzgfEouypZYLKHF9PnS3g': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_vIQvk5bGQo5Ph1wraClQmUfy': 'file_storage/call_vIQvk5bGQo5Ph1wraClQmUfy.json', 'var_call_aceBuxNJuGvxAOKEvO96S8RZ': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Repo': 'sveltejs/svelte', 'Stars': 73499.0}], 'var_call_DXH1jpFT0sEeTLcR43Gy3ATm': [{'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Repo': 'sveltejs/svelte', 'Stars': 73499.0}, {'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Repo': 'microsoft/typescript', 'Stars': 94931.0}]}

exec(code, env_args)
