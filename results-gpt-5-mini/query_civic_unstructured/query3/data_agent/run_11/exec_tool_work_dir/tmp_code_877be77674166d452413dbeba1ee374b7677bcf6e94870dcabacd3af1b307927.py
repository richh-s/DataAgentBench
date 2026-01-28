code = """import json, re
path = var_call_2ajh9JRnLUZjcgZaBU1zv32y
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()
proj_title_re = re.compile(r"\b(Project|Improvements|Repairs|Repair|Facility|Park|Playground|Study|Plan|Master Plan|Walkway|Retaining Wall|Drive|Road|Signal|Signs|Water Treatment|Backup Power|Trash Screens)\b", re.I)

for doc in docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        low = ln.lower()
        if 'fema' in low or 'emergency' in low or 'emergency warning' in low:
            # look backward for a project title
            title = None
            title_idx = None
            for j in range(i, max(-1, i-10), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # prefer lines that contain a project keyword
                if proj_title_re.search(cand) and len(cand) < 200:
                    title = re.sub(r"\s+", " ", cand).strip()
                    title_idx = j
                    break
            if title is None:
                # fallback: use the line containing FEMA/emergency (trim to 100 chars)
                title = re.sub(r"\s+", " ", ln).strip()
                title_idx = i

            # determine status from nearby context (look forward 6 lines and backward 6)
            start = max(0, title_idx-6)
            end = min(len(lines), title_idx+7)
            context = '\n'.join(lines[start:end]).lower()
            status = None
            if re.search(r'construction was completed|complete construction|notice of completion|completed,|complete construction:', context):
                status = 'completed'
            elif re.search(r'awaiting|awaiting final|awaiting approval|waiting|waiting for|not started|identified', context):
                status = 'not started'
            elif re.search(r'preliminary design|preliminary|working with the consultant to finalize the design|finalize the design|complete design|design phase|design is|project is in the preliminary design|project is in preliminary design|begin construction|begin construction:', context):
                # treat begin construction as in-progress/design
                status = 'design'
            else:
                status = 'not started'

            if title not in seen:
                seen.add(title)
                projects.append({'Project_Name': title, 'Status': status})

# sort
projects = sorted(projects, key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps(projects))"""

env_args = {'var_call_2ajh9JRnLUZjcgZaBU1zv32y': 'file_storage/call_2ajh9JRnLUZjcgZaBU1zv32y.json'}

exec(code, env_args)
