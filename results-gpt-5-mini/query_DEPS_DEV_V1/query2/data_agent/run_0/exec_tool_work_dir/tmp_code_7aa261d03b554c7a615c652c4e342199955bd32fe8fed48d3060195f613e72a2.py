code = """import json
p = var_call_uVzqr6w3MBdD5uKse2Gi8DUU
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
names = sorted(set(r['Name'] for r in data if r.get('System')=='NPM'))
def esc(s):
    return s.replace("'","''")
vals = ",".join("'"+esc(n)+"'" for n in names)
query = "SELECT DISTINCT ProjectName, System, Name, Version FROM project_packageversion WHERE System='NPM' AND Name IN (" + vals + ")" + ";"
print('__RESULT__:')
print(json.dumps({'query': query, 'count_names': len(names)}))"""

env_args = {'var_call_uVzqr6w3MBdD5uKse2Gi8DUU': 'file_storage/call_uVzqr6w3MBdD5uKse2Gi8DUU.json', 'var_call_EI7Px1Y3s5x2XXF7Oer38Zdd': 'file_storage/call_EI7Px1Y3s5x2XXF7Oer38Zdd.json', 'var_call_rvBbuGxsDZLZroup0whjuRLy': 'file_storage/call_rvBbuGxsDZLZroup0whjuRLy.json', 'var_call_Du00hMXw4cvWc8LQAFRZvCBl': 'file_storage/call_Du00hMXw4cvWc8LQAFRZvCBl.json', 'var_call_SgvZ4x0UxXRdcOCeAqDwfY2A': ['project_info', 'project_packageversion'], 'var_call_oBfQdzwsWQmuQJfCmacGssDL': 'file_storage/call_oBfQdzwsWQmuQJfCmacGssDL.json', 'var_call_XBD844VcEL7kCWPGnXxVmSYq': 'file_storage/call_XBD844VcEL7kCWPGnXxVmSYq.json', 'var_call_imdI6bcSWV6ckyYabMw18arf': 'file_storage/call_imdI6bcSWV6ckyYabMw18arf.json', 'var_call_JdXMRSThglkFvjgTgwYbyLiX': 'file_storage/call_JdXMRSThglkFvjgTgwYbyLiX.json'}

exec(code, env_args)
