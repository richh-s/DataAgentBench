code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_PMr5zq0ajEpSTgyvqBA9I0b5)
fund = load_json_maybe(var_call_YiusZ3QcF3T7rRofI85mNe2T)

fund_map = {r['Project_Name']: float(r['total_amount']) for r in fund}

projects = []
pat_disaster_section = re.compile(r'Disaster Recovery Projects\s*(?:\(.*?\))?\s*(?P<body>.*?)(?=\n\s*Capital Improvement Projects|\Z)', re.IGNORECASE | re.DOTALL)
pat_project_block = re.compile(r'\n(?P<name>[A-Z][^\n]{2,120}?)\n\s*(?:\(cid:190\)\s*Updates:.*?\n)?\s*(?:\(cid:190\)\s*Project Schedule:|\(cid:190\)\s*Estimated Schedule:|\(cid:190\)\s*Project Schedule \(.*?\):|\(cid:190\)\s*Estimated Schedule \(.*?\):)(?P<sch>.*?)(?=\n[A-Z][^\n]{2,120}?\n\s*\(cid:190\)|\n\s*Capital Improvement Projects|\Z)', re.DOTALL)
pat_begin = re.compile(r'Begin\s+Construction\s*:\s*(?P<st>[^\n\r]+)', re.IGNORECASE)
pat_start = re.compile(r'(?:Start|Begin)\s*(?:Date|Time|Construction)?\s*:\s*(?P<st>[^\n\r]+)', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    msec = pat_disaster_section.search(text)
    if not msec:
        continue
    body = msec.group('body')
    for m in pat_project_block.finditer(body):
        name = m.group('name').strip()
        sch = m.group('sch')
        st = None
        mb = pat_begin.search(sch)
        if mb:
            st = mb.group('st').strip()
        else:
            ms = pat_start.search(sch)
            if ms:
                st = ms.group('st').strip()
        if st and '2022' in st:
            projects.append({'Project_Name': name, 'st': st, 'filename': d.get('filename')})

seen=set()
proj_2022=[]
for r in projects:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        proj_2022.append(r)

total = 0.0
missing=[]
for r in proj_2022:
    amt = fund_map.get(r['Project_Name'])
    if amt is None:
        missing.append(r['Project_Name'])
    else:
        total += amt

out = {
    'total_funding_disaster_projects_started_2022': int(total),
    'project_count': len(proj_2022),
    'matched_funded_project_count': len(proj_2022)-len(missing),
    'unmatched_project_names': missing
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WTMkebJ5tBXmyNTIG44oaAgK': ['Funding'], 'var_call_JtXuQbLdcCW8xiMPGowlZXtS': ['civic_docs'], 'var_call_PMr5zq0ajEpSTgyvqBA9I0b5': 'file_storage/call_PMr5zq0ajEpSTgyvqBA9I0b5.json', 'var_call_YiusZ3QcF3T7rRofI85mNe2T': 'file_storage/call_YiusZ3QcF3T7rRofI85mNe2T.json'}

exec(code, env_args)
