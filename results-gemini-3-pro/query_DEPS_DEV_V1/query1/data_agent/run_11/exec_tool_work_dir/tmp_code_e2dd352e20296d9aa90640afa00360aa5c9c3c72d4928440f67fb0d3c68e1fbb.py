code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-8616037451404184889'], 'r') as f:
    latest_packages = json.load(f)

with open(locals()['var_function-call-1075993615467843555'], 'r') as f:
    project_mapping = json.load(f)

with open(locals()['var_function-call-3451489528784121859'], 'r') as f:
    project_info_list = json.load(f)

# Parse Project Info
project_stars = {}

# Regex patterns
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
    
    # Extract Name
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            p_name = m.group(1)
            break
    
    if not p_name:
        # Fallback or maybe simpler pattern?
        # Sometimes "project <name> on GitHub" might be split?
        # Let's stick to strict patterns for now to avoid false positives.
        continue
        
    # Extract Stars
    stars = 0
    for pat in star_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            s_str = m.group(1).replace(',', '')
            stars = int(s_str)
            break
            
    project_stars[p_name] = stars

# Create Set of Latest Packages for fast lookup
latest_set = set()
for p in latest_packages:
    latest_set.add((p['Name'], p['Version']))

# Filter Mappings
valid_packages = []
for m in project_mapping:
    key = (m['Name'], m['Version'])
    if key in latest_set:
        p_name = m['ProjectName']
        if p_name in project_stars:
            valid_packages.append({
                'Name': m['Name'],
                'Version': m['Version'],
                'Stars': project_stars[p_name],
                'ProjectName': p_name
            })

# Sort by Stars
valid_packages.sort(key=lambda x: x['Stars'], reverse=True)

# Top 5
top_5 = valid_packages[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-12581411140363148776': ['project_info', 'project_packageversion'], 'var_function-call-5315703445904423788': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-6829821427806659043': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-9866817274330198314': [{'count(*)': '661372'}], 'var_function-call-8616037451404184889': 'file_storage/function-call-8616037451404184889.json', 'var_function-call-14431994200503509505': [{'count_star()': '597602'}], 'var_function-call-14320230820370439136': [{'count_star()': '770'}], 'var_function-call-1075993615467843555': 'file_storage/function-call-1075993615467843555.json', 'var_function-call-3451489528784121859': 'file_storage/function-call-3451489528784121859.json'}

exec(code, env_args)
