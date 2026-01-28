code = """import re, json
from pathlib import Path

# Load full citation aggregates
with open(var_call_9DXLLBcomBbs0N7AlfWcb1bQ, 'r') as f:
    citations = json.load(f)

# Load a reasonable subset of papers mentioning physical activity and 2016
with open(var_call_W8ARnsCqBzTFGCpcXUvJlPxS, 'r') as f:
    papers = json.load(f)

results = []

for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','')
    m = re.search(r'(19|20)\d{2}', text)
    year = int(m.group(0)) if m else None
    if year != 2016:
        continue
    title = filename.rsplit('.txt',1)[0]
    # find citation total
    total_cit = 0
    for row in citations:
        if row['title'].strip('"') == title:
            try:
                total_cit = int(row['total_citations'])
            except Exception:
                total_cit = row['total_citations']
            break
    results.append({'title': title, 'total_citations': total_cit})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_W8ARnsCqBzTFGCpcXUvJlPxS': 'file_storage/call_W8ARnsCqBzTFGCpcXUvJlPxS.json', 'var_call_9DXLLBcomBbs0N7AlfWcb1bQ': 'file_storage/call_9DXLLBcomBbs0N7AlfWcb1bQ.json'}

exec(code, env_args)
