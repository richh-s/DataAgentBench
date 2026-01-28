code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
with open(var_call_GxEalvXZPzagBe29dC0xKvGc, 'r') as f:
    civic_docs = json.load(f)

# Patterns to heuristically extract project names and start dates
text_all = '\n'.join(d.get('text','') for d in civic_docs)

# Very rough heuristic: lines that look like project names followed by schedule with Begin Construction or similar containing a date-like token
projects = {}
for line in text_all.split('\n'):
    s = line.strip()
    if not s:
        continue
    # Capture lines that look like a project name (title case and contain keywords or are longish)
    if any(k in s for k in ['Project','Improvements','Repairs','Park','Road','Canyon','Median','Storm','Drain','Bridge','Water','Warning','Traffic','Playground','Facility']) and len(s.split())<=10 and not s.startswith('('):
        current = s
        projects.setdefault(current, {})

# Second pass: find explicit "Begin Construction" or similar with a season/year
current = None
for line in text_all.split('\n'):
    s = line.strip()
    if not s:
        continue
    if s in projects:
        current = s
        continue
    if current is None:
        continue
    m = re.search(r'(Begin Construction|Start|Project Start)[^0-9A-Za-z]*(Spring|Summer|Fall|Winter)?\s*(20\d{2})', s, re.IGNORECASE)
    if m:
        season = m.group(2)
        year = m.group(3)
        st = f"{year}-{season.capitalize()}" if season else year
        projects[current]['st'] = st

# Filter for Spring 2022
spring22_projects = {name:info for name,info in projects.items() if info.get('st','').lower()=='2022-spring'}

result = json.dumps(spring22_projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_GxEalvXZPzagBe29dC0xKvGc': 'file_storage/call_GxEalvXZPzagBe29dC0xKvGc.json', 'var_call_behDCFMEGiCwqDjyeiWcU1hp': 'file_storage/call_behDCFMEGiCwqDjyeiWcU1hp.json'}

exec(code, env_args)
