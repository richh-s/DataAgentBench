code = """import json, re, pandas as pd

# load package MIT release rows
pkg_src = var_call_Dvyqr7Py22ldWItyEtcscV6X
if isinstance(pkg_src, str):
    with open(pkg_src, 'r', encoding='utf-8') as f:
        pkg = json.load(f)
else:
    pkg = pkg_src

gh_src = var_call_OgcGl2eWbNc1lTb4DZux9iUU
if isinstance(gh_src, str):
    with open(gh_src, 'r', encoding='utf-8') as f:
        gh = json.load(f)
else:
    gh = gh_src

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
gh_df = pd.DataFrame(gh)[['System','Name','Version','ProjectName','Project_Information']].drop_duplicates()

# inner join on System/Name/Version
m = pkg_df.merge(gh_df, on=['System','Name','Version'], how='inner')

# extract forks from Project_Information
fork_re = re.compile(r'([0-9][0-9,]*)\s+forks')

def parse_forks(s):
    if not isinstance(s,str):
        return None
    mo = fork_re.search(s)
    if not mo:
        return None
    return int(mo.group(1).replace(',',''))

m['Forks'] = m['Project_Information'].map(parse_forks)

# get max forks per project
proj = (m.dropna(subset=['Forks'])
          .groupby('ProjectName', as_index=False)['Forks'].max())

proj = proj.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = proj.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uJ2RXv3SQTNMKdzi4UBti88N': [{'table_name': 'project_info'}, {'table_name': 'project_packageversion'}], 'var_call_VoQUrGdsFwgBo0aVA4F2qInZ': [{'name': 'packageinfo'}], 'var_call_Dvyqr7Py22ldWItyEtcscV6X': 'file_storage/call_Dvyqr7Py22ldWItyEtcscV6X.json', 'var_call_QpoPboiCbWE0ZXAEiq7Pxun0': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_call_fHaf2J7LTAtTnLZ7WP3OfvXo': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_call_OgcGl2eWbNc1lTb4DZux9iUU': 'file_storage/call_OgcGl2eWbNc1lTb4DZux9iUU.json'}

exec(code, env_args)
