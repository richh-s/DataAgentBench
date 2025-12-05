code = """import json, re, pandas as pd

# Load merged latest package-project mapping
with open(var_call_QLQHk4udFHcfDdwM1jDicBmk, 'r') as f:
    latest_pkg_proj = json.load(f)

pkg_proj_df = pd.DataFrame(latest_pkg_proj)

# Extract owner/repo from ProjectName (already in that format) so we can match text in Project_Information
pkg_proj_df['RepoString'] = pkg_proj_df['ProjectName'].astype(str)

# Load some project_info rows to build mapping from repo to stars by parsing text
info_rows = query_db_result_qltOu0rPZyKABD75lXwfqzYa  # already a list of dicts
info_df = pd.DataFrame(info_rows)

# Extract repo and stars from Project_Information text like "The project owner/repo ... has ... stars"
repo_pattern = re.compile(r"project ([^ ]+/[^ ]+) .*? (?:has|have) .*?([0-9,]+) stars", re.IGNORECASE)

def parse_info(row):
    text = row['Project_Information'] or ''
    m = repo_pattern.search(text)
    if not m:
        return None, None
    repo = m.group(1)
    stars = int(m.group(2).replace(',', ''))
    return repo, stars

info_df['Repo'], info_df['Stars'] = zip(*info_df.apply(parse_info, axis=1))
info_df = info_df.dropna(subset=['Repo','Stars'])

# Join stars to packages via RepoString == Repo
merged = pkg_proj_df.merge(info_df[['Repo','Stars']], left_on='RepoString', right_on='Repo', how='inner')

# For each package Name, keep max stars across repos (if multiple) and corresponding version
agg = merged.sort_values('Stars', ascending=False).groupby('Name', as_index=False).first()

# Get top 5 by Stars
top5 = agg.sort_values('Stars', ascending=False).head(5)[['Name','Version','Stars']]

result = top5.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oUWXneDPOkZEzhheLkOxCyAT': 'file_storage/call_oUWXneDPOkZEzhheLkOxCyAT.json', 'var_call_OgMKps48EQoU0fgAxa6eM1H7': 'file_storage/call_OgMKps48EQoU0fgAxa6eM1H7.json', 'var_call_QLQHk4udFHcfDdwM1jDicBmk': 'file_storage/call_QLQHk4udFHcfDdwM1jDicBmk.json', 'var_call_mPLjJ2haNwlaYR1moWw4mzK8': ['project_info', 'project_packageversion'], 'var_call_w4wSDo07pJapsNH0SNmliIJK': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_qltOu0rPZyKABD75lXwfqzYa': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}]}

exec(code, env_args)
