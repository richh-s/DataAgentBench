code = """import json, re

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

recs = load_records(var_call_wdpKCzaziu8R6N0HjcFJdX7l)

text_all = "\n".join([r.get('text','') for r in recs])

# Parse Disaster Recovery section items that contain schedules
lines = text_all.splitlines()
projects = []
current = None
in_disaster = False
for i, raw in enumerate(lines):
    line = raw.strip()
    if re.search(r"^Disaster Recovery Projects", line, re.I):
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
    # project name lines are typically standalone and not starting with bullets/labels
    if not line.startswith(('(cid:', '•', '-', '(cid', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'Complete', 'Advertise', 'Begin', 'Final', 'Design', 'Construction', 'Notice', 'Staff')) and not re.match(r"^(Page \d+|Agenda Item)", line):
        # ignore subheaders like (Design)/(Construction)/(Not Started)
        if re.match(r"^\(?(Design|Construction|Not Started)\)?$", line, re.I):
            continue
        # likely a project name
        current = {'Project_Name': line, 'schedule_text': ''}
        projects.append(current)
        continue
    if current is not None:
        if re.search(r"(Project Schedule|Estimated Schedule|Begin|Start|Advertise)", line, re.I) or re.search(r"\b2022\b", line):
            current['schedule_text'] += ' ' + line

# Determine started in 2022 if schedule mentions Begin construction and 2022, or start/begin in 2022
started_2022 = []
for p in projects:
    stxt = p.get('schedule_text','')
    if re.search(r"Begin (Construction|construction)\s*:\s*[^\n]*2022", stxt):
        started_2022.append(p['Project_Name'])
    elif re.search(r"\bBegin\b[^\n]*2022", stxt) or re.search(r"\bStart\b[^\n]*2022", stxt):
        started_2022.append(p['Project_Name'])

started_2022 = sorted(set(started_2022))
print('__RESULT__:')
print(json.dumps({'started_2022_disaster_projects': started_2022, 'count': len(started_2022)}))"""

env_args = {'var_call_kG8ZQWCW2AVY2ZXpQKanylNW': ['Funding'], 'var_call_jVGLGQgarGHvy0J91PYPUfMo': ['civic_docs'], 'var_call_jDyoHOwxFQnWh3YXVXOOXXe1': 'file_storage/call_jDyoHOwxFQnWh3YXVXOOXXe1.json', 'var_call_wdpKCzaziu8R6N0HjcFJdX7l': 'file_storage/call_wdpKCzaziu8R6N0HjcFJdX7l.json'}

exec(code, env_args)
