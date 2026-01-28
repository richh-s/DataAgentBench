code = """import json, re

src = var_call_fmcWhdDlFfhgtgN3OXIg8ml4
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        hi_projects = json.load(f)
else:
    hi_projects = src
hi_set = {r.get('Project_Name') for r in hi_projects if r.get('Project_Name')}

src_docs = var_call_LnczIrPl6GnyO0CnkkqWqEqa
if isinstance(src_docs, str):
    with open(src_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src_docs

def normalize(s):
    return re.sub(r"\s+", " ", s.strip().lower())

hi_norm = {normalize(p): p for p in hi_set}

design_projects = set()

section_end_re = re.compile(r"\\n\\s*(Capital Improvement Projects\\s*\\((Construction|Not Started)\\)|Disaster Recovery Projects|\\Z)", re.IGNORECASE)

design_header_re = re.compile(r"Capital Improvement Projects\\s*\\(Design\\)", re.IGNORECASE)

for d in docs:
    text = d.get('text') or ''
    if not text:
        continue
    for m in design_header_re.finditer(text):
        start = m.end()
        m_end = section_end_re.search(text, pos=start)
        end = m_end.start() if m_end else len(text)
        section = text[start:end]
        for line in section.splitlines():
            ln = normalize(line)
            if ln in hi_norm:
                design_projects.add(hi_norm[ln])

for d in docs:
    text = d.get('text') or ''
    if not text:
        continue
    if 'design' not in text.lower():
        continue
    for p in hi_set:
        if re.search(re.escape(p) + r"\\s*\\(\\s*Design\\s*\\)", text, flags=re.IGNORECASE):
            design_projects.add(p)

out = {"count": int(len(design_projects))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7G4HZCk8nvjTtr9jK1UPWCPI': [{'cnt': '276'}], 'var_call_LnczIrPl6GnyO0CnkkqWqEqa': 'file_storage/call_LnczIrPl6GnyO0CnkkqWqEqa.json', 'var_call_fmcWhdDlFfhgtgN3OXIg8ml4': 'file_storage/call_fmcWhdDlFfhgtgN3OXIg8ml4.json'}

exec(code, env_args)
