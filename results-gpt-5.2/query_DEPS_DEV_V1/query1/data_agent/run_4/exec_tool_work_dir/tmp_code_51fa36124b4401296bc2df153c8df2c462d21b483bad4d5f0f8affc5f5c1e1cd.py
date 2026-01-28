code = """import json, pandas as pd, re
from pathlib import Path

ppv = json.loads(Path(var_call_KQfjQrAIGtkZPNKzyufbMGz8).read_text())
df = pd.DataFrame(ppv).drop_duplicates(subset=['Name','Version','ProjectName'])
projects = sorted(df['ProjectName'].dropna().unique().tolist())
# chunk project names
chunks=[]
chunk_size=500
for i in range(0,len(projects),chunk_size):
    part=projects[i:i+chunk_size]
    values=",".join(["'%s'"%p.replace("'","''") for p in part])
    chunks.append(values)
print('__RESULT__:')
print(json.dumps({'project_chunks': chunks, 'n_projects': len(projects)}))"""

env_args = {'var_call_pxkLAs1YdGI39pZudg3opby1': [{'column_name': 'Project_Information'}, {'column_name': 'Licenses'}, {'column_name': 'Description'}, {'column_name': 'Homepage'}, {'column_name': 'OSSFuzz'}], 'var_call_tmIh16lE0gOjozKFl16rLxZk': [{'column_name': 'System'}, {'column_name': 'Name'}, {'column_name': 'Version'}, {'column_name': 'ProjectType'}, {'column_name': 'ProjectName'}, {'column_name': 'RelationProvenance'}, {'column_name': 'RelationType'}], 'var_call_wHfzC7WWYHd2TueaeVPAx7Bo': [{'cid': '0', 'name': 'System', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Name', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Version', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Licenses', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Links', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Advisories', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'VersionInfo', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Hashes', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'DependenciesProcessed', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'DependencyError', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'UpstreamPublishedAt', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'Registries', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'SLSAProvenance', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'UpstreamIdentifiers', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'Purl', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_call_Y4UkXe89I0JarTTqNyqWThAq': 'file_storage/call_Y4UkXe89I0JarTTqNyqWThAq.json', 'var_call_G5vTvfcZmYx9KtyVIoSIOggY': 'file_storage/call_G5vTvfcZmYx9KtyVIoSIOggY.json', 'var_call_Sh6iofSNonHZRscaMp8ExfOd': 'file_storage/call_Sh6iofSNonHZRscaMp8ExfOd.json', 'var_call_KQfjQrAIGtkZPNKzyufbMGz8': 'file_storage/call_KQfjQrAIGtkZPNKzyufbMGz8.json'}

exec(code, env_args)
