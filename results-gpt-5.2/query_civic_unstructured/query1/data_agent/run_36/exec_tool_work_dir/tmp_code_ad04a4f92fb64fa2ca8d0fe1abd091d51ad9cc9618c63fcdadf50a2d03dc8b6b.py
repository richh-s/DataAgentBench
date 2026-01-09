code = """import json, re
import pandas as pd

# Load mongo docs (may be in a file)
raw = var_call_kZN5vnZ1R2hyRTBYRZjd2yDZ
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# Extract project names under 'Capital Improvement Projects (Design)'
projects_design = set()

# Patterns to locate the design section and stop at next major section
start_pat = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
stop_pat = re.compile(r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects\s*\(", re.IGNORECASE)

for d in docs:
    text = d.get('text') or ''
    # find all occurrences per doc
    for m in start_pat.finditer(text):
        start = m.end()
        sub = text[start:]
        sm = stop_pat.search(sub)
        if sm:
            sub = sub[:sm.start()]
        # split lines and capture likely project name lines
        for line in sub.splitlines():
            ln = line.strip()
            if not ln:
                continue
            # skip bullets/headers
            if re.match(r"^(\(cid:|Page\s+\d+|Agenda Item|Updates:|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION)\b", ln, re.IGNORECASE):
                continue
            # likely names: mostly letters/numbers/&/ - and not ending with ':'
            if len(ln) > 3 and len(ln) < 120 and not ln.endswith(':'):
                # exclude lines that are sentences
                if re.search(r"\b(is|are|will|working|submitted|expecting|received|rejected|awaiting|field)\b", ln, re.IGNORECASE):
                    continue
                # exclude section titles
                if re.search(r"^(Capital|Disaster)\b", ln, re.IGNORECASE):
                    continue
                # Accept
                projects_design.add(ln)

# Query funding table already returned count of distinct projects with Amount>50000 (but not joined)
# We need intersection with design projects.

# Pull all funding > 50000 with project names

# We'll query via SQL? Not available here; use existing funding count only isn't enough.
# Therefore, approximate by using design set and count those that exist in Funding >50000 by querying now is not possible in python.
# However we can embed funding query results? Not.

print('__RESULT__:')
print(json.dumps({'design_projects_extracted_count': len(projects_design), 'sample': sorted(list(projects_design))[:30]}))"""

env_args = {'var_call_8LTewYVZ6vCazy4Nbo67HRc1': [{'cnt': '276'}], 'var_call_kZN5vnZ1R2hyRTBYRZjd2yDZ': 'file_storage/call_kZN5vnZ1R2hyRTBYRZjd2yDZ.json'}

exec(code, env_args)
