code = """import json, re, os

funding_records = var_call_Zt23CqLTy7mMoHl9YsBn40Uf

if isinstance(var_call_4uceinGyYaO22kHnN5TGdn3p, str) and os.path.isfile(var_call_4uceinGyYaO22kHnN5TGdn3p):
    with open(var_call_4uceinGyYaO22kHnN5TGdn3p, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_call_4uceinGyYaO22kHnN5TGdn3p

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

sections = re.split(r'Capital Improvement Projects \(Design\)', full_text, flags=re.IGNORECASE)
capital_design_projects = set()
if len(sections) > 1:
    design_block = sections[1]
    design_block = re.split(r'Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)', design_block, flags=re.IGNORECASE)[0]
    for line in design_block.split('\n'):
        line = line.strip()
        if not line:
            continue
        if len(line.split()) < 2:
            continue
        lower = line.lower()
        if 'updates' in lower or 'project schedule' in lower or 'estimated schedule' in lower or 'cid:' in lower:
            continue
        if line.endswith('.'):
            continue
        capital_design_projects.add(line)

project_name_to_amount = {r['Project_Name']: int(r['Amount']) for r in funding_records}

count = 0
for pname in capital_design_projects:
    if pname in project_name_to_amount and project_name_to_amount[pname] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_Zt23CqLTy7mMoHl9YsBn40Uf': 'file_storage/call_Zt23CqLTy7mMoHl9YsBn40Uf.json', 'var_call_4uceinGyYaO22kHnN5TGdn3p': 'file_storage/call_4uceinGyYaO22kHnN5TGdn3p.json'}

exec(code, env_args)
