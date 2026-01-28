code = """import json

pairs = var_call_ptQ99ID56B8ZnQTYxdSRH6Ho

# Load CPC definitions
cpc_path = var_call_PhBDJPa11TP1ROqC42Qfqs5k
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_rows = json.load(f)

cpc_map = {r['symbol'].strip(): (r.get('titleFull') or '').strip() for r in cpc_rows}

out=[]
for p in pairs:
    sym = p['cpc_subclass']
    title = cpc_map.get(sym)
    if not title:
        # sometimes subclass symbol includes trailing /00 in definitions; try add /00
        title = cpc_map.get(sym + '/00')
    if not title:
        title = None
    out.append({'citing_assignee': p['citing_assignee'], 'cpc_subclass': sym, 'cpc_subclass_titleFull': title})

out = [r for r in out if r['cpc_subclass_titleFull']]

# sort
out.sort(key=lambda x: (x['citing_assignee'], x['cpc_subclass']))

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_tlkzTucRomT39NGxEPtHjU1D': 'file_storage/call_tlkzTucRomT39NGxEPtHjU1D.json', 'var_call_PhBDJPa11TP1ROqC42Qfqs5k': 'file_storage/call_PhBDJPa11TP1ROqC42Qfqs5k.json', 'var_call_zf5QnerCfz7Lpp9ZBlIFOYWg': {'uc_pub_count': 112}, 'var_call_HB8Aj99xAYEazzcoYseMfwtU': 'file_storage/call_HB8Aj99xAYEazzcoYseMfwtU.json', 'var_call_ptQ99ID56B8ZnQTYxdSRH6Ho': [{'citing_assignee': 'CALIFORNIA INST OF TECHN', 'cpc_subclass': 'G01V1'}, {'citing_assignee': 'CRYSTAL IS INC', 'cpc_subclass': 'C30B25'}, {'citing_assignee': 'CRYSTAL IS INC', 'cpc_subclass': 'C30B11'}, {'citing_assignee': 'SCHOWALTER LEO J', 'cpc_subclass': 'H01L21'}]}

exec(code, env_args)
