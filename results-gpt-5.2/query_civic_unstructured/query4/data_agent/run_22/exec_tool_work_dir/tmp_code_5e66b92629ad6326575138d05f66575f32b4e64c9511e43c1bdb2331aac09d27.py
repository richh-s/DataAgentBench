code = """import json, re

mongo_path = var_call_p4HjSnYNUxe7NkRmq3vzuPCA
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

fund_path = var_call_oek2bn0tTBOuFoCdVj0yWRYv
with open(fund_path, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: float(r['Total_Amount']) for r in fund}

spring2022_pat = re.compile(r'(?:Spring\s+2022|2022\s*[-, ]\s*Spring)', re.IGNORECASE)

beginspring_pat = re.compile(r'(?:Begin(?:ning)?\s+(?:Construction|Design)|Begin|Start(?:ing)?\s+(?:Construction|Design)|Start)\s*:\s*Spring\s+2022', re.IGNORECASE)

project_started_spring_2022 = set()

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        name = None
        if ln in fund_map:
            name = ln
        else:
            ln2 = re.sub(r'^[•\-*]+\s*', '', ln)
            if ln2 in fund_map:
                name = ln2
        if not name:
            continue
        window = '\n'.join(lines[i:i+35])
        if spring2022_pat.search(window) and beginspring_pat.search(window):
            project_started_spring_2022.add(name)

count = len(project_started_spring_2022)
total_funding = sum(fund_map.get(n,0.0) for n in project_started_spring_2022)

result = {
    'projects_started_spring_2022_count': count,
    'projects_started_spring_2022_total_funding': int(total_funding),
    'projects': sorted(project_started_spring_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_p4HjSnYNUxe7NkRmq3vzuPCA': 'file_storage/call_p4HjSnYNUxe7NkRmq3vzuPCA.json', 'var_call_oek2bn0tTBOuFoCdVj0yWRYv': 'file_storage/call_oek2bn0tTBOuFoCdVj0yWRYv.json'}

exec(code, env_args)
