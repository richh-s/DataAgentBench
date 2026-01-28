code = """import json
path = var_call_8ugGrPpYxpcvG5GHmuvDFpVb
with open(path, 'r', encoding='utf-8') as f:
    items = json.load(f)

lines = []
for it in items:
    a = it.get('assignee')
    t = it.get('titleFull')
    if not a:
        continue
    au = a.upper()
    if 'UNIV' in au and 'CALIFORNIA' in au:
        continue
    if au in ('UNIV', 'CALIFORNIA'):
        continue
    if t is None:
        t = '(title not found)'
    # replace newlines in title
    t_clean = ' '.join(str(t).split())
    lines.append(f"{a}: {t_clean}")

final_text = '\n'.join(lines)
print('__RESULT__:')
print(json.dumps(final_text))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}, 'var_call_axVHWtR2B6vfCQTIIHYLeBLc': 'file_storage/call_axVHWtR2B6vfCQTIIHYLeBLc.json', 'var_call_nf8yO7o1k1It4OAB20DbEaoy': 'file_storage/call_nf8yO7o1k1It4OAB20DbEaoy.json', 'var_call_ji6UoQGci4UbQAEC5GrnGk21': 'file_storage/call_ji6UoQGci4UbQAEC5GrnGk21.json', 'var_call_N3bjYshQ0xsJvgxGYcZWEtqv': 'file_storage/call_N3bjYshQ0xsJvgxGYcZWEtqv.json', 'var_call_8ugGrPpYxpcvG5GHmuvDFpVb': 'file_storage/call_8ugGrPpYxpcvG5GHmuvDFpVb.json'}

exec(code, env_args)
