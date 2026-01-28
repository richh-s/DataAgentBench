code = """import json
path_pairs = var_call_nf8yO7o1k1It4OAB20DbEaoy
path_cpc = var_call_ji6UoQGci4UbQAEC5GrnGk21
with open(path_pairs, 'r', encoding='utf-8') as f:
    pairs_data = json.load(f)
with open(path_cpc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

sym2title = {}
for r in cpc_defs:
    sym = r.get('symbol')
    title = r.get('titleFull')
    if sym:
        sym2title[sym.strip()] = title

results = []
for p in pairs_data.get('pairs', []):
    assignee = p.get('assignee')
    code = p.get('code')
    title = sym2title.get(code)
    if title is None:
        title = sym2title.get(code.upper())
    if title is None:
        # try startswith
        for k,v in sym2title.items():
            if k.startswith(code):
                title = v
                break
    results.append({"assignee": assignee, "cpc_code": code, "titleFull": title})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}, 'var_call_axVHWtR2B6vfCQTIIHYLeBLc': 'file_storage/call_axVHWtR2B6vfCQTIIHYLeBLc.json', 'var_call_nf8yO7o1k1It4OAB20DbEaoy': 'file_storage/call_nf8yO7o1k1It4OAB20DbEaoy.json', 'var_call_ji6UoQGci4UbQAEC5GrnGk21': 'file_storage/call_ji6UoQGci4UbQAEC5GrnGk21.json'}

exec(code, env_args)
