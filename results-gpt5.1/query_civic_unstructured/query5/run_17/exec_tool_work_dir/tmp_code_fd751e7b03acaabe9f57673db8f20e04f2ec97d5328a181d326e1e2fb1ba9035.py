code = """import re, json, pandas as pd

path = var_call_BD9pzb58Cb5ePZ0S2hPMVuRN
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = var_call_uOcltXhkruajirNrJFOEVnN0
if isinstance(funding, str):
    with open(funding,'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding

rows = []
for r in funding_records:
    name = r['Project_Name']
    is_disaster = ('FEMA' in name) or ('CalOES' in name) or ('CalJPIA' in name)
    if is_disaster:
        rows.append(r)

# Very limited info on start dates; approximate by checking civic_docs for '2022' and project name co-occurring.

start_2022_projects = set()
texts = '\n'.join(doc.get('text','') for doc in civic_docs)
for r in rows:
    name = r['Project_Name']
    base_name = name.split('(')[0].strip()
    pattern = re.escape(base_name)
    if re.search(pattern + ".*2022", texts) or re.search("2022.*" + pattern, texts):
        start_2022_projects.add(name)

total = 0
for r in rows:
    if r['Project_Name'] in start_2022_projects:
        try:
            total += int(r['Amount'])
        except Exception:
            pass

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_BD9pzb58Cb5ePZ0S2hPMVuRN': 'file_storage/call_BD9pzb58Cb5ePZ0S2hPMVuRN.json', 'var_call_uOcltXhkruajirNrJFOEVnN0': 'file_storage/call_uOcltXhkruajirNrJFOEVnN0.json'}

exec(code, env_args)
