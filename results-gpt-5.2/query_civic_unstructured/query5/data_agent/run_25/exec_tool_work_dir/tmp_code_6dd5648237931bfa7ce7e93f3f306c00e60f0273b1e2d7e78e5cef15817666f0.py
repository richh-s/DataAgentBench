code = """import json, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

recs = load_records(var_call_z7Mf6VF2TPmhf1Kchq3B0YPc)

projects = []
for r in recs:
    lines = r.get('text','').splitlines()
    in_disaster = False
    current = None
    for raw in lines:
        line = raw.strip()
        if re.search(r"^Disaster Projects", line, re.I) or re.search(r"^Disaster Recovery Projects", line, re.I):
            in_disaster = True
            current = None
            continue
        if in_disaster and re.search(r"^Capital Improvement Projects", line, re.I):
            in_disaster = False
            current = None
            continue
        if not in_disaster:
            continue
        if not line:
            continue
        if re.match(r"^(Page \\d+|Agenda Item)", line):
            continue
        if line.startswith(('(cid:', '•', '-', '(cid', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Complete', 'Advertise', 'Begin', 'Final', 'Design', 'Construction', 'Notice', 'Staff')):
            if current is not None:
                if re.search(r"(Project Schedule|Estimated Schedule|Begin|Award|Start|Advertise)", line, re.I) or '2022' in line:
                    current['schedule_text'] += ' ' + line
            continue
        if re.match(r"^\(?(Design|Construction|Not Started|Completed)\)?$", line, re.I):
            continue
        current = {'Project_Name': line, 'schedule_text': ''}
        projects.append(current)

started_2022 = []
for p in projects:
    stxt = p.get('schedule_text','')
    if re.search(r"Begin\s+Construction\s*:\s*[^\n]*2022", stxt, re.I):
        started_2022.append(p['Project_Name'])
    elif re.search(r"Award Contract and Begin Construction\s*:\s*[^\n]*2022", stxt, re.I):
        started_2022.append(p['Project_Name'])
    elif re.search(r"Begin\s+Construction\s*:\s*Spring\s+2022", stxt, re.I):
        started_2022.append(p['Project_Name'])

started_2022 = sorted(set(started_2022))
print('__RESULT__:')
print(json.dumps({'started_2022_disaster_projects': started_2022, 'count': len(started_2022)}))"""

env_args = {'var_call_kG8ZQWCW2AVY2ZXpQKanylNW': ['Funding'], 'var_call_jVGLGQgarGHvy0J91PYPUfMo': ['civic_docs'], 'var_call_jDyoHOwxFQnWh3YXVXOOXXe1': 'file_storage/call_jDyoHOwxFQnWh3YXVXOOXXe1.json', 'var_call_wdpKCzaziu8R6N0HjcFJdX7l': 'file_storage/call_wdpKCzaziu8R6N0HjcFJdX7l.json', 'var_call_ebmDP9U7vETKwz1Nt2kBhfZv': {'started_2022_disaster_projects': [], 'count': 0}, 'var_call_z7Mf6VF2TPmhf1Kchq3B0YPc': 'file_storage/call_z7Mf6VF2TPmhf1Kchq3B0YPc.json'}

exec(code, env_args)
