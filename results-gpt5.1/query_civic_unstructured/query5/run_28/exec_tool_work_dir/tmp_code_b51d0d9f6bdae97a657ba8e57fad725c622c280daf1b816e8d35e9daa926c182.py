code = """import re, json
from datetime import datetime

# Load full civic docs result
path = var_call_V9VpPsKeyaVvQcn99ZYespgK
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(d.get('text','') for d in civic_docs)

# Heuristic: extract project lines and infer start year 2022 if '2022' appears near the project name or in a date tag
project_pattern = re.compile(r"\n([A-Z0-9][A-Za-z0-9 &/().'-]+?(?:Project|Improvements|Repairs|Repair|Study|Plan|Facility|Walkway|Park|Sirens|Signs|Shade Structure|Playground)[^\n]*)")
projects = set(m.group(1).strip() for m in project_pattern.finditer(texts))

# Find sentences mentioning 2022 and disaster markers near project names
disaster_markers = re.compile(r"FEMA|CalOES|CalJPIA|disaster|fire|emergency", re.I)

project_info = {}
for line in texts.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    for p in projects:
        if p in line_stripped:
            info = project_info.setdefault(p, {"type": None, "years": set()})
            if disaster_markers.search(line_stripped):
                info["type"] = "disaster"
            # look for 4-digit years
            for y in re.findall(r"20[0-3][0-9]", line_stripped):
                info["years"].add(y)

# Keep only disaster projects with year 2022
disaster_2022_projects = [p for p,info in project_info.items() if info["type"]=="disaster" and "2022" in info["years"]]

result = {"disaster_2022_projects": disaster_2022_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V9VpPsKeyaVvQcn99ZYespgK': 'file_storage/call_V9VpPsKeyaVvQcn99ZYespgK.json', 'var_call_mt4J9hnS0vIxt1eRwIpOu1DK': 'file_storage/call_mt4J9hnS0vIxt1eRwIpOu1DK.json'}

exec(code, env_args)
