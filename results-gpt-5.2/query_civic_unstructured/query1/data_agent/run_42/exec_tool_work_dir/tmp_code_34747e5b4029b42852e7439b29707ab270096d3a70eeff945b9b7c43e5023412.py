code = """import json, re

path = var_call_kmcAa0Vk1QVOQrIeBD8TN7W3
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

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

    section = section.replace('(cid:190)', '\\n').replace('(cid:131)', ' ')

    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.search(r"^(Updates|Project Schedule|Estimated Schedule|Final Design|Advertise|Begin Construction|Page \\d+ of \\d+|Agenda Item|DISCUSSION:|RECOMMENDED ACTION:)$", ln, re.IGNORECASE):
            continue
        if len(ln) < 4:
            continue
        if ln.endswith(':'):
            continue
        window = "\\n".join(lines[i+1:i+7])
        if re.search(r"\\bUpdates\\b|\\bProject Schedule\\b|\\bEstimated Schedule\\b|\\bProject Description\\b", window, re.IGNORECASE):
            if 'Capital Improvement Projects' in ln:
                continue
            projects_design_capital.add(ln)

print('__RESULT__:')
print(json.dumps({'projects_design_capital': sorted(projects_design_capital), 'n_design_capital': len(projects_design_capital)}))"""

env_args = {'var_call_KFAXzxfc3ZpVXH46fYupleAa': [{'cnt': '276'}], 'var_call_kmcAa0Vk1QVOQrIeBD8TN7W3': 'file_storage/call_kmcAa0Vk1QVOQrIeBD8TN7W3.json'}

exec(code, env_args)
