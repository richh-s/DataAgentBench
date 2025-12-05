code = """import json, re, pandas as pd
from pathlib import Path

# Load full publication results
path = Path(var_call_z5zUfdbxgREZlBt5y72RDQWv)
rows = json.loads(path.read_text())

records = []
for r in rows:
    info = r.get('Patents_info','') or ''
    cit = r.get('citation','') or ''
    # Extract assignee_harmonized if present
    m = re.search(r"assignee_harmonized: ([^;\\n]+)", info)
    assignee = m.group(1).strip() if m else None
    # Skip if citing assignee is UNIV CALIFORNIA
    if assignee and assignee.upper().strip() == 'UNIV CALIFORNIA':
        continue
    # Approximate: if citation text mentions UNIV CALIFORNIA, treat this as citing UC-assigned patents
    if 'UNIV CALIFORNIA' not in cit.upper():
        continue
    # Parse CPC JSON-like field
    cpc_txt = r.get('cpc') or ''
    try:
        cpc_list = json.loads(cpc_txt)
    except Exception:
        cpc_list = []
    # Get primary (first=true) codes; if none, fall back to all codes
    prim = [e['code'] for e in cpc_list if isinstance(e, dict) and e.get('first')]
    if not prim:
        prim = [e['code'] for e in cpc_list if isinstance(e, dict) and 'code' in e]
    for code in prim:
        # Derive primary subclass symbol: take up to first '/' (main group) or first space
        m2 = re.match(r"([A-Z]\d+[A-Z])", code)
        subclass = None
        if m2:
            subclass = m2.group(1)
        else:
            # fallback: take first 4-5 chars pattern like A61P or C12N
            m3 = re.match(r"([A-Z]\d{2}[A-Z])", code)
            subclass = m3.group(1) if m3 else code[:4]
        records.append({'assignee': assignee or 'UNKNOWN', 'cpc_symbol': subclass})

# Deduplicate
df = pd.DataFrame(records).drop_duplicates()

# Prepare list of unique CPC symbols for lookup
symbols = sorted(df['cpc_symbol'].dropna().unique().tolist())

result = {'assignee_cpc_pairs': df.to_dict(orient='records'), 'symbols': symbols}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_z5zUfdbxgREZlBt5y72RDQWv': 'file_storage/call_z5zUfdbxgREZlBt5y72RDQWv.json', 'var_call_LVSJmsZNtF22Q84diPB8U8aE': ['cpc_definition']}

exec(code, env_args)
