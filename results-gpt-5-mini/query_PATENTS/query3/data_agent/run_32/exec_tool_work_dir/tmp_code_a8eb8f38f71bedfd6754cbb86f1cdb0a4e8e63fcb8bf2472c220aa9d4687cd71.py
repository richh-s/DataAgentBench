code = """import json, re
# Load the result file from the previous query stored in var_call_Ep2domLX3d6t0MazCpUv3OHC
path = var_call_Ep2domLX3d6t0MazCpUv3OHC
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pubnums = set()
pat_entries = []
for rec in data:
    pat_entries.append(rec)
    pi = rec.get('Patents_info','')
    # find patterns like XX-1234567-A1 or US-11421276-B2 or TW-201925402-A
    matches = re.findall(r'[A-Z]{2}-\d{4,}-[A-Z0-9]+', pi)
    for m in matches:
        pubnums.add(m)
    # also try finding 'publication number' pattern with US numbers without hyphen
    matches2 = re.findall(r'US-?\d{4,}-?\d{4,}[A-Z0-9-]*', pi)
    for m in matches2:
        # normalize to with hyphen after country
        if not m.startswith('US-'):
            continue
        pubnums.add(m)

pubnums = sorted(pubnums)
# As fallback, also try to parse title_localized for any pubnum? skip

result = {'pubnums': pubnums}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ep2domLX3d6t0MazCpUv3OHC': 'file_storage/call_Ep2domLX3d6t0MazCpUv3OHC.json'}

exec(code, env_args)
