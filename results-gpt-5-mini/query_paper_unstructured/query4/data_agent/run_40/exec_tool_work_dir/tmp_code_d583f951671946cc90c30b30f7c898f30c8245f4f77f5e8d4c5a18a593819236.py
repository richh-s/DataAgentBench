code = """import json
path = var_call_F9oCE3SE9KbrlJYKWyW52bE9
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Filter titles that likely correspond to papers published in 2016 in the 'physical activity' domain.
# We need to join with paper_docs to determine publication year and domain. For now, list candidate titles that mention 'physical activity' or related.
candidates = []
for r in records:
    title = r.get('title','')
    # simple filter: titles that include 'physical activity' or 'activity' or 'exercise' or 'activity trackers' etc.
    if research := (('physical activity' in title.lower()) or ('activity' in title.lower()) or ('exercise' in title.lower()) or ('fitness' in title.lower())):
        candidates.append({'title': title, 'total_citations': int(r.get('total_citations') )})
# deduplicate
seen = set()
cand_unique = []
for c in candidates:
    if c['title'] not in seen:
        seen.add(c['title'])
        cand_unique.append(c)

import json
print('__RESULT__:')
print(json.dumps(cand_unique))"""

env_args = {'var_call_dZcb7oiZgAHY4QVK8xj1Nin6': 'file_storage/call_dZcb7oiZgAHY4QVK8xj1Nin6.json', 'var_call_jX3aMtn3six7yGSA1qsFYicb': [], 'var_call_ArPkaigkLlJbnG0DtleLJDpz': ['paper_docs'], 'var_call_uDJDEG1WUDDBdEQCbx5fId9d': 'file_storage/call_uDJDEG1WUDDBdEQCbx5fId9d.json', 'var_call_n4NrV33CJT5NQRfFghmgImjS': [], 'var_call_F9oCE3SE9KbrlJYKWyW52bE9': 'file_storage/call_F9oCE3SE9KbrlJYKWyW52bE9.json'}

exec(code, env_args)
