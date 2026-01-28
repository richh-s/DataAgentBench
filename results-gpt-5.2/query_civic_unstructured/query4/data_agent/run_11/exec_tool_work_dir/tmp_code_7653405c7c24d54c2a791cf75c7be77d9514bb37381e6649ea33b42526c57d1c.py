code = """import json, re
from pathlib import Path

path = Path(var_call_DQLKJrtf3yYi1VEkTJZXOohY)
docs = json.loads(path.read_text())

# Extract project schedule blocks and detect those with Begin Construction: Spring 2022
spring22 = []

# Regex patterns
proj_header = re.compile(r"^(?!\(cid:)([A-Z0-9][^\n]{2,100}?)\s*$")
begin_pat = re.compile(r"Begin Construction\s*:\s*([^\n\r]+)", re.IGNORECASE)

for d in docs:
    lines = d.get('text','').splitlines()
    current_proj = None
    for i, line in enumerate(lines):
        l = line.strip()
        if not l:
            continue
        # project header heuristics: line not too long and not common headings
        if l in {"Capital Improvement Projects (Design)","Capital Improvement Projects (Construction)","Capital Improvement Projects (Not Started)",
                 "Disaster Recovery Projects (Design)","Disaster Recovery Projects (Construction)","Disaster Recovery Projects (Not Started)",
                 "DISCUSSION:","RECOMMENDED ACTION:","Subject:","Project Schedule:","Estimated Schedule:","Project Description:","Project Updates:"}:
            continue
        if l.startswith('Page ') or l.startswith('Agenda Item') or l.startswith('Prepared by') or l.startswith('Approved by'):
            continue
        # detect potential project name: followed soon by bullet "Updates" or "Project Schedule" etc
        if (i+1)<len(lines) and 'Updates' in lines[i+1]:
            current_proj = l
            continue
        if (i+1)<len(lines) and 'Project Description' in lines[i+1]:
            current_proj = l
            continue
        m = begin_pat.search(l)
        if m and current_proj:
            val = m.group(1).strip()
            if re.search(r"\bSpring\s*2022\b", val, re.IGNORECASE):
                spring22.append(current_proj)

spring22_unique = sorted(set(spring22))
print('__RESULT__:')
print(json.dumps({'spring22_projects': spring22_unique, 'count': len(spring22_unique)}))"""

env_args = {'var_call_TpPn0yAmA3vLsADt1sJwRJSb': ['Funding'], 'var_call_357DOrmSTlhzjregOEGXC2P6': ['civic_docs'], 'var_call_DQLKJrtf3yYi1VEkTJZXOohY': 'file_storage/call_DQLKJrtf3yYi1VEkTJZXOohY.json'}

exec(code, env_args)
