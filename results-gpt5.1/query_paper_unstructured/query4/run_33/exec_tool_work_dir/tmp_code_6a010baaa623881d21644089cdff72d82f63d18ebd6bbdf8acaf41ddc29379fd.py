code = """import re, json
from pathlib import Path

# Load full results
with open(var_call_AVL5NJ9jyKe709YJhm6kmydk, 'r') as f:
    papers = json.load(f)
with open(var_call_F6p0YhaBRWj3iG6ZjDJxAxOC, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text
year_re = re.compile(r"\b(20\d{2}|19\d{2})\b")

records = []
for p in papers:
    text = p.get('text','')
    m = year_re.findall(text[:2000])
    year = None
    if m:
        years = [int(y) for y in m]
        cand = min(years)
        if 1900 <= cand <= 2025:
            year = cand
    title = p.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year})

# Filter to 2016 physical activity domain by searching text for phrase and year==2016
phys_2016_titles = {r['title'] for r in records if r['year'] == 2016}

# Sum citations already provided per title; now filter to our titles
phys_2016_citations = []
for c in citations:
    title = c['title'].strip('"')
    if title in phys_2016_titles:
        phys_2016_citations.append({'title': title, 'total_citations': int(c['total_citations'])})

result = phys_2016_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AVL5NJ9jyKe709YJhm6kmydk': 'file_storage/call_AVL5NJ9jyKe709YJhm6kmydk.json', 'var_call_F6p0YhaBRWj3iG6ZjDJxAxOC': 'file_storage/call_F6p0YhaBRWj3iG6ZjDJxAxOC.json'}

exec(code, env_args)
