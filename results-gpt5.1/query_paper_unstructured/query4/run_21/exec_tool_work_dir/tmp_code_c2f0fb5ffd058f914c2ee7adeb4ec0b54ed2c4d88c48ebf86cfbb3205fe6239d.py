code = """import re, json
from pathlib import Path

# Load full Mongo result
path = Path(var_call_rSbmuzIjgZr4cuAbitYhwS2b)
with path.open() as f:
    mongo_docs = json.load(f)

physical_2016_titles = []
for doc in mongo_docs:
    text = doc.get('text', '')
    # crude year detection
    if '2016' not in text:
        continue
    if re.search(r'physical activity', text, re.I):
        filename = doc.get('filename','')
        title = re.sub(r'\.txt$', '', filename)
        physical_2016_titles.append(title)

# deduplicate
physical_2016_titles = sorted(set(physical_2016_titles))

# Load citations aggregation
path2 = Path(var_call_wk3XxFtUaBiEWDpWZll65QSX)
with path2.open() as f:
    citations = json.load(f)

# build map title -> total_citations
cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []
for t in physical_2016_titles:
    if t in cit_map:
        results.append({'title': t, 'total_citations': cit_map[t]})

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_rSbmuzIjgZr4cuAbitYhwS2b': 'file_storage/call_rSbmuzIjgZr4cuAbitYhwS2b.json', 'var_call_wk3XxFtUaBiEWDpWZll65QSX': 'file_storage/call_wk3XxFtUaBiEWDpWZll65QSX.json'}

exec(code, env_args)
