code = """import json
import pandas as pd

# Load previous results (I can just re-run the logic or if I stored it... I didn't store the df)
# I'll quickly re-run the logic

with open(locals()['var_function-call-8616037451404184889'], 'r') as f:
    latest_packages = json.load(f)
with open(locals()['var_function-call-1075993615467843555'], 'r') as f:
    project_mapping = json.load(f)
with open(locals()['var_function-call-3451489528784121859'], 'r') as f:
    project_info_list = json.load(f)

# Parse stars
import re
project_stars = {}
name_patterns = [
    r"project\s+([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)\s+(?:on|is hosted on)\s+(?:GitHub|GITHUB)",
    r"(?:GitHub|GITHUB)\s+project\s+(?:named\s+)?([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)",
    r"hosted on (?:GitHub|GITHUB) under the name\s+([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)"
]
star_patterns = [
    r"(\d+(?:,\d+)*)\s+stars",
    r"stars\s+count\s+of\s+(\d+(?:,\d+)*)",
    r"total\s+of\s+(\d+(?:,\d+)*)\s+stars"
]
for entry in project_info_list:
    text = entry['Project_Information']
    if not text: continue
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            p_name = m.group(1)
            break
    if p_name:
        stars = 0
        for pat in star_patterns:
            m = re.search(pat, text, re.IGNORECASE)
            if m:
                stars = int(m.group(1).replace(',', ''))
                break
        project_stars[p_name] = stars

# Map
latest_map = {p['Name']: p['Version'] for p in latest_packages}
package_stars = []
for m in project_mapping:
    if m['Name'] in latest_map and latest_map[m['Name']] == m['Version']:
        if m['ProjectName'] in project_stars:
            package_stars.append({
                'Name': m['Name'],
                'Version': m['Version'],
                'Stars': project_stars[m['ProjectName']],
                'ProjectName': m['ProjectName']
            })

df = pd.DataFrame(package_stars)
if not df.empty:
    df = df.sort_values('Stars', ascending=False)
    df = df.drop_duplicates(subset=['Name', 'Version'])
    # Check top 10
    print("__RESULT__:")
    print(df.head(10).to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-12581411140363148776': ['project_info', 'project_packageversion'], 'var_function-call-5315703445904423788': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-6829821427806659043': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-9866817274330198314': [{'count(*)': '661372'}], 'var_function-call-8616037451404184889': 'file_storage/function-call-8616037451404184889.json', 'var_function-call-14431994200503509505': [{'count_star()': '597602'}], 'var_function-call-14320230820370439136': [{'count_star()': '770'}], 'var_function-call-1075993615467843555': 'file_storage/function-call-1075993615467843555.json', 'var_function-call-3451489528784121859': 'file_storage/function-call-3451489528784121859.json', 'var_function-call-2191318420744046977': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dolsem/actioncable', 'Version': '7.0.0-alpha-simple-5s-step-backoff', 'Stars': 55319, 'ProjectName': 'rails/rails'}], 'var_function-call-1146815390494191088': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dolsem/actioncable', 'Version': '7.0.0-alpha-simple-5s-step-backoff', 'Stars': 55319, 'ProjectName': 'rails/rails'}, {'Name': '@dreampie/semantic-ui', 'Version': '2.2.11', 'Stars': 51069, 'ProjectName': 'semantic-org/semantic-ui'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407, 'ProjectName': 'quilljs/quill'}, {'Name': '@dothq/styled-components', 'Version': '6.0.2-prealpha-dot', 'Stars': 39660, 'ProjectName': 'styled-components/styled-components'}, {'Name': '@dynasty/styled-components', 'Version': '3.2.1', 'Stars': 39660, 'ProjectName': 'styled-components/styled-components'}, {'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'Stars': 38715, 'ProjectName': 'leaflet/leaflet'}, {'Name': '@docid/monaco-editor', 'Version': '0.31.1-x1', 'Stars': 36025, 'ProjectName': 'microsoft/monaco-editor'}, {'Name': '@dudadev/mobx-react', 'Version': '6.1.12', 'Stars': 26802, 'ProjectName': 'mobxjs/mobx'}], 'var_function-call-2716806948898725562': {'svelte': {'in_latest': False, 'in_mapping': False}, 'tailwindcss': {'in_latest': False, 'in_mapping': False}, 'rails': {'in_latest': False, 'in_mapping': False}, 'semantic-ui': {'in_latest': False, 'in_mapping': False}, 'quill': {'in_latest': False, 'in_mapping': False}}}

exec(code, env_args)
