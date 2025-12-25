code = """import json, re, pandas as pd

with open(var_call_t7QoMHJh2UbiJzomHxSdltR4, 'r') as f:
    rows = json.load(f)

df = pd.DataFrame(rows)

# Extract repo name and stars from Project_Information
repo_pat = re.compile(r"The project ([^ ]+/[^ ]+)\b")
stars_pat = re.compile(r"(\d[\d,]*) stars")

repos = []
stars = []
for txt in df['Project_Information']:
    m1 = repo_pat.search(txt)
    m2 = stars_pat.search(txt)
    if m1 and m2:
        repos.append(m1.group(1))
        stars.append(int(m2.group(1).replace(',', '')))
    else:
        repos.append(None)
        stars.append(None)

info_df = pd.DataFrame({'ProjectName': repos, 'Stars': stars})
info_df = info_df.dropna()

# Get a sense of top starred projects overall
top_projects = info_df.sort_values('Stars', ascending=False).head(20).to_dict(orient='records')

import json as _json
print("__RESULT__:")
print(_json.dumps({'top_projects_overall': top_projects}))"""

env_args = {'var_call_WUzblKxX0PvPpqAosn3KpCm4': [], 'var_call_11MCSTwt3FMxRXwBMl0nGBgq': 'file_storage/call_11MCSTwt3FMxRXwBMl0nGBgq.json', 'var_call_YdQ1Pp2XtlWJFtFsBkwd6YZ0': ['project_info', 'project_packageversion'], 'var_call_pg0Kb5g8s39DLBItfDhCPvjI': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_u8tojOdQCGAVwrg1b3yzwSHb': 'file_storage/call_u8tojOdQCGAVwrg1b3yzwSHb.json', 'var_call_n1DxkPcduzfXhl4Z5DpH6msF': 'file_storage/call_n1DxkPcduzfXhl4Z5DpH6msF.json', 'var_call_J2Yu5g0NlEC7dvL4J3QBTwEx': {'latest_pkg_sample': [{'System': 'NPM', 'Name': '@dmail/object-clone', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@dmail/object-define', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@dmail/object-is', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@dmail/object-merge', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@dmail/property', 'Version': '0.0.1'}], 'merged_sample': [{'System': 'NPM', 'Name': '@dmail/object-define', 'Version': '0.0.1', 'ProjectName': 'dmail/object-define'}, {'System': 'NPM', 'Name': '@dmail/property', 'Version': '0.0.1', 'ProjectName': 'dmail/property'}, {'System': 'NPM', 'Name': '@dmail/iterator-filter', 'Version': '0.0.1', 'ProjectName': 'dmail/iterator-filter'}, {'System': 'NPM', 'Name': '@eddieajau/shell', 'Version': '0.2.1', 'ProjectName': 'eddieajau/node-shell'}, {'System': 'NPM', 'Name': '@dpwolfe/grunt-compc', 'Version': '1.1.5', 'ProjectName': 'artema/grunt-compc'}], 'project_names_sample': ['dmail/object-define', 'dmail/property', 'dmail/iterator-filter', 'eddieajau/node-shell', 'artema/grunt-compc', 'dominykas/test-two', 'dragosh/node-ally', 'dschnare/signalsjs', 'dtrussia/react-pager', 'casesandberg/react-color']}, 'var_call_t7QoMHJh2UbiJzomHxSdltR4': 'file_storage/call_t7QoMHJh2UbiJzomHxSdltR4.json'}

exec(code, env_args)
