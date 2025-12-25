code = """import json, pandas as pd, ast

# Load NPM packageinfo subset with UpstreamPublishedAt & VersionInfo
with open(var_call_n1DxkPcduzfXhl4Z5DpH6msF, 'r') as f:
    package_rows = json.load(f)

pkg_df = pd.DataFrame(package_rows)

# Filter to release versions only based on VersionInfo.IsRelease if present

def parse_is_release(v):
    try:
        obj = ast.literal_eval(v) if isinstance(v, str) else {}
        if isinstance(obj, dict) and 'IsRelease' in obj:
            return bool(obj['IsRelease'])
    except Exception:
        pass
    return True

pkg_df['is_release'] = pkg_df['VersionInfo'].apply(parse_is_release)
pkg_df = pkg_df[pkg_df['is_release']]

# Ensure numeric timestamp
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

# Pick latest version per (System, Name)
latest_pkg = pkg_df.sort_values('UpstreamPublishedAt').groupby(['System','Name'], as_index=False).tail(1)[['System','Name','Version']]

# Load project_packageversion
with open(var_call_u8tojOdQCGAVwrg1b3yzwSHb, 'r') as f:
    proj_pkg_rows = json.load(f)

pp_df = pd.DataFrame(proj_pkg_rows)
pp_df = pp_df[(pp_df['System']=='NPM') & (pp_df['ProjectType']=='GITHUB')]

# Join packages to projects on exact version
merged = latest_pkg.merge(pp_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Now get project_info for these ProjectNames from database via separate query later; here just keep unique ProjectNames
projects = merged['ProjectName'].unique().tolist()[:1000]

result = {
  'latest_pkg_sample': latest_pkg.head(5).to_dict(orient='records'),
  'merged_sample': merged.head(5).to_dict(orient='records'),
  'project_names_sample': projects[:10]
}

import json as _json

print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_WUzblKxX0PvPpqAosn3KpCm4': [], 'var_call_11MCSTwt3FMxRXwBMl0nGBgq': 'file_storage/call_11MCSTwt3FMxRXwBMl0nGBgq.json', 'var_call_YdQ1Pp2XtlWJFtFsBkwd6YZ0': ['project_info', 'project_packageversion'], 'var_call_pg0Kb5g8s39DLBItfDhCPvjI': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_call_u8tojOdQCGAVwrg1b3yzwSHb': 'file_storage/call_u8tojOdQCGAVwrg1b3yzwSHb.json', 'var_call_n1DxkPcduzfXhl4Z5DpH6msF': 'file_storage/call_n1DxkPcduzfXhl4Z5DpH6msF.json'}

exec(code, env_args)
