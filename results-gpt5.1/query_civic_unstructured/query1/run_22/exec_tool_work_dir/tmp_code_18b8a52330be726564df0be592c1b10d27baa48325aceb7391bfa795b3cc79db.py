code = """import re, json, pandas as pd
from pathlib import Path
import os

funding_records = var_call_UR62iUkHicKuDhpMCSumwD7W

civic_docs_data = var_call_VGjJzCi9VF0pdnKCbRVgGbwZ
if isinstance(civic_docs_data, str) and os.path.isfile(civic_docs_data):
    import json as _json
    with open(civic_docs_data, 'r') as f:
        civic_docs = _json.load(f)
else:
    civic_docs = civic_docs_data

texts = [d["text"] for d in civic_docs]
full_text = "\n".join(texts)

sections = re.split(r"Capital Improvement Projects \(Design\)", full_text, flags=re.IGNORECASE)
projects_design = {}
if len(sections) > 1:
    design_text = sections[1]
    design_text = re.split(r"Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)", design_text, flags=re.IGNORECASE)[0]
    lines = [l.strip() for l in design_text.split("\n")]
    for i, line in enumerate(lines):
        if not line:
            continue
        if "updates" in line.lower() or "schedule" in line.lower() or "estimated" in line.lower():
            continue
        if re.search(r"[A-Za-z]", line) and not line.endswith(":"):
            prev_blank = (i == 0) or (not lines[i-1])
            if prev_blank:
                name = line.strip()
                projects_design[name] = True

fund_df = pd.DataFrame(funding_records)
fund_df["Amount"] = pd.to_numeric(fund_df["Amount"])
fund_df = fund_df[fund_df["Amount"] > 50000]

fund_df["key"] = fund_df["Project_Name"].str.lower().str.strip()
proj_keys = {p.lower().strip() for p in projects_design.keys()}

direct = fund_df[fund_df["key"].isin(proj_keys)]

matches = set(direct["key"])
for pk in proj_keys:
    for fk in fund_df["key"]:
        if pk and pk in fk:
            matches.add(fk)

result_count = fund_df[fund_df["key"].isin(matches)].shape[0]

print("__RESULT__:")
print(json.dumps(int(result_count)))"""

env_args = {'var_call_UR62iUkHicKuDhpMCSumwD7W': 'file_storage/call_UR62iUkHicKuDhpMCSumwD7W.json', 'var_call_VGjJzCi9VF0pdnKCbRVgGbwZ': 'file_storage/call_VGjJzCi9VF0pdnKCbRVgGbwZ.json'}

exec(code, env_args)
