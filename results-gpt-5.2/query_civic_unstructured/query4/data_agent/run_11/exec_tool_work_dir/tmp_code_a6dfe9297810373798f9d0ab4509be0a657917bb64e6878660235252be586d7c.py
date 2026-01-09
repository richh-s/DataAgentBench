code = """import json, re
from pathlib import Path

path = Path(var_call_DQLKJrtf3yYi1VEkTJZXOohY)
docs = json.loads(path.read_text())

spring22 = []
begin_pat = re.compile(r"Begin Construction\s*:\s*([^\n\r]+)", re.IGNORECASE)

skip = {
    'Capital Improvement Projects (Design)','Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)',
    'Disaster Recovery Projects (Design)','Disaster Recovery Projects (Construction)','Disaster Recovery Projects (Not Started)',
    'DISCUSSION:','RECOMMENDED ACTION:','Subject:','Project Schedule:','Estimated Schedule:','Project Description:','Project Updates:'
}

for d in docs:
    lines = d.get('text','').splitlines()
    current_proj = None
    for i, line in enumerate(lines):
        l = line.strip()
        if not l:
            continue
        if l in skip:
            continue
        if l.startswith('Page ') or l.startswith('Agenda Item') or l.startswith('Prepared by') or l.startswith('Approved by'):
            continue
        # detect project header by next line containing 'Updates' or 'Project Description'
        nxt = lines[i+1].strip() if i+1 < len(lines) else ''
        if 'Updates' in nxt or 'Project Description' in nxt:
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
