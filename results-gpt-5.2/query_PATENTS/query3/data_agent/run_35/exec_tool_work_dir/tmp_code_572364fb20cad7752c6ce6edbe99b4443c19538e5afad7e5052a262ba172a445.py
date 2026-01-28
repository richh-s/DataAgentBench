code = """import json, re

path = var_call_cL1gMAJuLQisJ9ffV0GEZcx8
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

uc_pubs = set()
for r in recs:
    pi = r.get('Patents_info') or ''
    m = re.search(r'pub\.? number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
    if m:
        uc_pubs.add(m.group(1))

print('__RESULT__:')
print(json.dumps({'count': len(uc_pubs), 'sample': sorted(list(uc_pubs))[:20]}))"""

env_args = {'var_call_2H482CA64rUxdSoVjRJaxcrD': ['publicationinfo'], 'var_call_HO506ZI5IX9dpFemlQpYdkNT': ['cpc_definition'], 'var_call_jWkd0v2qnfrVS2uEDoJTPCEv': [], 'var_call_ufsEQoeFmLtnJhEZ82Fctw0q': 'file_storage/call_ufsEQoeFmLtnJhEZ82Fctw0q.json', 'var_call_WJKlOXkn0LMKx9Emg64JyUy4': {'uc_publications_found': [], 'count': 0}, 'var_call_cL1gMAJuLQisJ9ffV0GEZcx8': 'file_storage/call_cL1gMAJuLQisJ9ffV0GEZcx8.json', 'var_call_KPillqHZwUDQ18URxYLjmB6e': 'file_storage/call_KPillqHZwUDQ18URxYLjmB6e.json'}

exec(code, env_args)
