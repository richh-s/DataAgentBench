code = """import json, re
with open(var_call_uAbbEpB6ZBwfzaiEz02vBDm9, 'r', encoding='utf-8') as f:
    data = json.load(f)

assignee_to_codes = {}
all_codes = set()

patterns = [
    r'belonging to ([^.,;]+?)(?: and | which | that |,|\.|$)',
    r'is belonging to ([^.,;]+?)(?: and | which | that |,|\.|$)',
    r'belongs to ([^.,;]+?)(?: and | which | that |,|\.|$)',
    r'assigned to ([^.,;]+?)(?: and | which | that |,|\.|$)',
    r'is assigned to ([^.,;]+?)(?: and | which | that |,|\.|$)'
]

for rec in data:
    pinfo = rec.get('Patents_info') or ''
    assignee = None
    for pat in patterns:
        m = re.search(pat, pinfo, flags=re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
            break
    if assignee:
        assignee = assignee.rstrip('.')
        assignee = assignee.strip()
    else:
        m = re.search(r'([A-Z][A-Z0-9 &\-]{2,}(?: [A-Z][A-Z0-9 &\-]{2,})*)', pinfo)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        assignee = 'UNKNOWN'

    cpc_field = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpcs = []
    primary_code = None
    if isinstance(cpcs, list):
        for entry in cpcs:
            if isinstance(entry, dict) and entry.get('first'):
                primary_code = entry.get('code')
                break
        if not primary_code:
            for entry in cpcs:
                if isinstance(entry, dict) and entry.get('inventive'):
                    primary_code = entry.get('code'); break
        if not primary_code and len(cpcs)>0 and isinstance(cpcs[0], dict):
            primary_code = cpcs[0].get('code')
    if primary_code:
        all_codes.add(primary_code)
        assignee_to_codes.setdefault(assignee, set()).add(primary_code)

assignee_to_codes = {k: sorted(list(v)) for k,v in assignee_to_codes.items()}
all_codes = sorted(list(all_codes))
output = {'assignee_to_codes': assignee_to_codes, 'codes': all_codes}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_uAbbEpB6ZBwfzaiEz02vBDm9': 'file_storage/call_uAbbEpB6ZBwfzaiEz02vBDm9.json'}

exec(code, env_args)
