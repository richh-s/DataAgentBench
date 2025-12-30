code = """import re, json
from pathlib import Path

# Load full civic docs result
path = Path(var_call_5XwreXzQ8T5rTtgPIvpJ8I98)
with path.open() as f:
    civic_docs = json.load(f)

texts = ' '.join(d['text'] for d in civic_docs)

# Heuristic: project lines often start at line starts; grab names and any year-ish token
projects = []
for line in texts.splitlines():
    line = line.strip()
    if not line:
        continue
    # consider it a project name if it has 'Project' or looks like a titled phrase
    if 'Project' in line or 'Repairs' in line or 'Improvements' in line or 'Drain' in line:
        projects.append(line)

# deduplicate
projects = sorted(set(projects))

# Identify disaster projects by FEMA/CalOES etc and get those with 2022 in same or nearby lines
# For simplicity we just collect all project names; later we'll filter by names that are clearly disaster (with FEMA/CalOES etc.) and started in 2022 via substring "2022" in the same line

result = projects[:200]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5XwreXzQ8T5rTtgPIvpJ8I98': 'file_storage/call_5XwreXzQ8T5rTtgPIvpJ8I98.json', 'var_call_t6IViIpzntd5669hbmH4n6Mb': 'file_storage/call_t6IViIpzntd5669hbmH4n6Mb.json'}

exec(code, env_args)
