code = """import json, re
from collections import defaultdict

# Load full result from file
file_path = var_call_5A7iX4l9wRD6xo0gEe1c6XHC
with open(file_path, 'r') as f:
    citing_records = json.load(f)

# Helper to extract assignee_harmonized and cited assignees from Patents_info and citation
assignee_regex = re.compile(r"assignee_harmonized: ([^;,]+)")

citing_assignees = defaultdict(set)  # assignee -> set of CPC codes

for rec in citing_records:
    info = rec.get('Patents_info','') or ''
    m = assignee_regex.search(info)
    if not m:
        continue
    assignee = m.group(1).strip()
    if assignee.upper() == 'UNIV CALIFORNIA':
        continue
    cit = rec.get('citation','') or ''
    # require that the cited portion mentions UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' not in cit.upper():
        continue
    # collect CPC codes from JSON-like string
    cpc_raw = rec.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_raw)
        codes = [e.get('code') for e in cpc_list if isinstance(e, dict) and e.get('code')]
    except Exception:
        codes = []
    for code in codes:
        # primary subclass: take part up to first space or slash? For CPC, subclass is often first 4 chars like A61K
        primary = re.match(r"^[A-HY]\d\d[A-Z]", code)
        if primary:
            citing_assignees[assignee].add(primary.group(0))

# Prepare list of unique primary CPC symbols
primary_symbols = sorted({sym for syms in citing_assignees.values() for sym in syms})

result = {
    'assignees': {k: sorted(v) for k,v in citing_assignees.items()},
    'primary_symbols': primary_symbols
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mSZkzDvYrC2Q1RnwUu3my1nz': [], 'var_call_5A7iX4l9wRD6xo0gEe1c6XHC': 'file_storage/call_5A7iX4l9wRD6xo0gEe1c6XHC.json'}

exec(code, env_args)
