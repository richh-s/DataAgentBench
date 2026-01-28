code = """import json, re
p = var_call_oBfQdzwsWQmuQJfCmacGssDL
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
results = []
for r in data:
    info = r.get('Project_Information','')
    # try to find owner/repo pattern like 'the project OWNER/REPO' or 'project OWNER/REPO on GitHub'
    m = re.search(r"project\s+([\w\-\.]+/[\w\-\.]+)", info, re.IGNORECASE)
    if not m:
        m = re.search(r"GitHub project\s+([\w\-\.]+/[\w\-\.]+)", info, re.IGNORECASE)
    if not m:
        m = re.search(r"hosted on GitHub and.*?the project\s+([\w\-\.]+/[\w\-\.]+)", info, re.IGNORECASE)
    repo = m.group(1) if m else None
    # find forks count number
    mf = re.search(r"forks?\s*(?:count\s*of\s*)?(?:[:]?\s*)([0-9,]+)", info, re.IGNORECASE)
    if not mf:
        mf = re.search(r"forked\s*([0-9,]+)\s*times", info, re.IGNORECASE)
    forks = int(mf.group(1).replace(',','')) if mf else None
    if repo and forks is not None:
        results.append({'repo': repo, 'forks': forks, 'text': info})
# sort by forks desc
results.sort(key=lambda x: x['forks'], reverse=True)
# take top 50
top = results[:50]
repos = [r['repo'] for r in top]
print('__RESULT__:')
print(json.dumps({'top_repos': repos, 'top_count': len(repos)}))"""

env_args = {'var_call_uVzqr6w3MBdD5uKse2Gi8DUU': 'file_storage/call_uVzqr6w3MBdD5uKse2Gi8DUU.json', 'var_call_EI7Px1Y3s5x2XXF7Oer38Zdd': 'file_storage/call_EI7Px1Y3s5x2XXF7Oer38Zdd.json', 'var_call_rvBbuGxsDZLZroup0whjuRLy': 'file_storage/call_rvBbuGxsDZLZroup0whjuRLy.json', 'var_call_Du00hMXw4cvWc8LQAFRZvCBl': 'file_storage/call_Du00hMXw4cvWc8LQAFRZvCBl.json', 'var_call_SgvZ4x0UxXRdcOCeAqDwfY2A': ['project_info', 'project_packageversion'], 'var_call_oBfQdzwsWQmuQJfCmacGssDL': 'file_storage/call_oBfQdzwsWQmuQJfCmacGssDL.json', 'var_call_XBD844VcEL7kCWPGnXxVmSYq': 'file_storage/call_XBD844VcEL7kCWPGnXxVmSYq.json', 'var_call_imdI6bcSWV6ckyYabMw18arf': 'file_storage/call_imdI6bcSWV6ckyYabMw18arf.json', 'var_call_JdXMRSThglkFvjgTgwYbyLiX': 'file_storage/call_JdXMRSThglkFvjgTgwYbyLiX.json', 'var_call_eClUP71EQMfoVnnIUGa0XJV3': 'file_storage/call_eClUP71EQMfoVnnIUGa0XJV3.json'}

exec(code, env_args)
