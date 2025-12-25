code = """import json
import pandas as pd

# Load package info
with open(locals()['var_function-call-5064586497231711022'], 'r') as f:
    packages_data = json.load(f)

df_packages = pd.DataFrame(packages_data)

# Ensure UpstreamPublishedAt is float
df_packages['UpstreamPublishedAt'] = df_packages['UpstreamPublishedAt'].astype(float)

# Get latest version for each package
# Sort by Name and UpstreamPublishedAt descending
df_packages = df_packages.sort_values(by=['Name', 'UpstreamPublishedAt'], ascending=[True, False])
# Drop duplicates keeping first (latest)
df_latest_packages = df_packages.drop_duplicates(subset=['Name'], keep='first')

# Load project mapping
with open(locals()['var_function-call-7159053233744676591'], 'r') as f:
    mapping_data = json.load(f)

df_mapping = pd.DataFrame(mapping_data)

# Join
# We need to match Name and Version
df_merged = pd.merge(df_latest_packages, df_mapping, on=['Name', 'Version'], how='inner')

unique_projects = df_merged['ProjectName'].unique()
print("__RESULT__:")
print(len(unique_projects))"""

env_args = {'var_function-call-16346607828030946301': ['project_info', 'project_packageversion'], 'var_function-call-4586612903755575240': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-5064586497231711022': 'file_storage/function-call-5064586497231711022.json', 'var_function-call-7159053233744676591': 'file_storage/function-call-7159053233744676591.json'}

exec(code, env_args)
