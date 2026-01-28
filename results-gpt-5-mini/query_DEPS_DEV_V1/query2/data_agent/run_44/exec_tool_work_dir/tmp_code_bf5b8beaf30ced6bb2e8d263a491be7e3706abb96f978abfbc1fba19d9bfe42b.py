code = """import pandas as pd
import json
# Load results from previous query_db calls
# var_call_eZTWND63B9Ut5HlwIDSFC7V7 and var_call_vYGlZ0TX6a8k7YP3TkaDHMqV are available in storage
df_pkg = pd.read_json(var_call_eZTWND63B9Ut5HlwIDSFC7V7)
df_projver = pd.read_json(var_call_vYGlZ0TX6a8k7YP3TkaDHMqV)
# Merge on System, Name, Version
merged = pd.merge(df_pkg[['System','Name','Version']], df_projver[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
project_names = sorted(merged['ProjectName'].dropna().unique().tolist())
# Build WHERE clause: Project_Information LIKE '%projectname%'
# Limit to a reasonable number if too many
proj_names_limited = project_names[:500]
where_clauses = [f"Project_Information LIKE '%{pn.replace("'","" )}%" + "%'" for pn in proj_names_limited]
where_clause = ' OR '.join(where_clauses) if where_clauses else '1=0'
out = {'count_project_names': len(project_names), 'project_names_sample': proj_names_limited, 'where_clause': where_clause}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_eZTWND63B9Ut5HlwIDSFC7V7': 'file_storage/call_eZTWND63B9Ut5HlwIDSFC7V7.json', 'var_call_vYGlZ0TX6a8k7YP3TkaDHMqV': 'file_storage/call_vYGlZ0TX6a8k7YP3TkaDHMqV.json'}

exec(code, env_args)
