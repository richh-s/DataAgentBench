code = """import json, re, pandas as pd
from pathlib import Path

pkg_path = Path(var_call_gxTgALSTKBiZ55pCkLghy7It)
proj_pkg_path = Path(var_call_dg33ifVrAPTZ7q985JZueKb6)

pkg_df = pd.DataFrame(json.loads(pkg_path.read_text()))[['System','Name','Version']].drop_duplicates()
proj_pkg_df = pd.DataFrame(json.loads(proj_pkg_path.read_text()))[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')
projects = merged['ProjectName'].dropna().unique().tolist()

proj_info_path = Path('project_info_full.json')
proj_info_df = pd.DataFrame(json.loads(proj_info_path.read_text()))

proj_info_df = proj_info_df[proj_info_df['Project_Information'].str.contains('forks')]

pattern = re.compile(r"The project (.+?) on GitHub.*?([0-9,]+) stars.*?([0-9,]+) forks", re.IGNORECASE)

rows = []
for info in proj_info_df['Project_Information']:
    m = pattern.search(info)
    if m:
        name = m.group(1).strip()
        stars = int(m.group(2).replace(',',''))
        forks = int(m.group(3).replace(',',''))
        rows.append({'ProjectName': name, 'Stars': stars, 'Forks': forks})

info_parsed = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

final = info_parsed[info_parsed['ProjectName'].isin(projects)].sort_values('Forks', ascending=False).head(5)

result = final[['ProjectName','Forks']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gxTgALSTKBiZ55pCkLghy7It': 'file_storage/call_gxTgALSTKBiZ55pCkLghy7It.json', 'var_call_u3qdge9zUQ9XFwgqchhnKAjQ': ['project_info', 'project_packageversion'], 'var_call_PxhJ3XdhqDrTLmDe1uEtHtoT': 'file_storage/call_PxhJ3XdhqDrTLmDe1uEtHtoT.json', 'var_call_usmK5gNxZ5zat4MLBzwMOgWD': [{'Count': '1'}], 'var_call_dg33ifVrAPTZ7q985JZueKb6': 'file_storage/call_dg33ifVrAPTZ7q985JZueKb6.json', 'var_call_5gyP3dZ0F3eZymTzzRQ9nOG4': {'project_count': 5289, 'sample_projects': ['discue/ui-components', 'dvcol/web-extension-utils', 'dlesage25/eclipse-cli', 'ebot7/edem', 'encryption4all/irmaseal', 'ebury/chameleon', 'egroupai/egroup-material', 'ditojs/dito', 'dsrvlabs/kms', 'npenin/rfx', 'dnv-opensource/playwright-live-recorder', 'draftbit/react-native-jigsaw', 'dotdevv/packages', 'easyops-cn/docusaurus-search-local', 'dwelle/excalidraw', 'dxos/dxos', 'taixw2/dx', 'e-conomic/gaudi', 'n43/easyapp', 'luzzif/ethereum-contacts-registry']}, 'var_call_igoqUhS1wv4I1q1DTX4rTtRm': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}]}

exec(code, env_args)
