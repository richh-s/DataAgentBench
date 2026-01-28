code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

funding = load_records(var_call_okz6iv72HTp7OX2p4MDtyMaz)
docs = load_records(var_call_s6w1q98gQI4S5Cy7We9V1SUX)

funding_names = set(r['Project_Name'] for r in funding if r.get('Project_Name') is not None)

# Heuristic extraction: capture project names under "Capital Improvement Projects (Design)" sections
extracted = set()
for d in docs:
    text = d.get('text','') or ''
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    # limit to design section until next major header
    start = text.find('Capital Improvement Projects (Design)')
    sub = text[start:]
    m = re.search(r'\nCapital Improvement Projects \((Construction|Not Started)\)', sub)
    if m:
        sub = sub[:m.start()]
    m = re.search(r'\nDisaster Recovery Projects', sub)
    if m:
        sub = sub[:m.start()]

    # Candidate lines: not bullets/updates/schedule/page headers
    for line in sub.splitlines():
        line = line.strip()
        if not line:
            continue
        if any(line.startswith(p) for p in ['(cid', 'Page ', 'Agenda Item', 'RECOMMENDED ACTION', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject:']):
            continue
        if ':' in line:  # likely label lines
            continue
        if line.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'project description', 'complete design', 'advertise', 'begin construction', 'final design')):
            continue
        # keep reasonably short title-like lines
        if len(line) > 120:
            continue
        # filter out generic headers
        if line in ['Capital Improvement Projects (Design)']:
            continue
        # if it matches funding project name, keep
        if line in funding_names:
            extracted.add(line)

count = len(extracted)

print('__RESULT__:')
print(json.dumps({'count': count, 'projects': sorted(extracted)}))"""

env_args = {'var_call_zM1VWuHGFpMN9eDHqG2PYKJx': [{'cnt': '276'}], 'var_call_s6w1q98gQI4S5Cy7We9V1SUX': 'file_storage/call_s6w1q98gQI4S5Cy7We9V1SUX.json', 'var_call_okz6iv72HTp7OX2p4MDtyMaz': 'file_storage/call_okz6iv72HTp7OX2p4MDtyMaz.json'}

exec(code, env_args)
