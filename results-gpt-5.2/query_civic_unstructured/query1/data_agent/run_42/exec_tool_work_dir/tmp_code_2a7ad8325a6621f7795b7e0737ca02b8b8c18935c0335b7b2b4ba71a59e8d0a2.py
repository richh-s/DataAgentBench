code = """import json, re
import pandas as pd

# Load civic docs
path = var_call_kmcAa0Vk1QVOQrIeBD8TN7W3
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract project names under "Capital Improvement Projects (Design)" sections
projects_design_capital = set()

design_header_re = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
next_section_re = re.compile(r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects\s*\(|$", re.IGNORECASE)

for d in docs:
    text = d.get('text') or ''
    m = design_header_re.search(text)
    if not m:
        continue
    start = m.end()
    m2 = next_section_re.search(text, start)
    end = m2.start() if m2 else len(text)
    section = text[start:end]

    # Clean odd encoding markers
    section = section.replace('(cid:190)', '\n').replace('(cid:131)', ' ')

    # Heuristic: project name is a non-empty line followed soon by "Updates" or "Project Schedule" or "Estimated Schedule" or "Project Description"
    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # skip obvious non-project lines
        if re.search(r"^(Updates|Project Schedule|Estimated Schedule|Final Design|Advertise|Begin Construction|Page \d+ of \d+|Agenda Item|DISCUSSION:|RECOMMENDED ACTION:)$", ln, re.IGNORECASE):
            continue
        if len(ln) < 4:
            continue
        # must not be a bullet-like or sentence
        if ln.endswith(':'):
            continue
        # lookahead within next 6 lines
        window = "\n".join(lines[i+1:i+7])
        if re.search(r"\bUpdates\b|\bProject Schedule\b|\bEstimated Schedule\b|\bProject Description\b", window, re.IGNORECASE):
            # exclude header-like lines
            if 'Capital Improvement Projects' in ln:
                continue
            projects_design_capital.add(ln)

# Funding > 50000 distinct project names
fund_cnt = int(var_call_KFAXzxfc3ZpVXH46fYupleAa[0]['cnt'])

# Need count of capital projects with design status and funding > 50000
# Query funding table for project names > 50000

print('__RESULT__:')
print(json.dumps({
    'projects_design_capital': sorted(projects_design_capital),
    'n_design_capital': len(projects_design_capital)
}))"""

env_args = {'var_call_KFAXzxfc3ZpVXH46fYupleAa': [{'cnt': '276'}], 'var_call_kmcAa0Vk1QVOQrIeBD8TN7W3': 'file_storage/call_kmcAa0Vk1QVOQrIeBD8TN7W3.json'}

exec(code, env_args)
