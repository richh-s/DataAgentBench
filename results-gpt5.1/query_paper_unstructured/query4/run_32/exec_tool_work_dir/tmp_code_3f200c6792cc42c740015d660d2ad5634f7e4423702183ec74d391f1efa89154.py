code = """import re, json
from pathlib import Path

# Load full Mongo result
mongo_path = Path(var_call_DfBrU88CVj9F2bE5uLEH2fte)
with mongo_path.open() as f:
    mongo_records = json.load(f)

papers = []
for doc in mongo_records:
    text = doc.get('text', '')
    # heuristic: find a 4-digit year starting with 201 in first 1000 chars
    m = re.search(r"20(1[0-9]|20)", text[:1000])
    year = int(m.group(0)) if m else None
    # domain detection
    domain = 'physical activity' if re.search(r'physical activity', text, re.I) else None
    if year == 2016 and domain == 'physical activity':
        title = doc.get('filename', '').replace('.txt','')
        papers.append({'title': title, 'year': year, 'domain': domain})

# Load citations aggregation
cit_path = Path(var_call_fWkzC6xFpeHdLgrS6al7hZZC)
with cit_path.open() as f:
    cit_records = json.load(f)

cit_map = {c['title']: int(c['total_citations']) for c in cit_records}

results = []
for p in papers:
    # exact match
    total = cit_map.get(p['title'], 0)
    results.append({'title': p['title'], 'total_citations': total})

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_DfBrU88CVj9F2bE5uLEH2fte': 'file_storage/call_DfBrU88CVj9F2bE5uLEH2fte.json', 'var_call_fWkzC6xFpeHdLgrS6al7hZZC': 'file_storage/call_fWkzC6xFpeHdLgrS6al7hZZC.json'}

exec(code, env_args)
