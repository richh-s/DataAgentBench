code = """import json
path = var_call_TBlV8rB0asYjcC8kFLanPki8
with open(path, 'r', encoding='utf-8') as f:
    matched_with_info = json.load(f)
# We need to extract fork counts from Project_Information text.
import re
results = []
for r in matched_with_info:
    info = r.get('Project_Information','')
    # Look for pattern like 'X forks' or 'forks: X' or 'forked X times' etc.
    m = re.search(r'([0-9,]+)\s+forks', info, re.IGNORECASE)
    if not m:
        m = re.search(r'forked\s+([0-9,]+)\s+times', info, re.IGNORECASE)
    if not m:
        m = re.search(r'forks count of\s+([0-9,]+)', info, re.IGNORECASE)
    if m:
        forks = int(m.group(1).replace(',',''))
        results.append({'ProjectName': r['ProjectName'], 'Name': r['Name'], 'Version': r['Version'], 'Forks': forks})
# Deduplicate by ProjectName keeping max forks (though forks extracted from text likely consistent)
by_proj = {}
for r in results:
    p = r['ProjectName']
    if p not in by_proj or r['Forks'] > by_proj[p]['Forks']:
        by_proj[p] = r
# Sort by Forks desc and take top 5
top5 = sorted(by_proj.values(), key=lambda x: x['Forks'], reverse=True)[:5]
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_yLsAhTA5bdHMTrzlstkcUKhF': 'file_storage/call_yLsAhTA5bdHMTrzlstkcUKhF.json', 'var_call_ZAWEUlm0qlUdHYqISvwFHbVI': 'file_storage/call_ZAWEUlm0qlUdHYqISvwFHbVI.json', 'var_call_hW65jdsv3GmpdCSlUQsl6fxo': 'file_storage/call_hW65jdsv3GmpdCSlUQsl6fxo.json', 'var_call_ca4KRB3OW4oXuOi0zdpapENt': 'file_storage/call_ca4KRB3OW4oXuOi0zdpapENt.json', 'var_call_xsej0CgJXF5DxxGblASF1tv3': 'file_storage/call_xsej0CgJXF5DxxGblASF1tv3.json', 'var_call_D1crF1iMb1rYajTXGSwUo2mg': 'file_storage/call_D1crF1iMb1rYajTXGSwUo2mg.json', 'var_call_K88euMPheNbF1b3s6HbfkiHw': 'file_storage/call_K88euMPheNbF1b3s6HbfkiHw.json', 'var_call_mEuCUar5vYWMBnLzZvOOb5Xw': 'file_storage/call_mEuCUar5vYWMBnLzZvOOb5Xw.json', 'var_call_TBlV8rB0asYjcC8kFLanPki8': 'file_storage/call_TBlV8rB0asYjcC8kFLanPki8.json'}

exec(code, env_args)
