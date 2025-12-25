code = """import json, re, pandas as pd
from pathlib import Path

# Load latest versions
latest_path = Path(var_call_pgR8DklvvqL0NfufEWRJX6uP)
latest = pd.DataFrame(json.loads(latest_path.read_text()))

# Load project_packageversion
pp_path = Path(var_call_xO7rdrpgi2ALI0duis2lKySi)
pp = pd.DataFrame(json.loads(pp_path.read_text()))

# Join latest NPM versions with GitHub mappings
merged = latest.merge(pp, on=['System','Name','Version'], how='inner')

# Load project_info
pi = pd.DataFrame(var_call_B0PukT5VhaEeHTiMuntOx6nu)

# There is no explicit key, so we'll try to derive ProjectName (owner/repo) from Project_Information text
# Regex to capture 'owner/repo' immediately after 'project '
pattern = re.compile(r"project ([^\s/]+/[^\s]+)")

pi['ProjectName'] = pi['Project_Information'].apply(lambda s: pattern.search(s).group(1) if pattern.search(s) else None)

# Merge to get Project_Information for mapped projects
merged2 = merged.merge(pi[['ProjectName','Project_Information']], on='ProjectName', how='left')

# Extract stars from Project_Information text
stars_pattern = re.compile(r"(\d[\d,]*) stars")

def extract_stars(text):
    if not isinstance(text, str):
        return None
    m = stars_pattern.search(text)
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

merged2['Stars'] = merged2['Project_Information'].apply(extract_stars)

# Aggregate by package (Name, Version) taking max stars across possible multiple repos
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

# Get top 5 by stars
top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4BEVO5hAgGcLgquVMr5Bdrhu': ['project_info', 'project_packageversion'], 'var_call_5OrxSyEs6MnaamORRvkWrCoU': 'file_storage/call_5OrxSyEs6MnaamORRvkWrCoU.json', 'var_call_pgR8DklvvqL0NfufEWRJX6uP': 'file_storage/call_pgR8DklvvqL0NfufEWRJX6uP.json', 'var_call_SVUs3o7REvEvAksC66S3ndCj': 'file_storage/call_SVUs3o7REvEvAksC66S3ndCj.json', 'var_call_B0PukT5VhaEeHTiMuntOx6nu': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_m8QrrkQRNBObjF5T4HnXxSbb': ['project_info', 'project_packageversion'], 'var_call_xO7rdrpgi2ALI0duis2lKySi': 'file_storage/call_xO7rdrpgi2ALI0duis2lKySi.json'}

exec(code, env_args)
