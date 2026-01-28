code = """import json
# Load Mongo query result from storage variable
with open(var_call_aYiyKGOoBYD1V7En6jbcyyfz, 'r') as f:
    records = json.load(f)

titles = []
for r in records:
    filename = r.get('filename','')
    text = r.get('text','')
    if not filename or not text:
        continue
    lower = text.lower()
    # domain match: contains 'physical activity'
    if 'physical activity' not in lower:
        continue
    # publication year heuristic: look for '2016' in first 1000 chars (header area)
    if '2016' not in text[:1000]:
        continue
    title = filename
    if title.lower().endswith('.txt'):
        title = title[:-4]
    titles.append(title)

# de-duplicate
titles = sorted(list(set(titles)))
import json as _json
print('__RESULT__:')
print(_json.dumps(titles))"""

env_args = {'var_call_q1A0x1ef4aui3tx6vTkmVFcN': ['paper_docs'], 'var_call_BO6vopfLPkVKZx6CZsEf1NUO': ['Citations', 'sqlite_sequence'], 'var_call_aYiyKGOoBYD1V7En6jbcyyfz': 'file_storage/call_aYiyKGOoBYD1V7En6jbcyyfz.json'}

exec(code, env_args)
