code = """import re, json
from collections import defaultdict

# Load full funding results
import os, json as js
path = var_call_QHm9Jdy7J43OcbXh6ZBhTBPg
with open(path, 'r') as f:
    funding = js.load(f)

# Load civic docs (preview likely enough)
civic_docs = var_call_D7K2I059rWyFQC0YlV1sPyR7

text = " ".join(doc['text'] for doc in civic_docs)

# Heuristic: extract project names under 'Capital Improvement Projects (Design)' section
sections = re.split(r"Capital Improvement Projects \(Design\)", text, flags=re.I)
if len(sections) < 2:
    design_projects = []
else:
    design_text = sections[1]
    # stop before next major header
    design_text = re.split(r"Capital Improvement Projects \(|Capital Improvement Projects \-|Capital Improvement Projects ", design_text, 1, flags=re.I)[0]
    # project names look like title-case lines separated by double newlines
    candidates = re.split(r"\n\n+", design_text)
    design_projects = []
    for c in candidates:
        line = c.strip().split("\n")[0].strip()
        if len(line.split()) <= 1:
            continue
        if any(k in line.lower() for k in ["updates", "project schedule", "estimated schedule", "project description"]):
            continue
        # simple heuristic: starts with capital letter
        if re.match(r"[A-Z][A-Za-z0-9&\- ]+", line):
            design_projects.append(line)

# Clean duplicates
design_projects = sorted(set(design_projects))

# Mark which are capital: assume all in this section are capital type
capital_design_projects = set(design_projects)

# Join with funding where Amount > 50000
names_funding_gt_50k = {row['Project_Name'] for row in funding if int(row['Amount']) > 50000}

count = 0
for name in names_funding_gt_50k:
    # match by simple normalization
    n_norm = name.lower().replace(" project", "").strip()
    for dp in capital_design_projects:
        dp_norm = dp.lower().replace(" project", "").strip()
        if n_norm == dp_norm:
            count += 1
            break

result = count

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QHm9Jdy7J43OcbXh6ZBhTBPg': 'file_storage/call_QHm9Jdy7J43OcbXh6ZBhTBPg.json', 'var_call_D7K2I059rWyFQC0YlV1sPyR7': 'file_storage/call_D7K2I059rWyFQC0YlV1sPyR7.json'}

exec(code, env_args)
