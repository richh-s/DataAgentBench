code = """import json, re
import pandas as pd

# Load full UC-assigned publications (rows)
path = var_call_j55SyTVQyBw0aAybXsyxCaAM
with open(path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

# Helper: extract publication number from Patents_info
pub_re = re.compile(r"pub\. number\s+([A-Z]{2,}-[0-9A-Z]+(?:-[A-Z][0-9])?)", re.I)

def extract_pub(patents_info: str):
    if not patents_info:
        return None
    m = pub_re.search(patents_info)
    return m.group(1) if m else None

uc_pubs = set()
for r in uc_rows:
    p = extract_pub(r.get('Patents_info',''))
    if p:
        uc_pubs.add(p)

# Also include granted/published numbers possibly elsewhere in Patents_info (fallback)
# capture patterns like US-11421276-B2 etc
fallback_re = re.compile(r"\b([A-Z]{2,}-\d{7,}-[A-Z]\d)\b")
for r in uc_rows:
    txt = r.get('Patents_info','') or ''
    for m in fallback_re.findall(txt):
        uc_pubs.add(m)

# Get all publications to find citing patents: those whose citation list contains any UC pub
# SQLite JSON parsing not available; fetch candidates where citation contains 'US-' etc and 'citation' not empty
# We'll just pull all non-empty citations to Python and match.

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs)}))"""

env_args = {'var_call_RXZxPa6ek2GtXCBDhmGKF66H': ['publicationinfo'], 'var_call_xRaFlt6HbwpuEGgcKr0x8ZXF': ['cpc_definition'], 'var_call_j55SyTVQyBw0aAybXsyxCaAM': 'file_storage/call_j55SyTVQyBw0aAybXsyxCaAM.json'}

exec(code, env_args)
