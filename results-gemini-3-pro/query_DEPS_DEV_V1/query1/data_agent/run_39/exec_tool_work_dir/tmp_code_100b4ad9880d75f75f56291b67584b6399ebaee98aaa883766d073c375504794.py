code = """import json
import re
import pandas as pd

# 1. Parse Project Info for Stars
file_path_info = locals()['var_function-call-17095026802948898039']
with open(file_path_info, 'r') as f:
    project_info_list = json.load(f)

project_stars = {}
name_patterns = [
    r"The project ([^\s]+) (?:on GitHub|is hosted on GitHub|is hosted on GITHUB)",
    r"The GitHub project ([^\s]+) currently",
    r"The GitHub project named ([^\s]+) currently",
    r"The project named ([^\s]+) on GitHub",
    r"The project named ([^\s]+) is hosted",
    r"The project is hosted on GitHub under the name ([^\s,]+)",
    r"The project on GitHub, named ([^\s,]+),",
    r"The project ([^\s]+) has"
]
star_pattern = r"(\d+(?:,\d+)*) stars"

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    star_match = re.search(star_pattern, text)
    stars = int(star_match.group(1).replace(',', '')) if star_match else 0
    
    name = None
    for pat in name_patterns:
        match = re.search(pat, text)
        if match:
            name = match.group(1).rstrip(',')
            if '/' in name: break
    if name:
        project_stars[name] = stars

# 2. Filter Project Package Version
file_path_map = locals()['var_function-call-2730800807703072015']
with open(file_path_map, 'r') as f:
    mapping_list = json.load(f)

# Filter mapping where ProjectName is in project_stars
relevant_packages = []
unique_names = set()

for row in mapping_list:
    proj = row.get('ProjectName')
    if proj in project_stars:
        relevant_packages.append(row)
        unique_names.add(row.get('Name'))

# Save relevant_packages to a file to use later? 
# Or just pass the unique names to the next step. 
# I'll print the unique names to query DB.

print("__RESULT__:")
print(json.dumps(list(unique_names)))"""

env_args = {'var_function-call-3426217086508878109': ['project_info', 'project_packageversion'], 'var_function-call-14361327731076746203': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-802867660549840356': [{'COUNT(*)': '661372'}], 'var_function-call-17118522439532025906': [{'count_star()': '770'}], 'var_function-call-13698533078275415391': [{'count_star()': '597602'}], 'var_function-call-17095026802948898039': 'file_storage/function-call-17095026802948898039.json', 'var_function-call-2683278215389969689': 'file_storage/function-call-2683278215389969689.json', 'var_function-call-2730800807703072015': 'file_storage/function-call-2730800807703072015.json'}

exec(code, env_args)
