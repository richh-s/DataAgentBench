code = """import json, re
p = var_call_oBfQdzwsWQmuQJfCmacGssDL
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
results = []
for r in data:
    info = r.get('Project_Information','')
    # find repo owner/name
    m = re.search(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", info)
    repo = m.group(1) if m else None
    # find forks count number - look for 'forks' followed by numbers
    mf = re.search(r"(forks|forked)\D*([0-9,]+)", info, re.IGNORECASE)
    # alternative: 'and X forks' or 'forks count of X'
    if not mf:
        mf = re.search(r"([0-9,]+)\s+forks", info, re.IGNORECASE)
    forks = None
    if mf:
        num = mf.group(2) if mf.lastindex>=2 else mf.group(1)
        if num:
            try:
                forks = int(num.replace(',',''))
            except:
                forks = None
    if repo and forks is not None:
        results.append({'repo': repo, 'forks': forks, 'text': info})
results.sort(key=lambda x: x['forks'], reverse=True)
top = results[:5]
print('__RESULT__:')
print(json.dumps(top))"""

env_args = {'var_call_uVzqr6w3MBdD5uKse2Gi8DUU': 'file_storage/call_uVzqr6w3MBdD5uKse2Gi8DUU.json', 'var_call_EI7Px1Y3s5x2XXF7Oer38Zdd': 'file_storage/call_EI7Px1Y3s5x2XXF7Oer38Zdd.json', 'var_call_rvBbuGxsDZLZroup0whjuRLy': 'file_storage/call_rvBbuGxsDZLZroup0whjuRLy.json', 'var_call_Du00hMXw4cvWc8LQAFRZvCBl': 'file_storage/call_Du00hMXw4cvWc8LQAFRZvCBl.json', 'var_call_SgvZ4x0UxXRdcOCeAqDwfY2A': ['project_info', 'project_packageversion'], 'var_call_oBfQdzwsWQmuQJfCmacGssDL': 'file_storage/call_oBfQdzwsWQmuQJfCmacGssDL.json', 'var_call_XBD844VcEL7kCWPGnXxVmSYq': 'file_storage/call_XBD844VcEL7kCWPGnXxVmSYq.json', 'var_call_imdI6bcSWV6ckyYabMw18arf': 'file_storage/call_imdI6bcSWV6ckyYabMw18arf.json', 'var_call_JdXMRSThglkFvjgTgwYbyLiX': 'file_storage/call_JdXMRSThglkFvjgTgwYbyLiX.json', 'var_call_eClUP71EQMfoVnnIUGa0XJV3': 'file_storage/call_eClUP71EQMfoVnnIUGa0XJV3.json'}

exec(code, env_args)
