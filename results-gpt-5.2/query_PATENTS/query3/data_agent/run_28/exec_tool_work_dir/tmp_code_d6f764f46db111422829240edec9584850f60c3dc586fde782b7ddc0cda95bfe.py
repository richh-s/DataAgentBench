code = """import json, re
import pandas as pd

# load UC-assigned publications (could be file path)
rec = var_call_2XMXyBFfZI8aURDPjg9UvGT6
if isinstance(rec, str):
    with open(rec, 'r', encoding='utf-8') as f:
        rec = json.load(f)

def extract_pub_number(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', patents_info)
    if m:
        return m.group(1)
    # other patterns
    m = re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\b', patents_info)
    if m:
        return m.group(1)
    return None

uc_pubs = []
for r in rec:
    pn = extract_pub_number(r.get('Patents_info',''))
    if pn:
        uc_pubs.append(pn)
uc_pubs = sorted(set(uc_pubs))

# pull all records that cite any of these UC pubs
# SQLite has parameter limit; chunk
chunks = [uc_pubs[i:i+500] for i in range(0, len(uc_pubs), 500)]

# We'll query by LIKE on citation text for each chunk via OR, since citation is JSON-like string
# To reduce size, only select needed fields

queries = []
for ch in chunks:
    ors = ' OR '.join([f"citation LIKE '%\"publication_number\": \"{pn}\"%'" for pn in ch])
    queries.append(f"SELECT Patents_info, cpc, citation, title_localized FROM publicationinfo WHERE ({ors});")

print('__RESULT__:')
print(json.dumps({'uc_publication_numbers_count': len(uc_pubs), 'sql_queries_to_run': queries[:5], 'sql_queries_total': len(queries)}))"""

env_args = {'var_call_1qqHLHChxvaoBiBUSDt8j9Xn': ['publicationinfo'], 'var_call_ebIZYTH9V4k3B9k7wzQIfopr': ['cpc_definition'], 'var_call_xLB0RW8rsY3zUFgZ6QoQjcQn': [], 'var_call_2XMXyBFfZI8aURDPjg9UvGT6': 'file_storage/call_2XMXyBFfZI8aURDPjg9UvGT6.json'}

exec(code, env_args)
