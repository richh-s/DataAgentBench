code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-8170898954798864343'], 'r') as f:
    packages_data = json.load(f)
df_packages = pd.DataFrame(packages_data)

with open(locals()['var_function-call-9880616322736191733'], 'r') as f:
    mapping_data = json.load(f)
df_mapping = pd.DataFrame(mapping_data)

with open(locals()['var_function-call-8466107741308955836'], 'r') as f:
    info_data = json.load(f)
df_info = pd.DataFrame(info_data)

# Process Packages: Filter NPM (already done in query), Get Latest Version
# Ensure UpstreamPublishedAt is numeric
df_packages['UpstreamPublishedAt'] = pd.to_numeric(df_packages['UpstreamPublishedAt'], errors='coerce')
# Sort by Name and Date desc, then drop duplicates keeping first (latest)
df_latest = df_packages.sort_values(['Name', 'UpstreamPublishedAt'], ascending=[True, False]).drop_duplicates('Name', keep='first')

# Process Project Info: Extract Name and Stars
def extract_info(text):
    # Extract Project Name: looks like 'owner/repo'
    # Pattern: "project <name>", "project named <name>", "under the name <name>"
    # We look for a pattern that matches owner/repo (alphanumeric, -, _, /)
    # The name usually follows "project" or "name"
    name_match = re.search(r'(?:project|name)\s+(?:is\s+)?(?:named\s+)?(?:hosted\s+on\s+GitHub\s+under\s+the\s+name\s+)?([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+)', text, re.IGNORECASE)
    
    # Extract Stars
    # Patterns: "X stars", "stars count of X", "total of X stars"
    # We want the number associated with "stars"
    # Handling commas in numbers
    # Pattern 1: "... 38,715 stars ..."
    stars_match1 = re.search(r'([\d,]+)\s+stars', text, re.IGNORECASE)
    # Pattern 2: "... stars count of 3,761 ..."
    stars_match2 = re.search(r'stars\s+count\s+of\s+([\d,]+)', text, re.IGNORECASE)
    
    name = name_match.group(1) if name_match else None
    
    stars = 0
    if stars_match2:
        s = stars_match2.group(1).replace(',', '')
        stars = int(s)
    elif stars_match1:
        s = stars_match1.group(1).replace(',', '')
        stars = int(s)
        
    return name, stars

extracted = df_info['Project_Information'].apply(extract_info)
df_info_extracted = pd.DataFrame(extracted.tolist(), columns=['ProjectName', 'Stars'])
# Drop entries where ProjectName could not be found
df_info_extracted = df_info_extracted.dropna(subset=['ProjectName'])
# Handle duplicates in Project Info if any (take max stars)
df_info_extracted = df_info_extracted.groupby('ProjectName')['Stars'].max().reset_index()

# Merge Data
# 1. Join Latest Packages with Mapping
# mapping has Name, Version, ProjectName
# df_latest has Name, Version
merged_pkg_proj = pd.merge(df_latest, df_mapping, on=['Name', 'Version'], how='inner')

# 2. Join with Stars
final_df = pd.merge(merged_pkg_proj, df_info_extracted, on='ProjectName', how='inner')

# Sort by Stars
top_5 = final_df.sort_values('Stars', ascending=False).head(5)

# Format Result
result = top_5[['Name', 'Version', 'Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2557747426360575779': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-8170898954798864343': 'file_storage/function-call-8170898954798864343.json', 'var_function-call-9880616322736191733': 'file_storage/function-call-9880616322736191733.json', 'var_function-call-8466107741308955836': 'file_storage/function-call-8466107741308955836.json'}

exec(code, env_args)
