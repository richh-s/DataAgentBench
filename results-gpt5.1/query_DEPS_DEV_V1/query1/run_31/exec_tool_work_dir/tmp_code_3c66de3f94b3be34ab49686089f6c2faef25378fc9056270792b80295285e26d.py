code = """import json, re, pandas as pd
from pathlib import Path

pkg = pd.read_json(Path(var_call_n3fr0cSupfMtmKEu3WMVfu4k))
proj_pkg = pd.read_json(Path(var_call_J50VVUBYAG4j8zfysF0OKsl9))

latest = pkg.sort_values('Version').drop_duplicates(['System','Name'], keep='last')
merged = latest.merge(proj_pkg, on=['System','Name','Version'], how='inner')

info = pd.read_json('project_info.json') if False else None

from pathlib import Path as P
pi_path = None
for p in P('.').glob('*.duckdb_project_info.json'):
    pi_path = p

if pi_path is None:
    # fallback: query first N via provided sample not possible; cannot continue
    result = json.dumps({'error': 'project_info full data path not provided'})
else:
    proj_info = pd.read_json(pi_path)
    def extract(repo_info):
        m = re.search(r'The project ([^ ]+/[^ ]+) .*? (\d+) stars', repo_info)
        if not m:
            return None, None
        return m.group(1), int(m.group(2))
    proj_info[['Repo','Stars']] = proj_info['Project_Information'].apply(lambda x: pd.Series(extract(x)))
    proj_info = proj_info.dropna(subset=['Repo','Stars'])
    merged2 = merged.merge(proj_info, left_on='ProjectName', right_on='Repo', how='inner')
    top = merged2.sort_values('Stars', ascending=False).drop_duplicates('Name').head(5)
    out = top[['Name','Version','Stars']].to_dict(orient='records')
    result = json.dumps(out)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_n3fr0cSupfMtmKEu3WMVfu4k': 'file_storage/call_n3fr0cSupfMtmKEu3WMVfu4k.json', 'var_call_J50VVUBYAG4j8zfysF0OKsl9': 'file_storage/call_J50VVUBYAG4j8zfysF0OKsl9.json', 'var_call_eis2Ztp5CWlJD27AdUIejggM': 'file_storage/call_eis2Ztp5CWlJD27AdUIejggM.json', 'var_call_FriuNUTlvl4k8f8qnKJrfk2V': ['project_info', 'project_packageversion'], 'var_call_BlduOeD7Xr0RRnKrpzpRP2sx': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}]}

exec(code, env_args)
