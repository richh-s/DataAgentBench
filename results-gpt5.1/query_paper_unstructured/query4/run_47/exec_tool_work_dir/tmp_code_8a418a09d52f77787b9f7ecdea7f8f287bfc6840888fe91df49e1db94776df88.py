code = """import re, json
from pathlib import Path

# Load full mongo results
mongo_path = Path(var_call_lwZ9J61dbkKVu3dqXPGojy5a)
with mongo_path.open() as f:
    mongo_records = json.load(f)

# Extract title (filename sans .txt), year (first 4-digit year >= 2000), and domain via 'physical activity' mention
papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    # crude year extraction
    years = re.findall(r"(20[0-2][0-9])", text)
    year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2025:
            year = yi
            break
    title = doc.get('filename', '').replace('.txt', '')
    if year == 2016 and re.search(r"physical activity", text, re.I):
        papers.append({'title': title, 'year': year})

# Load citation aggregates
sql_path = Path(var_call_vbDxhKl1uFYyhXt2F0cD7fsm)
with sql_path.open() as f:
    sql_records = json.load(f)

citation_map = {r['title']: int(r['total_citations']) for r in sql_records}

results = []
for p in papers:
    # exact match on title
    c = citation_map.get(p['title'])
    results.append({'title': p['title'], 'total_citations': c})

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lwZ9J61dbkKVu3dqXPGojy5a': 'file_storage/call_lwZ9J61dbkKVu3dqXPGojy5a.json', 'var_call_vbDxhKl1uFYyhXt2F0cD7fsm': 'file_storage/call_vbDxhKl1uFYyhXt2F0cD7fsm.json'}

exec(code, env_args)
