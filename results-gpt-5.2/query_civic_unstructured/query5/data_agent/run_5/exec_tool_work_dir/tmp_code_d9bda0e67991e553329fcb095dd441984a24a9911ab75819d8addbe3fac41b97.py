code = """import json, re
from pathlib import Path

docs = var_call_WejKRxKgnE1X3SiXM0DUY3ew
if isinstance(docs, str) and docs.endswith('.json'):
    docs = json.loads(Path(docs).read_text())

section_re = re.compile(r"Disaster Recovery Projects.*?(?=\n\s*(?:Capital Improvement Projects|$))", re.IGNORECASE | re.DOTALL)
proj_re = re.compile(r"\n\s*([A-Z0-9][^\n]{3,120}?)\n\s*\(cid:190\)\s*Updates?:", re.IGNORECASE)
begin_re = re.compile(r"Begin\s+Construction\s*:\s*([^\n]+)", re.IGNORECASE)

records = []
for d in docs:
    text = d.get('text','') or ''
    for sec in section_re.findall(text):
        it = list(proj_re.finditer(sec))
        for idx, m in enumerate(it):
            name = m.group(1).strip()
            end = it[idx+1].start(1) if idx+1 < len(it) else len(sec)
            chunk = sec[m.start():end]
            begins = begin_re.findall(chunk)
            begin_val = begins[0].strip() if begins else None
            records.append({'Project_Name': name, 'type': 'disaster', 'st': begin_val, 'source_file': d.get('filename')})

started_2022 = [r for r in records if r.get('st') and '2022' in r['st']]
proj_names = sorted(set(r['Project_Name'] for r in started_2022))

out = {'disaster_projects_started_2022': proj_names, 'n': len(proj_names)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gGrVATjcKpu2cmnEAI1piIqa': ['Funding'], 'var_call_K4Hq7Nmz8VWu8C47Iqn6Rw7q': ['civic_docs'], 'var_call_WejKRxKgnE1X3SiXM0DUY3ew': 'file_storage/call_WejKRxKgnE1X3SiXM0DUY3ew.json'}

exec(code, env_args)
