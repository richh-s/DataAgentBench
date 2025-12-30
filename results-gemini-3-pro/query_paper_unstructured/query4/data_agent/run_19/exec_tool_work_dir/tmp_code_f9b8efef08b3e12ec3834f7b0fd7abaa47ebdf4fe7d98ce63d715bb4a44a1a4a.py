code = """import json

# Load citations
with open('var_function-call-14128661174357449322.json', 'r') as f:
    citations_data = json.load(f)

citation_counts = {}
for row in citations_data:
    t = row['title']
    c = int(row['citation_count'])
    citation_counts[t] = citation_counts.get(t, 0) + c

# Load papers
with open('var_function-call-2833110841078300927.json', 'r') as f:
    papers_data = json.load(f)

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # remove .txt
    text = paper.get('text', '')
    
    # Check domain
    if 'physical activity' not in text.lower():
        continue
        
    # Check year
    # Look for 2016 in the first 500 characters
    header = text[:500]
    # Simple heuristic: if 2016 appears in the header, assume published in 2016.
    # Also look for '16 if it's a conference abbreviation like CHI '16
    if '2016' in header or "'16" in header or "’16" in header:
        # verify it's not a citation year like "cited 2016"
        # usually header contains "Copyright 2016" or "CHI '16"
        pass
    else:
        continue
        
    total_citations = citation_counts.get(title, 0)
    results.append({"title": title, "total_citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2089186070141819768': 'file_storage/function-call-2089186070141819768.json', 'var_function-call-17809202052441850212': 'file_storage/function-call-17809202052441850212.json', 'var_function-call-17961397819046338500': [{'count(*)': '1405'}], 'var_function-call-2833110841078300927': 'file_storage/function-call-2833110841078300927.json', 'var_function-call-14128661174357449322': 'file_storage/function-call-14128661174357449322.json'}

exec(code, env_args)
