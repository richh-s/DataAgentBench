code = """import json, re
import pandas as pd

# Load mongo docs
path = var_call_K2hwlcqqTZL2gfcVFExZ9mfr
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic parser for project blocks
# We focus on Disaster Recovery Projects section and extract each project name with its schedule lines.
projects = []
for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    # isolate portion after header if possible
    idx = text.find('Disaster Recovery Projects')
    sub = text[idx:]
    # stop at next major header if present
    mstop = re.search(r'\n\s*Capital Improvement Projects\b', sub)
    # keep whole sub; disaster section often follows capital, so not safe.

    # Split into lines and scan
    lines = [ln.strip() for ln in sub.splitlines()]
    current = None
    buf = []
    in_disaster = False
    for ln in lines:
        if re.search(r'^Disaster Recovery Projects', ln):
            in_disaster = True
            current = None
            buf = []
            continue
        if not in_disaster:
            continue
        # end if another top-level section encountered
        if re.match(r'^(Capital Improvement Projects|Public Works Quarterly|RECOMMENDED ACTION|DISCUSSION:)', ln):
            if current:
                projects.append({'Project_Name': current, 'details':'\n'.join(buf), 'source_file': d.get('filename')})
            in_disaster = False
            current = None
            buf = []
            continue
        # detect a project title line: non-empty, no bullet char, not 'Updates'/'Project Schedule'
        if ln and not ln.startswith('(cid') and ln not in ['Updates:', 'Project Schedule:', 'Estimated Schedule:']:
            # many agenda texts use blank lines around titles; titles usually have no colon and not start with bullets
            # treat as title if next lines include 'Updates' or 'Project Schedule' soon; we can't lookahead easily, but accept if it contains keywords like 'Project'
            if (('Project' in ln) or ('Repair' in ln) or ('Repairs' in ln) or ('Restoration' in ln) or ('Recovery' in ln) or ('Slope' in ln) or ('Road' in ln) or ('Canyon' in ln) or ('Drainage' in ln) or ('Storm' in ln) or ('Park' in ln)) and len(ln) < 120:
                # If we already have a current project and this looks like a new title, flush previous
                if current and ln != current and (re.search(r'\bUpdates\b', '\n'.join(buf)) or re.search(r'\bSchedule\b', '\n'.join(buf)) or len(buf)>0):
                    projects.append({'Project_Name': current, 'details':'\n'.join(buf), 'source_file': d.get('filename')})
                    buf = []
                current = ln
                continue
        if current:
            buf.append(ln)
    if current:
        projects.append({'Project_Name': current, 'details':'\n'.join(buf), 'source_file': d.get('filename')})

# Determine which disaster projects started in 2022 by looking for 'Begin Construction' / 'Begin' lines containing 2022
started_2022 = set()
for p in projects:
    det = p['details']
    # look for begin/start markers
    if re.search(r'(Begin (Construction|construction)|Begin|Start|Started)\s*:\s*[^\n]*2022', det):
        started_2022.add(p['Project_Name'])
    elif re.search(r'2022', det) and re.search(r'Begin (Construction|construction)', det):
        # any line with begin construction and 2022 somewhere
        started_2022.add(p['Project_Name'])

# Some docs might not have explicit begin construction line. Also allow st like '2022-' in details with 'Project Schedule'
# Keep only unique
started_2022 = sorted(started_2022)

print('__RESULT__:')
print(json.dumps({'disaster_projects_started_2022': started_2022, 'count': len(started_2022)}))"""

env_args = {'var_call_BeorDsx8JrPIuB2mlCATPqZZ': ['Funding'], 'var_call_OADTgr7Ub1LCEk7c1kButQGv': ['civic_docs'], 'var_call_K2hwlcqqTZL2gfcVFExZ9mfr': 'file_storage/call_K2hwlcqqTZL2gfcVFExZ9mfr.json'}

exec(code, env_args)
