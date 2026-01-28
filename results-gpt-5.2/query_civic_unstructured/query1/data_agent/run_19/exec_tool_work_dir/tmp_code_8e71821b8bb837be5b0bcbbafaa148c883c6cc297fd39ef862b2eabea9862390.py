code = """import json

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

funding = load_records(var_call_okz6iv72HTp7OX2p4MDtyMaz)
docs = load_records(var_call_s6w1q98gQI4S5Cy7We9V1SUX)

funding_names = set([r.get('Project_Name') for r in funding if r.get('Project_Name')])

extracted = set()
for d in docs:
    text = d.get('text') or ''
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    lines = [ln.rstrip() for ln in text.splitlines()]
    in_design = False
    for ln in lines:
        s = ln.strip()
        if s == 'Capital Improvement Projects (Design)':
            in_design = True
            continue
        if in_design and (s == 'Capital Improvement Projects (Construction)' or s == 'Capital Improvement Projects (Not Started)' or s == 'Disaster Recovery Projects'):
            in_design = False
        if not in_design:
            continue
        s = s.strip()
        if not s:
            continue
        if s.startswith('(cid') or s.startswith('Page ') or s.startswith('Agenda Item'):
            continue
        if ':' in s:
            continue
        low = s.lower()
        if low.startswith(('updates','project schedule','estimated schedule','project description','complete design','advertise','begin construction','final design')):
            continue
        if len(s) > 120:
            continue
        if s in funding_names:
            extracted.add(s)

print('__RESULT__:')
print(json.dumps({'count': len(extracted)}))"""

env_args = {'var_call_zM1VWuHGFpMN9eDHqG2PYKJx': [{'cnt': '276'}], 'var_call_s6w1q98gQI4S5Cy7We9V1SUX': 'file_storage/call_s6w1q98gQI4S5Cy7We9V1SUX.json', 'var_call_okz6iv72HTp7OX2p4MDtyMaz': 'file_storage/call_okz6iv72HTp7OX2p4MDtyMaz.json'}

exec(code, env_args)
