code = """import json
p = var_call_uVzqr6w3MBdD5uKse2Gi8DUU
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
names = sorted(set(r['Name'] for r in data if r.get('System')=='NPM'))
def esc(s):
    return s.replace("'","''")
vals = ",".join("'"+esc(n)+"'" for n in names)
query = "SELECT DISTINCT ProjectName, System, Name FROM project_packageversion WHERE System='NPM' AND Name IN (" + vals + ")" + ";"
print('__RESULT__:')
print(json.dumps({'query': query, 'count_names': len(names)}))"""

env_args = {'var_call_uVzqr6w3MBdD5uKse2Gi8DUU': 'file_storage/call_uVzqr6w3MBdD5uKse2Gi8DUU.json', 'var_call_EI7Px1Y3s5x2XXF7Oer38Zdd': 'file_storage/call_EI7Px1Y3s5x2XXF7Oer38Zdd.json', 'var_call_rvBbuGxsDZLZroup0whjuRLy': 'file_storage/call_rvBbuGxsDZLZroup0whjuRLy.json'}

exec(code, env_args)
