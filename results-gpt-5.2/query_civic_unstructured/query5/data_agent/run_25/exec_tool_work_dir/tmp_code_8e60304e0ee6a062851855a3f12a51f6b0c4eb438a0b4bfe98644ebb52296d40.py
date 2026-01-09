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

        # project name heuristic: contains (FEMA/CalJPIA/CalOES) or ends with Project)
        is_project_name = False
        if re.search(r"\((FEMA|CalJPIA|CalOES)\s*Project\)", line, re.I):
            is_project_name = True
        if re.search(r"\((FEMA|CalJPIA|CalOES)\)", line, re.I) and 'Project' in line:
            is_project_name = True
        if re.search(r"Project\)$", line) and '(' in line:
            is_project_name = True

        if is_project_name:
            current = {'Project_Name': line, 'schedule_text': ''}
            projects.append(current)
            continue

        if current is not None:
            if re.search(r"(Begin|Start|Award)\\s+Construction", line, re.I) or re.search(r"Begin\\s+Construction", line, re.I):
                current['schedule_text'] += ' ' + line

started_2022 = []
for p in projects:
    stxt = p.get('schedule_text','')
    if re.search(r"(Begin|Start|Award)\\s+.*Construction\s*:\s*[^\\n]*2022", stxt, re.I):
        started_2022.append(p['Project_Name'])

started_2022 = sorted(set(started_2022))
print('__RESULT__:')
print(json.dumps({'started_2022_disaster_projects': started_2022, 'count': len(started_2022)}))"""

env_args = {'var_call_kG8ZQWCW2AVY2ZXpQKanylNW': ['Funding'], 'var_call_jVGLGQgarGHvy0J91PYPUfMo': ['civic_docs'], 'var_call_jDyoHOwxFQnWh3YXVXOOXXe1': 'file_storage/call_jDyoHOwxFQnWh3YXVXOOXXe1.json', 'var_call_wdpKCzaziu8R6N0HjcFJdX7l': 'file_storage/call_wdpKCzaziu8R6N0HjcFJdX7l.json', 'var_call_ebmDP9U7vETKwz1Nt2kBhfZv': {'started_2022_disaster_projects': [], 'count': 0}, 'var_call_z7Mf6VF2TPmhf1Kchq3B0YPc': 'file_storage/call_z7Mf6VF2TPmhf1Kchq3B0YPc.json', 'var_call_8NeVT5nkAvKK0lvLybafZDhM': {'started_2022_disaster_projects': ['Summer 2022.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in April 2022.', 'beginning in Fall 2022.', 'beginning in Spring 2022.', 'bid with bids due November 17.', 'coming weeks.', 'completing the final design.', 'final design and preparing the project for public bidding.', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'of 2022.', 'started and is anticipated to be completed by the Spring of 2022.', 'timber with non-combustible materials.'], 'count': 16}}

exec(code, env_args)
