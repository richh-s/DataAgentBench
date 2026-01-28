code = """import json, pandas as pd, re
from pathlib import Path

# load large packageinfo query result
p = Path(var_call_Y4UkXe89I0JarTTqNyqWThAq)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
# latest per package by UpstreamPublishedAt
# ensure numeric
df['UpstreamPublishedAt'] = pd.to_numeric(df['UpstreamPublishedAt'], errors='coerce')
# pick max timestamp per Name
idx = df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = df.loc[idx, ['Name','Version']].reset_index(drop=True)
# output list for join querying
latest_list = latest.to_dict('records')
print('__RESULT__:')
print(json.dumps({'latest': latest_list, 'n_latest': len(latest_list)}))"""

env_args = {'var_call_pxkLAs1YdGI39pZudg3opby1': [{'column_name': 'Project_Information'}, {'column_name': 'Licenses'}, {'column_name': 'Description'}, {'column_name': 'Homepage'}, {'column_name': 'OSSFuzz'}], 'var_call_tmIh16lE0gOjozKFl16rLxZk': [{'column_name': 'System'}, {'column_name': 'Name'}, {'column_name': 'Version'}, {'column_name': 'ProjectType'}, {'column_name': 'ProjectName'}, {'column_name': 'RelationProvenance'}, {'column_name': 'RelationType'}], 'var_call_wHfzC7WWYHd2TueaeVPAx7Bo': [{'cid': '0', 'name': 'System', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Name', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Version', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Licenses', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Links', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Advisories', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'VersionInfo', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Hashes', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'DependenciesProcessed', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'DependencyError', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'UpstreamPublishedAt', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'Registries', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'SLSAProvenance', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'UpstreamIdentifiers', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'Purl', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_call_Y4UkXe89I0JarTTqNyqWThAq': 'file_storage/call_Y4UkXe89I0JarTTqNyqWThAq.json'}

exec(code, env_args)
