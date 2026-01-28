code = """import json
path = var_call_AUL5MSdQI6iDOfhO8Khnfil0
with open(path, 'r') as f:
    repos = json.load(f)
# Build SQL IN clause
def sql_quote(s):
    return "'" + s.replace("'","''") + "'"
in_clause = '(' + ','.join(sql_quote(r) for r in repos) + ')'
print('__RESULT__:')
print(json.dumps(in_clause))"""

env_args = {'var_call_YBeocKWRxOxzvPgZ8i7fI1aQ': 'file_storage/call_YBeocKWRxOxzvPgZ8i7fI1aQ.json', 'var_call_TvoXgW0CKJm579O4NIyP6Kis': 'file_storage/call_TvoXgW0CKJm579O4NIyP6Kis.json', 'var_call_AUL5MSdQI6iDOfhO8Khnfil0': 'file_storage/call_AUL5MSdQI6iDOfhO8Khnfil0.json'}

exec(code, env_args)
