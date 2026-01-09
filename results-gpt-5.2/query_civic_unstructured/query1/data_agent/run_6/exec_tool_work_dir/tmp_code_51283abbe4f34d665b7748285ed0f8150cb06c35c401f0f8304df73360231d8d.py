code = """import json, re, pandas as pd

# Load funding project names > 50k
src = var_call_fmcWhdDlFfhgtgN3OXIg8ml4
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        hi_projects = json.load(f)
else:
    hi_projects = src
hi_set = {r['Project_Name'] for r in hi_projects if r.get('Project_Name')}

# Load civic docs
docs_src = var_call_LnczIrPl6GnyO0CnkkqWqEqa
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Determine which of the high-funded projects have 'design' status in any doc.
# Heuristic: project name appears near a header like 'Capital Improvement Projects (Design)' or '(Design)'
# We'll treat as design if found in a doc section explicitly labeled design.

def normalize(s):
    return re.sub(r"\s+", " ", s.strip().lower())

hi_norm = {normalize(p): p for p in hi_set}

# Build patterns
escaped = [(normalize(p), re.escape(p)) for p in hi_set]

# We'll scan each document: find ranges of text that are under a 'Design' section.
# Use simple approach: for each occurrence of a design header, take text until next section header with (Construction) or (Not Started) or 'Disaster Recovery Projects' etc.

design_projects = set()

section_end_re = re.compile(r"\n\s*(Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects|\Z)", re.IGNORECASE)

design_header_re = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)

for d in docs:
    text = d.get('text') or ''
    if not text:
        continue
    # Find all design sections
    for m in design_header_re.finditer(text):
        start = m.end()
        # Find end of section
        m_end = section_end_re.search(text, pos=start)
        end = m_end.start() if m_end else len(text)
        section = text[start:end]
        # For each high-funded project, check presence in section
        # Optimize by checking line-based names: consider each line, compare normalized line to normalized project
        for line in section.splitlines():
            ln = normalize(line)
            if not ln or len(ln) < 3:
                continue
            if ln in hi_norm:
                design_projects.add(hi_norm[ln])

# Also consider explicit '(Design)' tag next to project name, even outside the header.
for d in docs:
    text = d.get('text') or ''
    if not text:
        continue
    lower = text.lower()
    if 'design' not in lower:
        continue
    for p in hi_set:
        # match 'Project Name' followed by optional whitespace and '(Design)'
        pat = re.compile(re.escape(p) + r"\s*\(\s*Design\s*\)", re.IGNORECASE)
        if pat.search(text):
            design_projects.add(p)

result = {"count": int(len(design_projects))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7G4HZCk8nvjTtr9jK1UPWCPI': [{'cnt': '276'}], 'var_call_LnczIrPl6GnyO0CnkkqWqEqa': 'file_storage/call_LnczIrPl6GnyO0CnkkqWqEqa.json', 'var_call_fmcWhdDlFfhgtgN3OXIg8ml4': 'file_storage/call_fmcWhdDlFfhgtgN3OXIg8ml4.json'}

exec(code, env_args)
