code = """import json, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

funding = load_records(var_call_5lVP2DizuUF3118inIDYRs6q)
docs = load_records(var_call_LLQROfTnEfL0VhuwwQ2uwiYk)

fund_names = {r['Project_Name'] for r in funding}

# For each document, locate the 'Capital Improvement Projects (Design)' section
# and capture project names that appear as standalone lines (title-cased-ish) until next section.
project_set = set()

section_start_pat = re.compile(r'Capital Improvement Projects\s*\(Design\)', re.IGNORECASE)
section_end_pat = re.compile(r'Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    m = section_start_pat.search(text)
    if not m:
        continue
    start = m.end()
    end_m = section_end_pat.search(text, pos=start)
    end = end_m.start() if end_m else len(text)
    sec = text[start:end]

    # Split lines; candidate project name lines are non-empty, not bullets/updates/schedule/page/etc.
    for line in sec.splitlines():
        s = line.strip()
        if not s:
            continue
        # skip common non-names
        if re.match(r'^(\(cid:|\u2022|\-|\*|\d+\.|Page\s+\d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:|Updates:|Project Schedule|Estimated Schedule|Complete Design|Advertise|Begin Construction|Final Design|Project Description)', s, flags=re.IGNORECASE):
            continue
        # skip lines that are clearly sentence fragments
        if len(s) < 4 or len(s) > 120:
            continue
        if s.endswith(':'):
            continue
        # Require that line has letters and not too many punctuation
        if re.search(r'[A-Za-z]', s) is None:
            continue
        # Many project titles are in Title Case; accept if it doesn't contain many commas and doesn't start with 'City'
        if s.count(',') > 0:
            continue
        # exclude lines that look like schedule values
        if re.search(r'\b(Summer|Spring|Fall|Winter)\b\s*\d{4}', s, flags=re.IGNORECASE):
            continue
        # Candidate: if it matches a funding project name exactly
        if s in fund_names:
            project_set.add(s)

cnt = len(project_set)
print('__RESULT__:')
print(json.dumps({'count': cnt, 'projects': sorted(project_set)[:50]}))"""

env_args = {'var_call_AtWp8N0yPoJFsVqy5PzpNZq6': [{'cnt': '276'}], 'var_call_LLQROfTnEfL0VhuwwQ2uwiYk': 'file_storage/call_LLQROfTnEfL0VhuwwQ2uwiYk.json', 'var_call_5lVP2DizuUF3118inIDYRs6q': 'file_storage/call_5lVP2DizuUF3118inIDYRs6q.json'}

exec(code, env_args)
