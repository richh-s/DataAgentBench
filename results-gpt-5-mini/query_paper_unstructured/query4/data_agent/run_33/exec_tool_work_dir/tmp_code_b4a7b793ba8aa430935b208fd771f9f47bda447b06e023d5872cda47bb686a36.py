code = """import json
# load citations aggregation result
with open(var_call_CI4flWKd1V2IDGAGR2Msmp2L, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Filter titles that mention 'physical activity' domain - using hint that domain may be in titles or known set
# We'll select papers whose titles or known list include keywords 'physical activity', 'activity', 'activity tracker', etc.
keywords = ['physical activity','activity','activity tracker','activity tracking','activity trackers','physical-activity','exercise']
matches = []
for r in citations:
    t = r.get('title','')
    low = t.lower()
    for kw in keywords:
        if kw in low:
            matches.append({'title': t, 'total_citations': int(r['total_citations'])})
            break

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_MofUK2m03WbBxbNaWInNuQUc': 'file_storage/call_MofUK2m03WbBxbNaWInNuQUc.json', 'var_call_CVUkhUcAwiQzAT1X9ezOtb8s': [], 'var_call_8e2mPHQzlupulgcMsl5j9Fx8': 'file_storage/call_8e2mPHQzlupulgcMsl5j9Fx8.json', 'var_call_1dqZJPG8Xcds5IamNQEwYsx4': [], 'var_call_FGeeAyPEj8L6Pq4zzkFbmoSo': ['Citations', 'sqlite_sequence'], 'var_call_CI4flWKd1V2IDGAGR2Msmp2L': 'file_storage/call_CI4flWKd1V2IDGAGR2Msmp2L.json'}

exec(code, env_args)
