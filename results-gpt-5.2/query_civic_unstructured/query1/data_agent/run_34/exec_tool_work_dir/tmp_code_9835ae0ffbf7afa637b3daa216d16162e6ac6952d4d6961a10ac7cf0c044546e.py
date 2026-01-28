code = """import json, re

cd = var_call_gsbYlFUmFtwBGaBGpXKYjgoA
if isinstance(cd, str):
    with open(cd, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cd

fp = var_call_NvAkBh0AB6whaps5nn2niXAn
if isinstance(fp, str):
    with open(fp, 'r', encoding='utf-8') as f:
        funded = json.load(f)
else:
    funded = fp
funded_names = [r.get('Project_Name') for r in funded if r.get('Project_Name')]

# Extract design project names from common agenda report formatting
pattern = re.compile(r'Capital Improvement Projects\s*\(Design\)(.*?)(?:Capital Improvement Projects\s*\(|Disaster Recovery Projects\s*\(|\Z)', re.IGNORECASE | re.DOTALL)

all_design = set()
for d in civic_docs:
    text = d.get('text') or ''
    for m in pattern.finditer(text):
        block = m.group(1)
        for line in block.splitlines():
            ln = line.strip()
            if not ln:
                continue
            if re.search(r'^(\(cid|Page\s+\d+|Agenda Item|Updates|Project Schedule|Estimated Schedule|Complete Design|Advertise|Begin Construction)\b', ln, re.IGNORECASE):
                continue
            if 3 < len(ln) < 120 and re.search(r'[A-Za-z]', ln) and not ln.endswith(':'):
                if ln.lower() in {'discussion', 'recommended action'}:
                    continue
                all_design.add(ln)

funded_design = {name for name in funded_names if name in all_design}

print('__RESULT__:')
print(json.dumps({"count": int(len(funded_design))}))"""

env_args = {'var_call_WdBEy05jPeQ4xShF7NNuqxZ2': [{'cnt': '276'}], 'var_call_gsbYlFUmFtwBGaBGpXKYjgoA': 'file_storage/call_gsbYlFUmFtwBGaBGpXKYjgoA.json', 'var_call_NvAkBh0AB6whaps5nn2niXAn': 'file_storage/call_NvAkBh0AB6whaps5nn2niXAn.json'}

exec(code, env_args)
