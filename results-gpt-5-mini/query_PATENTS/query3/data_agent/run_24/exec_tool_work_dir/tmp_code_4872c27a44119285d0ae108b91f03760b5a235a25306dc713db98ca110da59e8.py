code = """import json
# load mappings and filtered pairs
pairs_path = var_call_N3bjYshQ0xsJvgxGYcZWEtqv
cpc_path = var_call_ji6UoQGci4UbQAEC5GrnGk21
with open(pairs_path, 'r', encoding='utf-8') as f:
    pairs = json.load(f)
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

sym2title = {r['symbol']: r['titleFull'] for r in cpc_defs}

# Filter pairs to unique assignees excluding ones that contain 'UNIV' or 'CALIFORNIA' alone
filtered = []
seen = set()
for p in pairs:
    assignee = p['assignee']
    code = p['cpc_code']
    key = (assignee, code)
    if key in seen:
        continue
    seen.add(key)
    # exclude if assignee contains UNIV CALIFORNIA or just UNIV or CALIFORNIA?
    au = assignee.upper()
    if 'UNIV' in au and 'CALIFORNIA' in au:
        continue
    if assignee.strip().upper() == 'UNIV' or assignee.strip().upper() == 'CALIFORNIA':
        # keep other 'UNIV XYZ' but exclude generic UNIV or CALIFORNIA
        if assignee.strip().upper() in ('UNIV','CALIFORNIA'):
            continue
    # find title
    title = sym2title.get(code)
    if title is None:
        # try match startswith
        for k,v in sym2title.items():
            if k.startswith(code):
                title = v
                break
    filtered.append({'assignee': assignee, 'code': code, 'titleFull': title})

# Now produce final mapping of assignee -> unique titles
from collections import OrderedDict
map_assoc = OrderedDict()
for f in filtered:
    a = f['assignee']
    t = f['titleFull'] if f['titleFull'] is not None else '(title not found)'
    map_assoc.setdefault(a, set()).add(t)

lines = []
for a, titles in map_assoc.items():
    for t in sorted(titles):
        lines.append({"assignee": a, "titleFull": t})

print('__RESULT__:')
print(json.dumps(lines))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}, 'var_call_axVHWtR2B6vfCQTIIHYLeBLc': 'file_storage/call_axVHWtR2B6vfCQTIIHYLeBLc.json', 'var_call_nf8yO7o1k1It4OAB20DbEaoy': 'file_storage/call_nf8yO7o1k1It4OAB20DbEaoy.json', 'var_call_ji6UoQGci4UbQAEC5GrnGk21': 'file_storage/call_ji6UoQGci4UbQAEC5GrnGk21.json', 'var_call_N3bjYshQ0xsJvgxGYcZWEtqv': 'file_storage/call_N3bjYshQ0xsJvgxGYcZWEtqv.json'}

exec(code, env_args)
