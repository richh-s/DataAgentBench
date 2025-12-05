code = """import json, pandas as pd, re

# load full joins and packageinfo
path_pkg = var_call_U0swI4HRIc5HYLD3P6ZbfQDd
path_join = var_call_0MyvK1Oyl0SHuVBuIF0H6xes

with open(path_pkg) as f:
    pkg = json.load(f)
with open(path_join) as f:
    join = json.load(f)

pkg_df = pd.DataFrame(pkg)
join_df = pd.DataFrame(join)

# keep only release versions
def parse_vi(x):
    try:
        return json.loads(x)
    except Exception:
        return {}

vi = pkg_df['VersionInfo'].apply(parse_vi)
pkg_df['IsRelease'] = vi.apply(lambda d: d.get('IsRelease'))
pkg_df['Ordinal'] = vi.apply(lambda d: d.get('Ordinal', -1))

pkg_rel = pkg_df[pkg_df['IsRelease'] == True]

# latest release per package name (NPM only already)
idx = pkg_rel.groupby('Name')['Ordinal'].idxmax()
latest_pkg = pkg_rel.loc[idx, ['Name','Version']].rename(columns={'Version':'LatestVersion'})

# join with project_packageversion+info
merged = pd.merge(join_df, latest_pkg, how='inner', left_on=['Name','Version'], right_on=['Name','LatestVersion'])

# extract stars from Project_Information
star_counts = []
for txt in merged['Project_Information']:
    m = re.search(r"(\d[\d,]*) stars", txt)
    if m:
        star = int(m.group(1).replace(',', ''))
    else:
        star = None
    star_counts.append(star)
merged['Stars'] = star_counts

merged = merged.dropna(subset=['Stars'])

# sort by stars desc and pick top 5 distinct packages
merged = merged.sort_values('Stars', ascending=False)
seen = set()
rows = []
for _, r in merged.iterrows():
    name = r['Name']
    if name in seen:
        continue
    seen.add(name)
    rows.append({'Name': name, 'Version': r['Version'], 'Stars': int(r['Stars'])})
    if len(rows) == 5:
        break

result = json.dumps(rows)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_U0swI4HRIc5HYLD3P6ZbfQDd': 'file_storage/call_U0swI4HRIc5HYLD3P6ZbfQDd.json', 'var_call_Oo7JpYO1s9PaYfS24lVlDmNi': [], 'var_call_4l0EAE1jWwRJmWdo1rnvAnIa': ['project_info', 'project_packageversion'], 'var_call_xW34suPdHHJ5SmaIINSOSVCk': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_9m5yAa2snXUZLCQjyxm6sbtk': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_call_0MyvK1Oyl0SHuVBuIF0H6xes': 'file_storage/call_0MyvK1Oyl0SHuVBuIF0H6xes.json'}

exec(code, env_args)
