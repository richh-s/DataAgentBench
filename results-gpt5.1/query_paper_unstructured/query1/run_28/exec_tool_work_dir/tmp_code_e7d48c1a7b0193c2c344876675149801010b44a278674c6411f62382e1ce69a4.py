code = """import json, os, re
from collections import defaultdict

# Load full Mongo and SQL results
with open(var_call_pmzeTXmaqsnfRhZYQjq7uOFo, 'r') as f:
    mongo_docs = json.load(f)
with open(var_call_OIIBJ366SJKctQobuBgePQn3, 'r') as f:
    sql_rows = json.load(f)

# Extract titles of papers in 'food' domain.
food_titles = set()
pattern = re.compile(r"domain\s*[:=]\s*\[?[^\n]*food[^\n]*", re.IGNORECASE)
for doc in mongo_docs:
    text = doc.get('text','')
    if 'food' in text.lower():
        if pattern.search(text) or 'domain' in text.lower():
            filename = doc.get('filename','')
            if filename.lower().endswith('.txt'):
                title = filename[:-4]
            else:
                title = filename
            if title:
                food_titles.add(title)

# Sum citations for these titles
food_titles_lower = {t.lower() for t in food_titles}

total_citations = 0
for row in sql_rows:
    title = row.get('title','')
    if title.lower() in food_titles_lower:
        try:
            c = int(row.get('citation_count',0))
        except ValueError:
            c = 0
        total_citations += c

result = total_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pmzeTXmaqsnfRhZYQjq7uOFo': 'file_storage/call_pmzeTXmaqsnfRhZYQjq7uOFo.json', 'var_call_OIIBJ366SJKctQobuBgePQn3': 'file_storage/call_OIIBJ366SJKctQobuBgePQn3.json'}

exec(code, env_args)
