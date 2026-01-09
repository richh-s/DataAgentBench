code = """import json, re

path = var_call_rqk86h5PbRqU7Jnxdv2SDM7u
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

section_pat = re.compile(r'(Capital Improvement Projects \(Design\)|Disaster Recovery Projects \(Design\))\s*(.*?)(?=\n\s*(Capital Improvement Projects \(|Disaster Recovery Projects \(|Page \d+ of \d+|Agenda Item|\Z))', re.S|re.I)

projects=set()
skip_prefixes = ('(cid', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description',
                 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by',
                 'Date prepared', 'Meeting date', 'Subject:')

for d in docs:
    text = d.get('text','') or ''
    for m in section_pat.finditer(text):
        block = m.group(2)
        for line in block.split('\n'):
            line=line.strip()
            if not line:
                continue
            if line.startswith(skip_prefixes):
                continue
            if len(line) < 3 or len(line) > 120:
                continue
            if re.match(r'^[\W_]+$', line):
                continue
            if ':' in line:
                continue
            if line.endswith('.'):
                continue
            if re.search(r'[A-Za-z]', line) and not line.lower().startswith('page '):
                projects.add(line)

# funded projects > 50k
funded = var_call_tFCzG6Ku9PapCLRhaw4QyROM  # not used; this is count only

print('__RESULT__:')
print(json.dumps({'design_projects_extracted_sample': sorted(list(projects))[:20], 'n_design_projects_extracted': len(projects)}))"""

env_args = {'var_call_tFCzG6Ku9PapCLRhaw4QyROM': [{'cnt': '276'}], 'var_call_rqk86h5PbRqU7Jnxdv2SDM7u': 'file_storage/call_rqk86h5PbRqU7Jnxdv2SDM7u.json'}

exec(code, env_args)
