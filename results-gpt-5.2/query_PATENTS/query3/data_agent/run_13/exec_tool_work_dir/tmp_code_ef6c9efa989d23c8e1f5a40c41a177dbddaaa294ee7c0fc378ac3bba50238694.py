code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

uc_rows = load_records(var_call_podeueb7ZgQ1Fvj9LRgBnJmT)
cpc_defs = load_records(var_call_tnXJkoGwQIL9QloKmbYghE1p)

def extract_pub_number(patents_info:str):
    if not patents_info:
        return None
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', patents_info)
    if m:
        return m.group(1)
    return None

def extract_assignee(patents_info:str):
    if not patents_info:
        return None
    # capture between 'owned by'/'assigned to' and 'and has'
    m = re.search(r'(?:owned by|assigned to)\s+(.+?)\s+and has', patents_info)
    if m:
        return m.group(1).strip().strip('.')
    m = re.search(r'^\s*([^,]+?)\s+holds\s+the', patents_info)
    if m:
        return m.group(1).strip().strip('.')
    return None

uc_pubnums = []
for r in uc_rows:
    pub = extract_pub_number(r.get('Patents_info'))
    if pub:
        uc_pubnums.append(pub)
uc_pubnums = sorted(set(uc_pubnums))

# now find citing patents: those whose citation list contains any uc_pubnum
# Query all rows that have 'US-' etc? we only have uc_rows subset. Need full table scan based on LIKE of cited pub numbers.
# We'll build LIKE queries in python? not allowed. We'll approximate by scanning all publicationinfo in a single query: too big.
# Instead: use uc_pubnums to build SQL OR conditions and query citing rows.

# We'll output the OR like clauses list for subsequent query_db call.
clauses = []
for p in uc_pubnums:
    # citation is stored as text JSON; use LIKE
    esc = p.replace('%','\\%').replace('_','\\_')
    clauses.append(f"citation LIKE '%{esc}%'")
where = ' OR '.join(clauses) if clauses else '0'

out = {
  'uc_publication_numbers': uc_pubnums,
  'where_clause': where,
  'uc_count': len(uc_pubnums)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_podeueb7ZgQ1Fvj9LRgBnJmT': 'file_storage/call_podeueb7ZgQ1Fvj9LRgBnJmT.json', 'var_call_tnXJkoGwQIL9QloKmbYghE1p': 'file_storage/call_tnXJkoGwQIL9QloKmbYghE1p.json'}

exec(code, env_args)
