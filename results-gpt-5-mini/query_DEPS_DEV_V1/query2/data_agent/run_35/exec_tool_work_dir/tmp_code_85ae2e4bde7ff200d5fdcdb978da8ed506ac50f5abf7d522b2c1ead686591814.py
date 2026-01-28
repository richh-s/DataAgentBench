code = """import json
# load matched projects
matched_path = var_call_K88euMPheNbF1b3s6HbfkiHw
with open(matched_path, 'r', encoding='utf-8') as f:
    matched = json.load(f)
# load project_info records
projinfo_path = var_call_mEuCUar5vYWMBnLzZvOOb5Xw
with open(projinfo_path, 'r', encoding='utf-8') as f:
    projinfo = json.load(f)
# For faster search, build index by lowercased project_info string to record
# But project_info entries are textual sentences that include 'owner/repo' name. We'll search for each ProjectName in Project_Information.
results = []
for m in matched:
    pname = m['ProjectName']
    found = None
    for p in projinfo:
        info = p.get('Project_Information') or ''
        if pname.lower() in info.lower():
            found = p.get('Project_Information')
            break
    if found:
        results.append({'Name': m['Name'], 'Version': m['Version'], 'ProjectName': pname, 'Project_Information': found})
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json', 'var_call_ca4KRB3OW4oXuOi0zdpapENt': 'file_storage/call_ca4KRB3OW4oXuOi0zdpapENt.json', 'var_call_xsej0CgJXF5DxxGblASF1tv3': 'file_storage/call_xsej0CgJXF5DxxGblASF1tv3.json', 'var_call_D1crF1iMb1rYajTXGSwUo2mg': 'file_storage/call_D1crF1iMb1rYajTXGSwUo2mg.json', 'var_call_K88euMPheNbF1b3s6HbfkiHw': 'file_storage/call_K88euMPheNbF1b3s6HbfkiHw.json', 'var_call_mEuCUar5vYWMBnLzZvOOb5Xw': 'file_storage/call_mEuCUar5vYWMBnLzZvOOb5Xw.json'}

exec(code, env_args)
