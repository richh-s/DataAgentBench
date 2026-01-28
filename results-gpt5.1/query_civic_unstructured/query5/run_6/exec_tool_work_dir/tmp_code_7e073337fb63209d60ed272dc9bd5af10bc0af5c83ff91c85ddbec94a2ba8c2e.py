code = """import re, json
from pathlib import Path

# Load full civic docs
path = Path(var_call_VYRpnwOZvKmQYUkpdaLPYU5v)
import pandas as pd
civic_docs = pd.read_json(path)
text = " ".join(civic_docs['text'].tolist())

# Roughly identify project blocks mentioning disaster/FEMA/CalOES etc
blocks = re.split(r"\n\s*\n", text)

projects_2022 = set()
for b in blocks:
    if not re.search(r"(FEMA|CalOES|CalJPIA|disaster|Woolsey)", b, re.I):
        continue
    if not re.search(r"2022", b):
        continue
    # heuristic: project name is first line containing 'Project'
    for line in b.split("\n"):
        line = line.strip(" \t:-\u2022")
        if not line:
            continue
        if re.search(r"project", line, re.I):
            # avoid generic headings
            if re.search(r"Status|Report|Projects", line, re.I):
                continue
            projects_2022.add(line)
            break

# Also capture explicitly known disaster-style names from entire text if 2022 appears near them
candidates = set(re.findall(r"([A-Z0-9][A-Za-z0-9&.,'()\-/ ]+?(?:Project|Repairs|Improvements|Sirens))", text))
for c in candidates:
    # look for '2022' within 100 chars of candidate
    for m in re.finditer(re.escape(c), text):
        window = text[m.start()-100:m.end()+100]
        if '2022' in window and re.search(r"(FEMA|CalOES|CalJPIA|disaster|Woolsey)", window, re.I):
            projects_2022.add(c.strip())
            break

# Load funding table
funding = pd.read_json(var_call_r3Ly2AjNpSxyqTHu71BdX0W6)
# disaster-related projects in funding table: those with FEMA/CalOES/CalJPIA in name
funding['is_disaster'] = funding['Project_Name'].str.contains(r"FEMA|CalOES|CalJPIA", case=False, regex=True)

# For 2022 start, we'll approximate by names that also appear in projects_2022 set (string match)
mask_2022 = funding['Project_Name'].isin(projects_2022)

# Disaster-related and started in 2022
subset = funding[funding['is_disaster'] & mask_2022]

# If heuristic finds none, fall back to assuming all disaster projects with '2022' in name (e.g., year prefix)
if subset.empty:
    mask_2022b = funding['Project_Name'].str.contains('2022', regex=False)
    subset = funding[funding['is_disaster'] & mask_2022b]

# Sum Amount
subset['Amount'] = subset['Amount'].astype(int)
 total_amount = int(subset['Amount'].sum())

result = {"projects_identified": subset[['Project_Name','Amount']].to_dict(orient='records'), "total_funding": total_amount}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VYRpnwOZvKmQYUkpdaLPYU5v': 'file_storage/call_VYRpnwOZvKmQYUkpdaLPYU5v.json', 'var_call_r3Ly2AjNpSxyqTHu71BdX0W6': 'file_storage/call_r3Ly2AjNpSxyqTHu71BdX0W6.json'}

exec(code, env_args)
