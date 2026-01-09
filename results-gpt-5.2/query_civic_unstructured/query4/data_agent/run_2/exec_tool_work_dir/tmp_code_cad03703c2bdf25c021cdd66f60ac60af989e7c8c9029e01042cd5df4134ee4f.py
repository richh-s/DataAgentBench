code = """import json, re

# Load mongo docs (possibly a json file path)
raw = var_call_sir3H7yoilAVtxp9uzAjCNCs
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# Extract project names with 'Begin Construction: Spring 2022' (started in Spring 2022)
projects = set()
for d in docs:
    text = d.get('text','')
    # normalize bullets
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'\bBegin\s+Construction\s*:\s*Spring\s+2022\b', line, flags=re.I):
            # find nearest prior non-empty line that looks like a project name
            j = i-1
            while j>=0 and (lines[j].strip()=='' or re.search(r'^(\(cid:|\u2022|\*|\-|\d+\.|Page\s+\d+|Agenda Item)', lines[j].strip())):
                j -= 1
            if j>=0:
                name = lines[j].strip()
                # exclude obvious headers
                if not re.search(r'^(Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Updates|Estimated Schedule|Project Description)', name, flags=re.I):
                    projects.add(name)

projects_list = sorted(projects)
print('__RESULT__:')
print(json.dumps({'projects': projects_list, 'count': len(projects_list)}))"""

env_args = {'var_call_voCW34f5mhpr4lBcDrP0GdJi': ['Funding'], 'var_call_beaAEvwBIwRzy1HcSw5H4XHD': ['civic_docs'], 'var_call_sir3H7yoilAVtxp9uzAjCNCs': 'file_storage/call_sir3H7yoilAVtxp9uzAjCNCs.json'}

exec(code, env_args)
