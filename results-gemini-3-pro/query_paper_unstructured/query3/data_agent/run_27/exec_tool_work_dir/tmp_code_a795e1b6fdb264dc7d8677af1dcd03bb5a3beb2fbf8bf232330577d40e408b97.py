code = """import json
import re
import os

# Load citations
path_cit = locals()['var_function-call-76014379587843141']
with open(path_cit, 'r') as f:
    citations_list = json.load(f)

# Map title -> count
cit_map = {}
for item in citations_list:
    t = item['title']
    c = int(item['total_citations'])
    cit_map[t] = c

# Load papers
path_papers = locals()['var_function-call-15302473096394275436']
with open(path_papers, 'r') as f:
    papers = json.load(f)

results = []
debug_years = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Extract year
    # Look for 4 digits starting with 20 in first 500 chars
    m = re.search(r'(20\d{2})', text[:500])
    if m:
        year = int(m.group(1))
    else:
        year = 0 # unknown
    
    if year > 2016:
        # Check contribution
        # Simple check: 'empirical' in text
        if 'empirical' in text.lower():
            count = cit_map.get(title, 0)
            results.append({"title": title, "total_citation_count": count})

# Sort by title
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3735696705524140447': 'file_storage/function-call-3735696705524140447.json', 'var_function-call-8426954921484076460': ['paper_docs'], 'var_function-call-8432852988790509735': [{'COUNT(*)': '1405'}], 'var_function-call-15575652384849502838': [], 'var_function-call-76014379587843141': 'file_storage/function-call-76014379587843141.json', 'var_function-call-15302473096394275436': 'file_storage/function-call-15302473096394275436.json'}

exec(code, env_args)
