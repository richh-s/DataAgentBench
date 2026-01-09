code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

funding = load_json_maybe(var_call_9VTcyE0rwaemK7cQ94kOlwa6)
docs = load_json_maybe(var_call_qSNM8svbdwVUOUeF2YIBUzBK)

# Build dict: project -> total funding (int)
funding_map = {r['Project_Name']: int(r['total_amount']) for r in funding if r.get('Project_Name') is not None}

# Extract disaster projects and their start date string from docs.
# Heuristic parsing based on known agenda report structure.
project_info = {}  # name -> {'type':..., 'st':...}

current_section = None
current_type = None

# patterns
bullet_proj = re.compile(r'^\s*([A-Za-z0-9].{2,120}?)\s*$')
psched = re.compile(r'Project Schedule', re.I)
starts = re.compile(r'^(?:Start|Begin)\s*(?:Construction|Design)?\s*:\s*(.+?)\s*$', re.I)
# also accept formats like 'Estimated Schedule:' then 'Complete Design' etc; start we take earliest Begin/Start

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        # section headers
        if re.search(r'Disaster Recovery Projects', ln, re.I):
            current_type = 'disaster'
        elif re.search(r'Capital Improvement Projects', ln, re.I):
            # don't override disaster unless explicitly in capital section
            current_type = 'capital'

        # project names: appear as standalone lines, often Title Case and not too long
        # We'll consider a line a project name if it exists in funding_map exactly.
        if ln in funding_map:
            # initialize
            project_info.setdefault(ln, {'type': current_type, 'st': None})
            # scan next ~25 lines for first begin/start occurrence
            st_val = None
            for j in range(i+1, min(i+26, len(lines))):
                m = starts.match(lines[j])
                if m:
                    st_val = m.group(1).strip()
                    break
            if st_val and not project_info[ln]['st']:
                project_info[ln]['st'] = st_val
            # type update if unknown
            if not project_info[ln].get('type'):
                project_info[ln]['type'] = current_type

# Filter: disaster-related AND started in 2022 (st contains '2022')
selected = []
for name, info in project_info.items():
    if (info.get('type') == 'disaster') and info.get('st') and ('2022' in info['st']):
        selected.append(name)

total = sum(funding_map.get(n, 0) for n in selected)

out = {
    'total_funding_usd': total,
    'matched_disaster_projects_started_2022_count': len(selected),
    'matched_disaster_projects_started_2022': sorted(selected)[:50]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9VTcyE0rwaemK7cQ94kOlwa6': 'file_storage/call_9VTcyE0rwaemK7cQ94kOlwa6.json', 'var_call_qSNM8svbdwVUOUeF2YIBUzBK': 'file_storage/call_qSNM8svbdwVUOUeF2YIBUzBK.json'}

exec(code, env_args)
