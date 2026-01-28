code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_3YtepfoY6DOQbUp7I679LURC, 'r') as f:
    latest_list = json.load(f)
with open(var_call_XljJbtTCS6GePb5hPcknw472, 'r') as f:
    ppv_list = json.load(f)
with open(var_call_CCXkdljdiYKlh0GeoI7BTp63, 'r') as f:
    pi_list = json.load(f)

# DataFrames
df_latest = pd.DataFrame(latest_list)
df_ppv = pd.DataFrame(ppv_list)
df_pi = pd.DataFrame(pi_list)

# Keep only GITHUB project types
if 'ProjectType' in df_ppv.columns:
    df_ppv = df_ppv[df_ppv['ProjectType'].str.upper()=='GITHUB']

# Normalize columns
for df in (df_latest, df_ppv):
    if 'System' in df.columns:
        df['System'] = df['System'].astype(str)
    if 'Name' in df.columns:
        df['Name'] = df['Name'].astype(str)
    if 'Version' in df.columns:
        df['Version'] = df['Version'].astype(str)

# Build mapping from project_info entries to project name and stars
proj_stars = {}

patterns_project = [
    re.compile(r'project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', re.IGNORECASE),
    re.compile(r'hosted on GitHub under the name\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', re.IGNORECASE),
    re.compile(r'The GitHub project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', re.IGNORECASE),
    re.compile(r'on GitHub under the name\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', re.IGNORECASE),
]

patterns_stars = [
    re.compile(r'([\d,]+)\s+stars', re.IGNORECASE),
    re.compile(r'stars count of\s*([\d,]+)', re.IGNORECASE),
    re.compile(r'has garnered a total of\s*([\d,]+)\s+stars', re.IGNORECASE),
]

for entry in df_pi['Project_Information'].astype(str):
    project = None
    stars = None
    # extract project name
    for p in patterns_project:
        m = p.search(entry)
        if m:
            project = m.group(1)
            break
    # extract stars
    for p in patterns_stars:
        m = p.search(entry)
        if m:
            stars = int(m.group(1).replace(',',''))
            break
    # fallback: sometimes phrasing like 'currently has 0 open issues, 0 stars, and 0 forks.' we can find '0 stars'
    if not stars:
        m = re.search(r'([\d,]+)\s+stars', entry)
        if m:
            stars = int(m.group(1).replace(',',''))
    if project:
        # store max stars if multiple entries
        if stars is None:
            stars_val = 0
        else:
            stars_val = stars
        if project in proj_stars:
            if stars_val > proj_stars[project]:
                proj_stars[project] = stars_val
        else:
            proj_stars[project] = stars_val

# Merge latest packages with project_packageversion to get ProjectName
merged = pd.merge(df_latest, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

# For packages with no ProjectName, set None
merged['ProjectName'] = merged['ProjectName'].where(merged['ProjectName'].notnull(), None)

# Lookup stars from proj_stars mapping
def lookup_stars(projname):
    if projname is None:
        return 0
    # try direct
    if projname in proj_stars:
        return proj_stars[projname]
    # try variations: some project_info may include owner/repo without case sensitivity
    low = projname.lower()
    for k,v in proj_stars.items():
        if k.lower()==low:
            return v
    return 0

merged['Stars'] = merged['ProjectName'].apply(lookup_stars)

# Some projects may map to multiple rows (duplicates). Group by package name and take max stars and corresponding version/project
grouped = merged.groupby(['Name','Version','ProjectName'], as_index=False)['Stars'].max()

# Now select top 5 by Stars. If tie, sort by Name
top5 = grouped.sort_values(by=['Stars','Name'], ascending=[False,True]).head(5)

# Prepare output list
results = []
for _, row in top5.iterrows():
    results.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'ProjectName': row['ProjectName'] if pd.notna(row['ProjectName']) else None,
        'Stars': int(row['Stars'])
    })

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_3YtepfoY6DOQbUp7I679LURC': 'file_storage/call_3YtepfoY6DOQbUp7I679LURC.json', 'var_call_XljJbtTCS6GePb5hPcknw472': 'file_storage/call_XljJbtTCS6GePb5hPcknw472.json', 'var_call_1N90Xf5wj0JobBvs8tBuww1j': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.', 'Licenses': '[]', 'Description': '基于 Element-UI 二次封装的支持自适应列宽的 table-column 列组件', 'Homepage': 'None'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Get high-quality and customizable Gatsby themes to quickly bootstrap your website! Choose from many professionally created and impressive designs with a wide variety of features and customization options.', 'Homepage': 'https://themes.lekoarts.de'}, {'Project_Information': 'The GitHub project lenconda/dollie currently has 0 open issues, 12 stars, and 3 forks, making it a noteworthy repository in its category.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Dollie is a universal generator to generate anything', 'Homepage': 'https://dollie.lenconda.top'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.', 'Licenses': '[]', 'Description': 'reflect', 'Homepage': 'https://leo-ran.github.io/easy-node-reflect/'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.', 'Licenses': '[]', 'Description': 'server', 'Homepage': 'https://leo-ran.github.io/easy-node-server/'}, {'Project_Information': 'The project named leofelix077/bunchofnothing on GitHub currently has 40 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None'}, {'Project_Information': 'The project leoilab/react-native-analytics-segment-io on GitHub currently has 26 open issues, 71 stars, and 36 forks, making it a notable repository for those interested in integrating analytics into React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'A React Native module for Segment Analytics', 'Homepage': 'None'}, {'Project_Information': 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.', 'Licenses': '[]', 'Description': 'An easy-to-use express server that is extensible using other Easy-Express modules.', 'Homepage': 'None'}, {'Project_Information': 'The project leoroese/template-cli is hosted on GitHub and currently has 1 open issue, along with a total of 17 stars and 13 forks.', 'Licenses': '[]', 'Description': 'A template cli for instatiating projects', 'Homepage': 'None'}, {'Project_Information': 'The project is a GitHub repository named letrungdo/react-ui-component-lib, which currently has 0 open issues, 4 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'How to build component library with react storybook jest enzyme rollup typescript', 'Homepage': 'https://tđ.vn/how-to-build-component-library-with-react-typescript-rollup'}], 'var_call_CCXkdljdiYKlh0GeoI7BTp63': 'file_storage/call_CCXkdljdiYKlh0GeoI7BTp63.json'}

exec(code, env_args)
