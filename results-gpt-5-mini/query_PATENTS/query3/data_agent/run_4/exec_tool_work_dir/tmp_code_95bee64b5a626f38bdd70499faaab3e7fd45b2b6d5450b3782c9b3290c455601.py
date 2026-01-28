code = """import json, re
# load the query result from storage
with open(var_call_uAbbEpB6ZBwfzaiEz02vBDm9, 'r', encoding='utf-8') as f:
    data = json.load(f)

assignee_to_codes = {}
all_codes = set()

# heuristics to extract assignee from Patents_info
patterns = [
    r'belonging to ([^.,;\n]+?)(?: and | which | that |,|\.|$)',
    r'is belonging to ([^.,;\n]+?)(?: and | which | that |,|\.|$)',
    r'belongs to ([^.,;\n]+?)(?: and | which | that |,|\.|$)',
    r'assigned to ([^.,;\n]+?)(?: and | which | that |,|\.|$)',
    r'is assigned to ([^.,;\n]+?)(?: and | which | that |,|\.|$)'
]

for rec in data:
    pinfo = rec.get('Patents_info') or ''
    assignee = None
    for pat in patterns:
        m = re.search(pat, pinfo, flags=re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
            break
    # cleanup common trailing words
    if assignee:
        assignee = assignee.rstrip('.')
        assignee = assignee.strip()
    else:
        # fallback: look for uppercase sequences of words
        m = re.search(r'([A-Z][A-Z0-9 &\-]{2,}(?: [A-Z][A-Z0-9 &\-]{2,})*)', pinfo)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        assignee = 'UNKNOWN'

    # parse cpc JSON-like
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try to fix single quotes
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
        if not primary_code and len(cpcs)>0:
            # fallback: take first dict with 'inventive' True
            for entry in cpcs:
                if isinstance(entry, dict) and entry.get('inventive'):
                    primary_code = entry.get('code'); break
        if not primary_code and len(cpcs)>0 and isinstance(cpcs[0], dict):
            primary_code = cpcs[0].get('code')
    if primary_code:
        all_codes.add(primary_code)
        assignee_to_codes.setdefault(assignee, set()).add(primary_code)

# convert sets to lists
assignee_to_codes = {k: sorted(list(v)) for k,v in assignee_to_codes.items()}
all_codes = sorted(list(all_codes))

output = {'assignee_to_codes': assignee_to_codes, 'codes': all_codes}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_uAbbEpB6ZBwfzaiEz02vBDm9': 'file_storage/call_uAbbEpB6ZBwfzaiEz02vBDm9.json'}

exec(code, env_args)
