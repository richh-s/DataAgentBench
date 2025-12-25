code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-5253085552876619836'], 'r') as f:
    project_info_data = json.load(f)

with open(locals()['var_function-call-13209268095735794685'], 'r') as f:
    package_info_data = json.load(f)

with open(locals()['var_function-call-13209268095735792616'], 'r') as f:
    mapping_data = json.load(f)

# Process Project Info
proj_list = []
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    
    # Extract Stars
    stars = 0
    star_match = re.search(r'(?:(\d{1,3}(?:,\d{3})*|\d+)\s+stars?|stars? count of (\d{1,3}(?:,\d{3})*|\d+))', info)
    if star_match:
        s = star_match.group(1) or star_match.group(2)
        stars = int(s.replace(',', ''))
        
    # Extract Project Name
    name_match = re.search(r'(?:project|named|name)\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)', info)
    
    if name_match:
        proj_name = name_match.group(1)
        if proj_name.endswith('.'): proj_name = proj_name[:-1]
        if proj_name.endswith(','): proj_name = proj_name[:-1]
        
        proj_list.append({'ProjectName': proj_name, 'Stars': stars})

df_proj = pd.DataFrame(proj_list)
# Deduplicate Project Info (keep max stars if duplicates, though unlikely)
df_proj = df_proj.sort_values('Stars', ascending=False).drop_duplicates(subset=['ProjectName'], keep='first')

# Process Package Info (Latest Version)
df_pkg = pd.DataFrame(package_info_data)
df_pkg['UpstreamPublishedAt'] = pd.to_numeric(df_pkg['UpstreamPublishedAt'], errors='coerce')
df_pkg = df_pkg.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
df_pkg_latest = df_pkg.drop_duplicates(subset=['Name'], keep='first')

# Process Mapping
df_map = pd.DataFrame(mapping_data)
# Deduplicate Mapping
df_map = df_map.drop_duplicates(subset=['Name', 'Version', 'ProjectName'])

# Merge
df_merged = pd.merge(df_pkg_latest, df_map, on=['Name', 'Version'], how='inner')
df_final = pd.merge(df_merged, df_proj, on='ProjectName', how='inner')

# Sort by Stars desc
df_final = df_final.sort_values(by=['Stars', 'Name'], ascending=[False, True])

# Select top 5
top_5 = df_final.head(5)[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-15043937850003619489': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-8286026177156777015': [{'COUNT(*)': '661372'}], 'var_function-call-884254517671409957': [{'count_star()': '597602'}], 'var_function-call-1646620457127674755': [{'count_star()': '770'}], 'var_function-call-5253085552876619836': 'file_storage/function-call-5253085552876619836.json', 'var_function-call-13209268095735794685': 'file_storage/function-call-13209268095735794685.json', 'var_function-call-13209268095735792616': 'file_storage/function-call-13209268095735792616.json', 'var_function-call-411015322578897938': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'Stars': 57236, 'ProjectName': 'strapi/strapi'}]}

exec(code, env_args)
