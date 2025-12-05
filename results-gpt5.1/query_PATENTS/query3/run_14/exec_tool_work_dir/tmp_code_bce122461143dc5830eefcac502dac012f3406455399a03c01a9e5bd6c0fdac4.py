code = """import json, re, pandas as pd
from collections import defaultdict

# Load full result from file
file_path = var_call_Jh5KNvY67mu9gxG4b9laG9If
with open(file_path, 'r') as f:
    data = json.load(f)

# Helper to extract assignee
def extract_assignee(patents_info):
    m = re.search(r'assignee_harmonized: ([^,\.]+)', patents_info)
    if m:
        return m.group(1).strip()
    # fallback: try "owned by X" or "assigned to X" patterns
    m = re.search(r'owned by ([^,\.]+)', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'assigned to ([^,\.]+)', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'holds the .* filing .* by ([^,\.]+)', patents_info)
    if m:
        return m.group(1).strip()
    return None

# Build a map from cited publication_number to list of citing assignees (excluding UNIV CALIFORNIA)
cited_to_assignees = defaultdict(set)
for rec in data:
    pi = rec.get('Patents_info','')
    assignee = extract_assignee(pi)
    if not assignee or assignee.upper().startswith('UNIV CALIFORNIA'):
        continue
    cit_raw = rec.get('citation') or '[]'
    try:
        cits = json.loads(cit_raw)
    except Exception:
        continue
    for c in cits:
        pub = c.get('publication_number')
        if pub:
            cited_to_assignees[pub].add(assignee)

# Now we need to know which of these cited publication_numbers are UNIV CALIFORNIA patents.
# We'll later query DB by searching Patents_info containing each pub number and UNIV CALIFORNIA.

cited_uc_pubs = sorted(cited_to_assignees.keys())

result = {
    'cited_publication_numbers': cited_uc_pubs[:200],  # limit to first 200 to keep query manageable
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GRSPqzPoejP7mZpN69U3Mk4P': [], 'var_call_Jh5KNvY67mu9gxG4b9laG9If': 'file_storage/call_Jh5KNvY67mu9gxG4b9laG9If.json'}

exec(code, env_args)
