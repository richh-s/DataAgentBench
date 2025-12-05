code = """import re, json, pandas as pd

projects_file = var_call_tKdtB9c4HhlVLdzyBCGl4WcV
info_file = var_call_WV9b9oa7jzGMK6Iz8HGGinf4

project_names = json.loads(open(projects_file).read())
info = pd.read_json(info_file)

pattern = re.compile(r"The project ([-\w./]+) on GitHub.*? (\d+) stars")

rows = []
for s in info['Project_Information']:
    m = pattern.search(s)
    if m:
        repo, stars = m.group(1), int(m.group(2))
        if repo in project_names:
            rows.append({'ProjectName': repo, 'Stars': stars})

stars_df = pd.DataFrame(rows).drop_duplicates('ProjectName')

stars_df = stars_df.sort_values('Stars', ascending=False).head(5)

result = stars_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GVXUyJ41Qi1VV7jCOsD5zc1t': 'file_storage/call_GVXUyJ41Qi1VV7jCOsD5zc1t.json', 'var_call_C8Hva7mrNRjfDUHAhw12akIn': ['project_info', 'project_packageversion'], 'var_call_9gbjNSgGJSN2zC5QfYfREvZJ': 'file_storage/call_9gbjNSgGJSN2zC5QfYfREvZJ.json', 'var_call_tKdtB9c4HhlVLdzyBCGl4WcV': 'file_storage/call_tKdtB9c4HhlVLdzyBCGl4WcV.json', 'var_call_WV9b9oa7jzGMK6Iz8HGGinf4': 'file_storage/call_WV9b9oa7jzGMK6Iz8HGGinf4.json'}

exec(code, env_args)
