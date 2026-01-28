code = """import json, re
path = var_call_os7AOcjj2rufSpBsKHwOLaNF
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

out = []
for rec in records:
    filename = rec.get('filename','')
    text = rec.get('text','')
    has_pa = bool(re.search(r'physical activity', text, re.I))
    count_pa = len(re.findall(r'physical activity', text, re.I))
    has_2016 = bool(re.search(r'\b2016\b', text))
    years = re.findall(r'\b(20\d{2})\b', text)
    years_unique = sorted(list(set(years)))
    out.append({'filename': filename, 'has_pa': has_pa, 'count_pa': count_pa, 'has_2016': has_2016, 'years_found': years_unique[:5]})

# Limit output size
out_sample = out[:200]
print('__RESULT__:')
print(json.dumps(out_sample))"""

env_args = {'var_call_dZzFsi4SOtro7Uw908RvLc2W': ['paper_docs'], 'var_call_LXL8ZA4trbYjT9RIvZMnHL63': 'file_storage/call_LXL8ZA4trbYjT9RIvZMnHL63.json', 'var_call_RN46vEKa6noQo1hbV1WtR7CC': [], 'var_call_os7AOcjj2rufSpBsKHwOLaNF': 'file_storage/call_os7AOcjj2rufSpBsKHwOLaNF.json', 'var_call_9GUtUiD2tMzvSetv4WScVci1': [], 'var_call_hpNKR78RMC3MOGV1id8Nj0Dl': []}

exec(code, env_args)
