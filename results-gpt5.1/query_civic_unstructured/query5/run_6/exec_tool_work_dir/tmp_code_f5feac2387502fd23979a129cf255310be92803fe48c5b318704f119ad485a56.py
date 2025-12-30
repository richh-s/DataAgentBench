code = """import re, json
from pathlib import Path
import pandas as pd

# Load full civic docs
path = Path(var_call_VYRpnwOZvKmQYUkpdaLPYU5v)
civic_docs = pd.read_json(path)
text = " ".join(civic_docs['text'].tolist())

# Split into blocks
blocks = re.split(r"\n\s*\n", text)

projects_2022 = set()
for b in blocks:
    if not re.search(r"(FEMA|CalOES|CalJPIA|disaster|Woolsey)", b, re.I):
        continue
    if "2022" not in b:
        continue
    for line in b.split("\n"):
        line = line.strip(" \t:-")
        if not line:
            continue
        if re.search(r"project", line, re.I):
            if re.search(r"Status|Report|Projects", line, re.I):
                continue
            projects_2022.add(line)
            break

# Load funding table
funding = pd.read_json(var_call_r3Ly2AjNpSxyqTHu71BdX0W6)
funding['is_disaster'] = funding['Project_Name'].str.contains(r"FEMA|CalOES|CalJPIA", case=False, regex=True)

mask_2022 = funding['Project_Name'].isin(projects_2022)
subset = funding[funding['is_disaster'] & mask_2022]

if subset.empty:
    mask_2022b = funding['Project_Name'].str.contains('2022', regex=False)
    subset = funding[funding['is_disaster'] & mask_2022b]

subset = subset.copy()
subset['Amount'] = subset['Amount'].astype(int)
 total_amount = int(subset['Amount'].sum())

result = {"projects_identified": subset[['Project_Name','Amount']].to_dict(orient='records'), "total_funding": total_amount}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VYRpnwOZvKmQYUkpdaLPYU5v': 'file_storage/call_VYRpnwOZvKmQYUkpdaLPYU5v.json', 'var_call_r3Ly2AjNpSxyqTHu71BdX0W6': 'file_storage/call_r3Ly2AjNpSxyqTHu71BdX0W6.json'}

exec(code, env_args)
