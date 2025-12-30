code = """import re, json, pandas as pd

funding_records = var_call_D95PaecIGGxwuyYUUqSYYM6P
if isinstance(funding_records, str) and funding_records.endswith('.json'):
    with open(funding_records, 'r') as f:
        funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
projects_over_50k = set(funding_df.loc[funding_df['Amount'] > 50000, 'Project_Name'])

civic_docs = var_call_6yMDUgDVwGJpQhTAWsdxxCj5
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

lines = full_text.splitlines()

design_projects = set()

in_design = False
for line in lines:
    l = line.strip()
    if not l:
        continue
    if 'Capital Improvement Projects (Design)' in l:
        in_design = True
        continue
    if in_design and l.startswith('Capital Improvement Projects (') and 'Design' not in l:
        in_design = False
    if in_design:
        if 'Updates' in l or 'Project Schedule' in l or 'Estimated Schedule' in l or 'Project Description' in l:
            continue
        if ':' in l:
            continue
        if re.match(r'^[A-Z0-9].*', l):
            design_projects.add(l)

for pname in projects_over_50k:
    if 'Design' in pname:
        design_projects.add(pname)

normalized_funding = {p.lower(): p for p in projects_over_50k}

count = 0
matched_projects = []
for dp in design_projects:
    key = dp.lower()
    if key in normalized_funding:
        count += 1
        matched_projects.append(normalized_funding[key])

result = {"count_design_capital_projects_over_50k": count, "matched_projects": matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_D95PaecIGGxwuyYUUqSYYM6P': 'file_storage/call_D95PaecIGGxwuyYUUqSYYM6P.json', 'var_call_6yMDUgDVwGJpQhTAWsdxxCj5': 'file_storage/call_6yMDUgDVwGJpQhTAWsdxxCj5.json'}

exec(code, env_args)
