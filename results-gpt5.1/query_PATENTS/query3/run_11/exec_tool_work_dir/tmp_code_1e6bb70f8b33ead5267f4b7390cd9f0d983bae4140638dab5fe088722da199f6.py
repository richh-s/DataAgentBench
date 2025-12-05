code = """import json, re, pandas as pd
from pathlib import Path

# Load full publication results
path = Path(var_call_akqVR2qjqlf5VBdrnLaZgCIL)
records = json.loads(path.read_text())

assignee_cpc = {}

for rec in records:
    info = rec.get('Patents_info','') or ''
    # extract assignee_harmonized value
    m = re.search(r'assignee_harmonized: ([^;\.]+)', info)
    if not m:
        # fallback: look for 'is belonging to <ASSIGNEE>' pattern
        m2 = re.search(r'is belonging to ([^.;]+)', info)
        if m2:
            assignee = m2.group(1).strip()
        else:
            continue
    else:
        assignee = m.group(1).strip()
    if assignee.upper().startswith('UNIV CALIFORNIA'):
        continue
    # parse CPC JSON-like
    cpc_raw = rec.get('cpc','') or ''
    try:
        cpc_list = json.loads(cpc_raw)
    except Exception:
        continue
    # primary CPC subclass: take first entry's code, strip to subclass (first 4 chars with optional letter/number), often like 'A61P43/00' -> 'A61P'
    if not cpc_list:
        continue
    code = cpc_list[0].get('code','')
    if not code:
        continue
    subclass = re.match(r'^[A-Z]\d{2}[A-Z]', code)
    if subclass:
        subclass = subclass.group(0)
    else:
        subclass = code.split('/')[0]
    assignee_cpc.setdefault(assignee, set()).add(subclass)

# Build list of unique subclass codes
all_subclasses = sorted({c for s in assignee_cpc.values() for c in s})

result = {
    'assignee_to_subclass': {k: sorted(list(v)) for k,v in assignee_cpc.items()},
    'subclasses': all_subclasses
}

import json as _j
out = _j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_akqVR2qjqlf5VBdrnLaZgCIL': 'file_storage/call_akqVR2qjqlf5VBdrnLaZgCIL.json', 'var_call_H0bKrtby3qFTHlcBj91Cn4vt': ['cpc_definition']}

exec(code, env_args)
