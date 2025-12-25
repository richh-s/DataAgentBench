code = """import pandas as pd, json

pkg_file = var_call_GVXUyJ41Qi1VV7jCOsD5zc1t
proj_file = var_call_9gbjNSgGJSN2zC5QfYfREvZJ

pkg = pd.read_json(pkg_file)
proj = pd.read_json(proj_file)

latest = pkg.sort_values('Version').drop_duplicates(['System','Name'], keep='last')
latest = latest[latest['System']=='NPM'][['System','Name','Version']]

merged = latest.merge(proj[proj['System']=='NPM'], on=['System','Name','Version'])

project_names = merged['ProjectName'].unique().tolist()

result = json.dumps(project_names[:500])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_GVXUyJ41Qi1VV7jCOsD5zc1t': 'file_storage/call_GVXUyJ41Qi1VV7jCOsD5zc1t.json', 'var_call_C8Hva7mrNRjfDUHAhw12akIn': ['project_info', 'project_packageversion'], 'var_call_9gbjNSgGJSN2zC5QfYfREvZJ': 'file_storage/call_9gbjNSgGJSN2zC5QfYfREvZJ.json'}

exec(code, env_args)
