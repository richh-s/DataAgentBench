code = """import json, re
from pathlib import Path
p_latest = Path(var_call_FMPoXaG74AMdN2Nacorg3zQw)
latest = json.loads(p_latest.read_text())
ps = Path(var_call_vsK5PBlLGACOJq5jqVcPgnc6)
pp = json.loads(ps.read_text())
pi_path = Path(var_call_c8DdMGBHrUhDV0Yu7ZcbWmRF)
proj_info = json.loads(pi_path.read_text())

# Build mapping from (Name, Version) -> list of ProjectName
pv_map = {}
for r in pp:
    if r.get('System') != 'NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    pv_map.setdefault(key, []).append(r.get('ProjectName'))

# Helper to extract stars from Project_Information text
patterns = [
    re.compile(r'([0-9,]+)\s+stars'),
    re.compile(r'stars count of\s*([0-9,]+)'),
    re.compile(r'has garnered a total of\s*([0-9,]+)\s*stars'),
    re.compile(r'has an open issues count of\s*[0-9,]+,?\s*a stars count of\s*([0-9,]+)'),
    re.compile(r'has an open issues count of\s*[0-9,]+,\s*([0-9,]+)\s*stars'),
]

def extract_stars(text):
    if not text:
        return None
    for pat in patterns:
        m = pat.search(text)
        if m:
            num = m.group(1)
            try:
                return int(num.replace(',', ''))
            except:
                continue
    return None

proj_entries = []
for r in proj_info:
    info = r.get('Project_Information') or ''
    stars = extract_stars(info)
    proj_entries.append({'info': info, 'stars': stars})

results = []
for pkg in latest:
    name = pkg.get('Name')
    ver = pkg.get('Version')
    key = (name, ver)
    project_names = pv_map.get(key, [])
    best = None
    for pn in project_names:
        if not pn:
            continue
        for e in proj_entries:
            if pn in (e.get('info') or ''):
                s = e.get('stars')
                if s is None:
                    continue
                if (best is None) or (s > best['stars']):
                    best = {'Name': name, 'Version': ver, 'stars': s, 'ProjectName': pn}
    if best is not None:
        results.append(best)

results_sorted = sorted(results, key=lambda x: x['stars'], reverse=True)
# pick top 5 and prepare output with Stars field
top5 = [{'Name': r['Name'], 'Version': r['Version'], 'Stars': r['stars'], 'ProjectName': r['ProjectName']} for r in results_sorted[:5]]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_ZMbRMIcspGSPND5NJgLD3lUI': 'file_storage/call_ZMbRMIcspGSPND5NJgLD3lUI.json', 'var_call_FMPoXaG74AMdN2Nacorg3zQw': 'file_storage/call_FMPoXaG74AMdN2Nacorg3zQw.json', 'var_call_vsK5PBlLGACOJq5jqVcPgnc6': 'file_storage/call_vsK5PBlLGACOJq5jqVcPgnc6.json', 'var_call_c8DdMGBHrUhDV0Yu7ZcbWmRF': 'file_storage/call_c8DdMGBHrUhDV0Yu7ZcbWmRF.json'}

exec(code, env_args)
