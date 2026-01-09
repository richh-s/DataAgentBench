code = """import json, re

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

funding = load_records(var_call_okz6iv72HTp7OX2p4MDtyMaz)
docs = load_records(var_call_s6w1q98gQI4S5Cy7We9V1SUX)

funding_names = set([r.get('Project_Name') for r in funding if r.get('Project_Name')])

extracted = set()

pattern_next_cap = re.compile(r'\nCapital Improvement Projects \((Construction|Not Started)\)')
pattern_next_dis = re.compile(r'\nDisaster Recovery Projects')

for d in docs:
    text = d.get('text') or ''
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    start = text.find('Capital Improvement Projects (Design)')
    sub = text[start:]
    m = pattern_next_cap.search(sub)
    if m:
        sub = sub[:m.start()]
    m = pattern_next_dis.search(sub)
    if m:
        sub = sub[:m.start()]

    for line in sub.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('(cid') or line.startswith('Page ') or line.startswith('Agenda Item'):
            continue
        if ':' in line:
            continue
        low = line.lower()
        if low.startswith('updates') or low.startswith('project schedule') or low.startswith('estimated schedule') or low.startswith('project description'):
            continue
        if low.startswith('complete design') or low.startswith('advertise') or low.startswith('begin construction') or low.startswith('final design'):
            continue
        if len(line) > 120:
            continue
        if line in funding_names:
            extracted.add(line)

out = {'count': len(extracted), 'projects': sorted(extracted)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zM1VWuHGFpMN9eDHqG2PYKJx': [{'cnt': '276'}], 'var_call_s6w1q98gQI4S5Cy7We9V1SUX': 'file_storage/call_s6w1q98gQI4S5Cy7We9V1SUX.json', 'var_call_okz6iv72HTp7OX2p4MDtyMaz': 'file_storage/call_okz6iv72HTp7OX2p4MDtyMaz.json'}

exec(code, env_args)
