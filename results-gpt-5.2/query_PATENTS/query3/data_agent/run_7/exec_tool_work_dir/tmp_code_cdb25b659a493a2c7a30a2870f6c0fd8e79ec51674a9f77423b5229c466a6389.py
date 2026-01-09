code = """import json, re, pandas as pd

# Load citing-side records that mention UNIV CALIFORNIA (for cited-side we need assignee names)
path = var_call_32FcVDZfzFqhgKaVXxdtGrYO
with open(path, 'r', encoding='utf-8') as f:
    cited_uc_recs = json.load(f)

# Build set of UC publication_numbers (cited targets)
uc_pubs = set()
for r in cited_uc_recs:
    pi = r.get('Patents_info','') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9\-]*?)\b', pi)
    if m:
        uc_pubs.add(m.group(1))

# Pull all records (citing universe) with citations containing any of these UC pubs
# We'll do a coarse SQL LIKE query per prefix to reduce size: use first 8 chars maybe.
# Instead, just query all rows with 'citation' containing 'US-' etc then filter in python.

# Get all rows with non-empty citation
# (can't query here; use existing tool results only) -> need tool call outside python.

print('__RESULT__:')
print(json.dumps({'uc_publications_count': len(uc_pubs), 'sample_uc_publications': sorted(list(uc_pubs))[:20]}))"""

env_args = {'var_call_L9PcQ9ViTcmIoQKlufknTEOs': ['publicationinfo'], 'var_call_jFzSdOxWdZ8AEHUCyMFYMZEd': ['cpc_definition'], 'var_call_mMyUsI7E40mgWFzvNjfDjqs3': [], 'var_call_32FcVDZfzFqhgKaVXxdtGrYO': 'file_storage/call_32FcVDZfzFqhgKaVXxdtGrYO.json'}

exec(code, env_args)
