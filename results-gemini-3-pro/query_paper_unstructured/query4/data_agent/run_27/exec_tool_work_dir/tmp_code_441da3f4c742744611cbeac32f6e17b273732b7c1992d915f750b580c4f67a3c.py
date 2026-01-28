code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-14323313354234643834'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-7764328309385985012'], 'r') as f:
    citations = json.load(f)

# Aggregate citations by title
citation_map = {}
for c in citations:
    t = c['title']
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    citation_map[t] = citation_map.get(t, 0) + count

results = []

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    # Heuristic: If 2016 appears in the header, assume it's published in 2016.
    # We should probably filter out years that are clearly citations (like [21] or something, but \b20\d{2}\b is fairly safe for years)
    # However, sometimes a 2015 paper mentions "Copyright 2015".
    # I'll check if '2016' is in the years found.
    published_in_2016 = '2016' in years
    
    # Extract Domain
    content_sample = text[:5000].lower()
    is_physical_activity = 'physical activity' in content_sample
    
    if published_in_2016 and is_physical_activity:
        total_citations = citation_map.get(title, 0)
        results.append({"title": title, "citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8814252410451424238': ['paper_docs'], 'var_function-call-5259206578733669392': 'file_storage/function-call-5259206578733669392.json', 'var_function-call-14323313354234643834': 'file_storage/function-call-14323313354234643834.json', 'var_function-call-12161874527337870347': ['Citations', 'sqlite_sequence'], 'var_function-call-7764328309385985012': 'file_storage/function-call-7764328309385985012.json'}

exec(code, env_args)
