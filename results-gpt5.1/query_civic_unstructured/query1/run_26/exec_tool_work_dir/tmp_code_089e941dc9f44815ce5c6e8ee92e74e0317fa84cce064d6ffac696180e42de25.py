code = """import re, json

funding_records = var_call_u5Y6Md7vn139uNl1NNlLsbzI
civic_docs = var_call_dm9v833eUHokmhj2EmtnJPjo

project_status = {}
current_type = None
current_status = None

for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for line in lines:
        lower = line.lower()
        if 'capital improvement projects' in lower:
            current_type = 'capital'
            if '(design)' in lower:
                current_status = 'design'
            elif '(construction)' in lower:
                current_status = 'completed'
            elif '(not started)' in lower:
                current_status = 'not started'
            continue
        if lower.startswith('disaster recovery projects'):
            current_type = 'disaster'
            current_status = None
            continue
        if current_type == 'capital' and current_status:
            if (':' not in line and 'updates' not in lower and 'project schedule' not in lower and 'estimated schedule' not in lower and not lower.startswith('agenda item') and not lower.startswith('page ')) and len(line.split()) <= 10:
                name = line.strip()
                if name and 'capital improvement projects (design)' not in name.lower():
                    project_status[name] = {'type': current_type, 'status': current_status}

count = 0
for rec in funding_records:
    pname = rec['Project_Name']
    info = project_status.get(pname)
    if not info:
        base = re.sub(r'\s*\(.*?\)\s*', '', pname).strip()
        info = project_status.get(base)
    if info and info['type'] == 'capital' and info['status'] == 'design':
        count += 1

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_u5Y6Md7vn139uNl1NNlLsbzI': 'file_storage/call_u5Y6Md7vn139uNl1NNlLsbzI.json', 'var_call_dm9v833eUHokmhj2EmtnJPjo': 'file_storage/call_dm9v833eUHokmhj2EmtnJPjo.json'}

exec(code, env_args)
