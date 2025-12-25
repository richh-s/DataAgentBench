code = """import json
import re

# Load data
with open(locals()['var_function-call-8616037451404184889'], 'r') as f:
    latest_packages = json.load(f) # List of {Name, Version}

with open(locals()['var_function-call-1075993615467843555'], 'r') as f:
    project_mapping = json.load(f) # List of {Name, Version, ProjectName}

with open(locals()['var_function-call-3451489528784121859'], 'r') as f:
    project_info_list = json.load(f) # List of {Project_Information}

# Parse Project Info
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
    if not text:
        continue
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
                s_str = m.group(1).replace(',', '')
                stars = int(s_str)
                break
        project_stars[p_name] = stars

# Create dict for latest packages: Name -> Version
latest_map = {p['Name']: p['Version'] for p in latest_packages}

# Process mappings
# We want to link latest package -> project -> stars
package_stars = []
seen_packages = set()

for m in project_mapping:
    name = m['Name']
    version = m['Version']
    
    # Check if this is the latest version
    if name in latest_map and latest_map[name] == version:
        # Check if we have project info
        p_name = m['ProjectName']
        if p_name in project_stars:
            # We found a match
            # If we haven't processed this PACKAGE Name yet?
            # Wait, one package might map to multiple projects?
            # Or project_mapping duplicates?
            # We should collect all candidates and then dedup.
            stars = project_stars[p_name]
            package_stars.append({
                'Name': name,
                'Version': version,
                'Stars': stars,
                'ProjectName': p_name
            })

# Convert to dataframe to handle duplicates easily
import pandas as pd
df = pd.DataFrame(package_stars)

# Drop duplicates
# A package (Name, Version) might map to multiple projects (unlikely but possible) or same project multiple times.
# We want distinct packages. If a package maps to multiple projects, which star count to take?
# Usually maps to one. If multiple, maybe take max?
if not df.empty:
    df = df.sort_values('Stars', ascending=False)
    df = df.drop_duplicates(subset=['Name', 'Version'])
    top_10 = df.head(10).to_dict(orient='records')
else:
    top_10 = []

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-12581411140363148776': ['project_info', 'project_packageversion'], 'var_function-call-5315703445904423788': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-6829821427806659043': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-9866817274330198314': [{'count(*)': '661372'}], 'var_function-call-8616037451404184889': 'file_storage/function-call-8616037451404184889.json', 'var_function-call-14431994200503509505': [{'count_star()': '597602'}], 'var_function-call-14320230820370439136': [{'count_star()': '770'}], 'var_function-call-1075993615467843555': 'file_storage/function-call-1075993615467843555.json', 'var_function-call-3451489528784121859': 'file_storage/function-call-3451489528784121859.json', 'var_function-call-2191318420744046977': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dolsem/actioncable', 'Version': '7.0.0-alpha-simple-5s-step-backoff', 'Stars': 55319, 'ProjectName': 'rails/rails'}]}

exec(code, env_args)
