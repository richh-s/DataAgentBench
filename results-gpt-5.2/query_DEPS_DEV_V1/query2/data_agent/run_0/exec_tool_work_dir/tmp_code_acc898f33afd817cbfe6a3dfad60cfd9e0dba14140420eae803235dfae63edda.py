code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_maybe_path(var_call_eJlz4VYzf6heD9o9PrvGcslC)
ppv = load_maybe_path(var_call_jDVr2ZJVmahXRYCaRfp98Mq5)
pi = load_maybe_path(var_call_SIxKnWW64nhDPffr7K0F6gn9)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(m['ProjectName'].dropna().astype(str).tolist())

rows=[]
pat = re.compile(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?(\d[\d,]*)\s+forks?", re.IGNORECASE)
for rec in pi:
    s = rec.get('Project_Information') or ''
    mm = pat.search(s)
    if not mm:
        continue
    proj = mm.group(1)
    if proj not in projects:
        continue
    forks = int(mm.group(2).replace(',',''))
    rows.append({'ProjectName': proj, 'Forks': forks})

df = pd.DataFrame(rows)
if df.empty:
    top5=[]
else:
    df = df.drop_duplicates('ProjectName')
    df = df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    top5 = df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'matched_projects_with_forks': int(len(rows)), 'top5': top5}))"""

env_args = {'var_call_9LuYGPEF3wSPIlKvs17sqBgA': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_5jcuITIvnx98ITroDUEkpbFS': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_call_eJlz4VYzf6heD9o9PrvGcslC': 'file_storage/call_eJlz4VYzf6heD9o9PrvGcslC.json', 'var_call_jDVr2ZJVmahXRYCaRfp98Mq5': 'file_storage/call_jDVr2ZJVmahXRYCaRfp98Mq5.json', 'var_call_bFFzYHjdNqcgOCl39JIHoZ2L': {'need_project_info_full': True, 'unique_projects': 5289}, 'var_call_SIxKnWW64nhDPffr7K0F6gn9': 'file_storage/call_SIxKnWW64nhDPffr7K0F6gn9.json'}

exec(code, env_args)
