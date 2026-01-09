code = """import json, re, pandas as pd

# Load funding>50k project list
funding_src = var_call_nnHzOTd1fREYKiodYXvdMQ8e
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src
funding_projects = {r['Project_Name'] for r in funding}

# Load civic docs
docs_src = var_call_dCvRlrtmX7a7qTsDXXPHhXNO
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Determine which projects have 'design' status by detecting them in "Design" section lists.
# Heuristic: if a project name appears in a line within a section headed by "(Design)" or "Projects Under Design".

design_projects = set()

# precompile regexes
header_re = re.compile(r"\(Design\)|Projects Under Design|Under Design", re.IGNORECASE)
stop_header_re = re.compile(r"\(Construction\)|\(Not Started\)|\(Completed\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Construction\)|Disaster Recovery Projects \(Not Started\)|Disaster Recovery Projects \(Completed\)", re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    in_design = False
    for ln in lines:
        if header_re.search(ln):
            in_design = True
            continue
        if in_design and stop_header_re.search(ln):
            in_design = False
            continue
        if not in_design:
            continue
        if not ln or len(ln) < 4:
            continue
        # skip bullet/metadata lines
        if ln.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'project description', 'discussion', 'recommended action', 'page ')):
            continue
        if re.match(r"^[\(\[\{]?cid:|^[\u2022\-\*]\s*", ln, flags=re.IGNORECASE):
            continue
        # Consider it a project line if it contains letters and no colon and not too long
        if ':' in ln:
            continue
        if re.search(r"[A-Za-z]", ln) is None:
            continue
        if len(ln) > 120:
            continue
        design_projects.add(ln)

# intersect with funding>50k projects
answer_count = len(design_projects & funding_projects)

print('__RESULT__:')
print(json.dumps({'count': answer_count}))"""

env_args = {'var_call_nnHzOTd1fREYKiodYXvdMQ8e': 'file_storage/call_nnHzOTd1fREYKiodYXvdMQ8e.json', 'var_call_dCvRlrtmX7a7qTsDXXPHhXNO': 'file_storage/call_dCvRlrtmX7a7qTsDXXPHhXNO.json'}

exec(code, env_args)
