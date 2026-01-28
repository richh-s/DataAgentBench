code = """import json
path = var_call_8ugGrPpYxpcvG5GHmuvDFpVb
with open(path, 'r', encoding='utf-8') as f:
    lines = json.load(f)
# Build a concise plain-text answer: for each assignee list unique titles
from collections import OrderedDict
map_assoc = OrderedDict()
for item in lines:
    a = item['assignee']
    t = item['titleFull']
    map_assoc.setdefault(a, set()).add(t)

out_lines = []
for a, titles in map_assoc.items():
    if a.strip()=='' or a is None:
        continue
    # exclude UNIV CALIFORNIA exact
    au = a.upper()
    if 'UNIV' in au and 'CALIFORNIA' in au:
        continue
    if au in ('UNIV','CALIFORNIA'):
        continue
    for t in sorted(titles):
        out_lines.append(f"{a}: {t}")

final = '\n'.join(out_lines)

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}, 'var_call_axVHWtR2B6vfCQTIIHYLeBLc': 'file_storage/call_axVHWtR2B6vfCQTIIHYLeBLc.json', 'var_call_nf8yO7o1k1It4OAB20DbEaoy': 'file_storage/call_nf8yO7o1k1It4OAB20DbEaoy.json', 'var_call_ji6UoQGci4UbQAEC5GrnGk21': 'file_storage/call_ji6UoQGci4UbQAEC5GrnGk21.json', 'var_call_N3bjYshQ0xsJvgxGYcZWEtqv': 'file_storage/call_N3bjYshQ0xsJvgxGYcZWEtqv.json', 'var_call_8ugGrPpYxpcvG5GHmuvDFpVb': 'file_storage/call_8ugGrPpYxpcvG5GHmuvDFpVb.json'}

exec(code, env_args)
