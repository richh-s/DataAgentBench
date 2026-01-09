code = """import json, re

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

chunks = [uc_pubs[i:i+200] for i in range(0, len(uc_pubs), 200)]
queries = []
for ch in chunks:
    ors = ' OR '.join([f"citation LIKE '%\\\"publication_number\\\": \\\"{pn}\\\"%'" for pn in ch])
    q = "SELECT Patents_info, cpc, citation, title_localized FROM publicationinfo WHERE (" + ors + ");"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'uc_publication_numbers_count': len(uc_pubs), 'sql_queries_total': len(queries), 'first_query': (queries[0] if queries else None)}))"""

env_args = {'var_call_1qqHLHChxvaoBiBUSDt8j9Xn': ['publicationinfo'], 'var_call_ebIZYTH9V4k3B9k7wzQIfopr': ['cpc_definition'], 'var_call_xLB0RW8rsY3zUFgZ6QoQjcQn': [], 'var_call_2XMXyBFfZI8aURDPjg9UvGT6': 'file_storage/call_2XMXyBFfZI8aURDPjg9UvGT6.json'}

exec(code, env_args)
