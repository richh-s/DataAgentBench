code = """import json, re
from pathlib import Path

# Load parsed civic project lines
path = Path(var_call_chJXwKDW12TOXMGIxYqddhsF)
with path.open() as f:
    civic_lines = json.load(f)

# Identify disaster-related project names (with FEMA/CalOES/CalJPIA or clearly disaster) and those that started in 2022
# We only have names, not explicit start dates; use heuristic: names containing '2022 ' or starting with '2022 ' considered 2022-start.

disaster_keywords = ['fema', 'caloes', 'caljpia']

projects_2022_disaster = set()
for line in civic_lines:
    lower = line.lower()
    if not any(k in lower for k in disaster_keywords):
        continue
    # infer 2022 from line text
    if '2022' in line:
        projects_2022_disaster.add(line)

# Also consider explicit "2022 " prefix even without FEMA wording (but then must be disaster via some other mention - but we don't have type info here), so we skip that to avoid mislabeling.

projects_2022_disaster = sorted(projects_2022_disaster)

print('__RESULT__:')
print(json.dumps(projects_2022_disaster))"""

env_args = {'var_call_5XwreXzQ8T5rTtgPIvpJ8I98': 'file_storage/call_5XwreXzQ8T5rTtgPIvpJ8I98.json', 'var_call_t6IViIpzntd5669hbmH4n6Mb': 'file_storage/call_t6IViIpzntd5669hbmH4n6Mb.json', 'var_call_chJXwKDW12TOXMGIxYqddhsF': 'file_storage/call_chJXwKDW12TOXMGIxYqddhsF.json'}

exec(code, env_args)
