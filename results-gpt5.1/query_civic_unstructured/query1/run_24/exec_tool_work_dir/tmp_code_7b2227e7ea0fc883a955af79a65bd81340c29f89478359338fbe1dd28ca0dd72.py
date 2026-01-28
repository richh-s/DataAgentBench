code = """import re, json, os
from collections import defaultdict

import json as js

path = var_call_QHm9Jdy7J43OcbXh6ZBhTBPg
with open(path, 'r') as f:
    funding = js.load(f)

civic_docs = var_call_D7K2I059rWyFQC0YlV1sPyR7

text = " ".join(doc['text'] for doc in civic_docs)

sections = re.split(r"Capital Improvement Projects \(Design\)", text, flags=re.I)
if len(sections) < 2:
    design_projects = []
else:
    design_text = sections[1]
    design_text = re.split(r"Capital Improvement Projects \(|Capital Improvement Projects \-|Capital Improvement Projects ", design_text, 1, flags=re.I)[0]
    candidates = re.split(r"\n\n+", design_text)
    design_projects = []
    for c in candidates:
        first_line = c.strip().split("\n")[0].strip()
        line = first_line
        if len(line.split()) <= 1:
            continue
        low = line.lower()
        if ("updates" in low) or ("project schedule" in low) or ("estimated schedule" in low) or ("project description" in low):
            continue
        if re.match(r"[A-Z][A-Za-z0-9&\- ]+", line):
            design_projects.append(line)

design_projects = sorted(set(design_projects))
capital_design_projects = set(design_projects)

names_funding_gt_50k = {row['Project_Name'] for row in funding if int(row['Amount']) > 50000}

count = 0
for name in names_funding_gt_50k:
    n_norm = name.lower().replace(" project", "").strip()
    for dp in capital_design_projects:
        dp_norm = dp.lower().replace(" project", "").strip()
        if n_norm == dp_norm:
            count += 1
            break

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_QHm9Jdy7J43OcbXh6ZBhTBPg': 'file_storage/call_QHm9Jdy7J43OcbXh6ZBhTBPg.json', 'var_call_D7K2I059rWyFQC0YlV1sPyR7': 'file_storage/call_D7K2I059rWyFQC0YlV1sPyR7.json'}

exec(code, env_args)
