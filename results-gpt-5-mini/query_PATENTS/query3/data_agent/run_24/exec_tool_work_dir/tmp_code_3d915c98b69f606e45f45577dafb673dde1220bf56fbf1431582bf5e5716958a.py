code = """import json
# load previous results (file paths)
path_pairs = var_call_nf8yO7o1k1It4OAB20DbEaoy
path_cpc = var_call_ji6UoQGci4UbQAEC5GrnGk21

with open(path_pairs, 'r', encoding='utf-8') as f:
    pairs_data = json.load(f)
with open(path_cpc, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# build mapping from symbol to titleFull
sym2title = {}
for r in cpc_defs:
    sym = r.get('symbol')
    title = r.get('titleFull')
    if sym:
        sym2title[sym.strip()] = title

# For some codes, the format might differ in case or spacing; ensure lookup exact
entries = []
for p in pairs_data.get('pairs', []):
    assignee = p.get('assignee')
    code = p.get('code')
    title = sym2title.get(code)
    if title is None:
        # try various fallbacks: full code without trailing zeros/spaces
        title = sym2title.get(code.upper())
    if title is None:
        # try to find symbol that startswith code
        for k,v in sym2title.items():
            if k.startswith(code):
                title = v
                break
    entries.append({'assignee': assignee, 'code': code, 'titleFull': title})

# Group by assignee
from collections import OrderedDict
grouped = OrderedDict()
for e in entries:
    a = e['assignee']
    grouped.setdefault(a, []).append({'code': e['code'], 'titleFull': e['titleFull']})

# Build final text
lines = []
for a, lst in grouped.items():
    lines.append(a)
    for it in lst:
        title = it['titleFull'] if it['titleFull'] is not None else '(title not found)'
        lines.append(f" - {it['code']}: {title}")
    lines.append('')
final_text = '\n'.join(lines).strip()

out = {'final_text': final_text, 'entries': entries}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}, 'var_call_axVHWtR2B6vfCQTIIHYLeBLc': 'file_storage/call_axVHWtR2B6vfCQTIIHYLeBLc.json', 'var_call_nf8yO7o1k1It4OAB20DbEaoy': 'file_storage/call_nf8yO7o1k1It4OAB20DbEaoy.json', 'var_call_ji6UoQGci4UbQAEC5GrnGk21': 'file_storage/call_ji6UoQGci4UbQAEC5GrnGk21.json'}

exec(code, env_args)
