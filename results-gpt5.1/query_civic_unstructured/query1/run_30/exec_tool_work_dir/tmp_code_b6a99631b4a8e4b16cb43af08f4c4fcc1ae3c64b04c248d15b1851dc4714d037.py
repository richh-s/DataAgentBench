code = """import re, json, pandas as pd

# Load funding data
funding = var_call_zwHFFIQM0e7Toet188ASgghM

# Load civic docs (may be path or list)
import os, builtins
civic_raw = var_call_tIzAtB6dvfaFzpdbsfLhXHsl
if isinstance(civic_raw, str) and os.path.exists(civic_raw):
    import json as _json
    with open(civic_raw, 'r') as f:
        civic_docs = _json.load(f)
else:
    civic_docs = civic_raw

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Very simple heuristic: list of known capital design projects from the text header 'Capital Improvement Projects (Design)'
section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|$)', full_text, re.S)
projects_design = []
if section_match:
    section = section_match.group(1)
    # project lines are those that are not empty and not starting with bullets/parentheses
    for line in section.split('\n'):
        line = line.strip('\r ')
        if not line:
            continue
        if line.startswith('(cid:') or line.startswith('Updates') or line.startswith('Project Schedule') or line.startswith('Estimated Schedule'):
            continue
        # Skip obvious non-project descriptors
        if 'Updates' in line or 'Schedule' in line or 'Project Description' in line:
            continue
        # Filter to Lines in Title Case (rough heuristic)
        if re.search(r'[a-z]', line) and re.search(r'[A-Z]', line):
            projects_design.append(line)

projects_design = list(dict.fromkeys(projects_design))

# Build DataFrame of funding
fund_df = pd.DataFrame(funding)

# Normalize names for join
def norm(name):
    return re.sub(r'[^a-z0-9]+', ' ', name.lower()).strip()

fund_df['norm'] = fund_df['Project_Name'].apply(norm)

design_norm = [norm(p) for p in projects_design]

# Find funding entries whose normalized name matches any design project name (allow subset match both ways)
matched_projects = set()
for pn, nn in zip(projects_design, design_norm):
    for _, row in fund_df.iterrows():
        fn = row['norm']
        if nn == fn or nn in fn or fn in nn:
            matched_projects.add(row['Project_Name'])

# count unique matched projects with amount>50000 (already filtered by SQL) and assume type 'capital' since section says Capital Improvement
count = len(matched_projects)

import json as json_mod
result = json_mod.dumps({"count_capital_design_over_50000": int(count)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zwHFFIQM0e7Toet188ASgghM': 'file_storage/call_zwHFFIQM0e7Toet188ASgghM.json', 'var_call_tIzAtB6dvfaFzpdbsfLhXHsl': 'file_storage/call_tIzAtB6dvfaFzpdbsfLhXHsl.json'}

exec(code, env_args)
