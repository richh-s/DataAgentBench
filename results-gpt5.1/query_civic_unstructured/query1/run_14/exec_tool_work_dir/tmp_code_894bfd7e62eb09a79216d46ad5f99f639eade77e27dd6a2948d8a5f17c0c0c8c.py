code = """import re, json, pandas as pd

# Load funding data
funding_records = var_call_JzWsliya6BcFeSIPcWMfADGm

# Load civic docs (file path if large)
import os, pathlib, json as jsonlib

civic_source = var_call_02UigJJP75tL5mXPnfoaubJr
if isinstance(civic_source, str) and os.path.exists(civic_source):
    with open(civic_source, 'r') as f:
        civic_docs = jsonlib.load(f)
else:
    civic_docs = civic_source

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Extract project sections under "Capital Improvement Projects (Design)" and assume these are status 'design' and type 'capital'

sections = re.split(r"Capital Improvement Projects \(Design\)", full_text, flags=re.IGNORECASE)
if len(sections) > 1:
    design_block = sections[1]
else:
    design_block = ''

# Heuristic: project names are lines that are title-like and not starting with bullets or parentheses
project_lines = []
for line in design_block.split('\n'):
    clean = line.strip()
    if not clean:
        continue
    if clean.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'project description')):
        continue
    if clean.startswith('('):
        continue
    if len(clean.split()) <= 1:
        continue
    # filter out obvious non-project headers
    if clean.endswith(':'):
        continue
    project_lines.append(clean)

# Manually trim based on where design list ends (before 'Capital Improvement Projects (Construction)')
trimmed = []
for line in project_lines:
    if re.search(r'Capital Improvement Projects \(Construction\)', line, re.IGNORECASE):
        break
    trimmed.append(line)

# Deduplicate while preserving order
seen = set()
design_projects = []
for name in trimmed:
    if name not in seen:
        seen.add(name)
        design_projects.append(name)

# From preview we know some of these names; but use whatever we extracted

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Join on Project_Name
mask = fund_df['Project_Name'].isin(design_projects) & (fund_df['Amount'] > 50000)
count = int(mask.sum())

result = json.dumps({"count_capital_design_over_50000": count, "design_projects_matched": design_projects})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_JzWsliya6BcFeSIPcWMfADGm': 'file_storage/call_JzWsliya6BcFeSIPcWMfADGm.json', 'var_call_02UigJJP75tL5mXPnfoaubJr': 'file_storage/call_02UigJJP75tL5mXPnfoaubJr.json'}

exec(code, env_args)
