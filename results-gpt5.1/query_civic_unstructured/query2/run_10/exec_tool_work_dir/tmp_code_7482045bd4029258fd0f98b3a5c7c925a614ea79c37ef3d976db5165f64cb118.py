code = """import re, json
from pathlib import Path

# Load full civic docs
path = Path(var_call_iZw1B0Bk5lx7C7yxPGBP7lD4)
import pandas as pd
civic = pd.read_json(path)
texts = "\n".join(civic['text'].tolist())

# Very rough project extraction: split on double newlines where a line looks like a title (no colon, reasonably short)
projects = []
for block in texts.split('\n\n'):
    line = block.strip().split('\n')[0].strip()
    if 3 < len(line) < 120 and ':' not in line and any(ch.isalpha() for ch in line):
        projects.append(line)

projects = list(dict.fromkeys(projects))

# Identify park-related projects completed in 2022 by scanning the raw text for 'Construction was completed, ... 2022'
completed_2022 = set()
pattern = re.compile(r"(.*?)(?:\n|\r).*?Construction was completed,? (?:[A-Za-z]+ )?2022", re.DOTALL)
for match in pattern.finditer(texts):
    context = match.group(0)
    # backtrack a bit to find nearest preceding line that matches a project title
    lines = context.split('\n')
    title = None
    for l in lines[::-1]:
        s = l.strip()
        if s in projects:
            title = s
            break
    if title:
        completed_2022.add(title)

# Also handle phrasing 'Construction was completed November 2022' as seen in preview
pattern2 = re.compile(r"([A-Za-z0-9 &/]+)\n\(cid:190\) Updates: Construction was completed November 2022", re.MULTILINE)
for m in pattern2.finditer(texts):
    completed_2022.add(m.group(1).strip())

# Filter to park-related by keyword 'park' in name (case-insensitive)
park_completed_2022 = [p for p in completed_2022 if 'park' in p.lower()]

# Load funding table
funding_path = Path(var_call_9F3AQCQ5HAoutsPNr1qU0laf)
fund = pd.read_json(funding_path)

# Join by Project_Name
mask = fund['Project_Name'].isin(park_completed_2022)
matched = fund[mask]

total_funding = int(matched['Amount'].astype(int).sum())

result = {
  'park_completed_2022_projects': park_completed_2022,
  'matched_funding_records': matched.to_dict(orient='records'),
  'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iZw1B0Bk5lx7C7yxPGBP7lD4': 'file_storage/call_iZw1B0Bk5lx7C7yxPGBP7lD4.json', 'var_call_9F3AQCQ5HAoutsPNr1qU0laf': 'file_storage/call_9F3AQCQ5HAoutsPNr1qU0laf.json'}

exec(code, env_args)
