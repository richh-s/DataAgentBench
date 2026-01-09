code = """import json, re
import pandas as pd

# Load publication records for UNIV CALIFORNIA assignee
path = var_call_59lcvJsIjZ1vcLpPvQ8cFHob
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def extract_pubnum(info):
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', info)
    if m:
        return m.group(1)
    m = re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', info)
    if m:
        return m.group(1)
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*)\b', info)
    if m:
        return m.group(1)
    return None

def normalize_pubnum(p):
    if not p:
        return None
    p = p.strip()
    return p

uc_pubnums = []
for r in recs:
    p = extract_pubnum(r.get('Patents_info','') or '')
    p = normalize_pubnum(p)
    if p:
        uc_pubnums.append(p)

uc_pubnums = sorted(set(uc_pubnums))

# Pull all patents (potential citing patents) that cite any of these UC pubnums
# We'll scan all rows' citation JSON and match publication_number against uc_pubnums

# Get all rows with non-empty citation
# (can't query JSON in SQLite easily; instead, we fetch columns for rows where citation not empty)

print('__RESULT__:')
print(json.dumps({'uc_pubnums_count': len(uc_pubnums), 'uc_pubnums_sample': uc_pubnums[:20]}))"""

env_args = {'var_call_iHXHysJC3duFCWWnJW64v10h': ['publicationinfo'], 'var_call_jlHGhsPdB6yLdpu78t6zwQ84': ['cpc_definition'], 'var_call_59lcvJsIjZ1vcLpPvQ8cFHob': 'file_storage/call_59lcvJsIjZ1vcLpPvQ8cFHob.json'}

exec(code, env_args)
