code = """import json
import re

# Load data
with open(locals()['var_function-call-7459141219968339162'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-17043150740226976793'], 'r') as f:
    citations = json.load(f)

# Build citation map
citation_map = {}
for c in citations:
    t = c['title'].strip().lower()
    count = int(c['citation_count'])
    if t in citation_map:
        citation_map[t] += count
    else:
        citation_map[t] = count

food_papers = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title_from_filename = filename.replace('.txt', '').strip()
    
    is_food = False
    
    # 1. Check title
    if 'food' in title_from_filename.lower():
        is_food = True
        
    # 2. Check Keywords
    if not is_food:
        header = text[:5000]
        match = re.search(r'(?:Author Keywords|Index Terms|Keywords)(.*?)(?:ACM Classification|Introduction|General Terms|Category)', header, re.IGNORECASE | re.DOTALL)
        if match:
            keywords = match.group(1).lower()
            if 'food' in keywords:
                is_food = True
                
    if is_food:
        food_papers.append(title_from_filename)

total_citations = 0
found_details = []
for t in food_papers:
    t_norm = t.strip().lower()
    c = citation_map.get(t_norm, 0)
    total_citations += c
    found_details.append({"title": t, "citations": c})

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "papers": found_details}))"""

env_args = {'var_function-call-3676184941267040123': 'file_storage/function-call-3676184941267040123.json', 'var_function-call-6873213907714452995': 'file_storage/function-call-6873213907714452995.json', 'var_function-call-17043150740226976793': 'file_storage/function-call-17043150740226976793.json', 'var_function-call-7459141219968339162': 'file_storage/function-call-7459141219968339162.json'}

exec(code, env_args)
