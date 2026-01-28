code = """import re, json, pandas as pd, os, json as jsonlib

funding_records = var_call_JzWsliya6BcFeSIPcWMfADGm

civic_source = var_call_02UigJJP75tL5mXPnfoaubJr
if isinstance(civic_source, str) and os.path.exists(civic_source):
    with open(civic_source, 'r') as f:
        civic_docs = jsonlib.load(f)
else:
    civic_docs = civic_source

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

sections = re.split(r'Capital Improvement Projects \(Design\)', full_text, flags=re.IGNORECASE)
if len(sections) > 1:
    design_block = sections[1]
else:
    design_block = ''

project_lines = []
for line in design_block.split('\n'):
    clean = line.strip()
    if not clean:
        continue
    low = clean.lower()
    if low.startswith('updates') or low.startswith('project schedule') or low.startswith('estimated schedule') or low.startswith('project description'):
        continue
    if clean.startswith('('):
        continue
    if len(clean.split()) <= 1:
        continue
    if clean.endswith(':'):
        continue
    project_lines.append(clean)

trimmed = []
for line in project_lines:
    if re.search(r'Capital Improvement Projects \(Construction\)', line, re.IGNORECASE):
        break
    trimmed.append(line)

seen = set()
design_projects = []
for name in trimmed:
    if name not in seen:
        seen.add(name)
        design_projects.append(name)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

mask = fund_df['Project_Name'].isin(design_projects) & (fund_df['Amount'] > 50000)
count = int(mask.sum())

result = json.dumps({"count_capital_design_over_50000": count})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_JzWsliya6BcFeSIPcWMfADGm': 'file_storage/call_JzWsliya6BcFeSIPcWMfADGm.json', 'var_call_02UigJJP75tL5mXPnfoaubJr': 'file_storage/call_02UigJJP75tL5mXPnfoaubJr.json'}

exec(code, env_args)
