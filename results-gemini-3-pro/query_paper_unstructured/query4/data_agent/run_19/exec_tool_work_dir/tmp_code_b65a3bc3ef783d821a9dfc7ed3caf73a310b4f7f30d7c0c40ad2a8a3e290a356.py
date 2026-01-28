code = """import json

# Get file paths from locals
citations_path = locals()['var_function-call-14128661174357449322']
papers_path = locals()['var_function-call-2833110841078300927']

# Load citations
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_counts = {}
for row in citations_data:
    t = row['title']
    c = int(row['citation_count'])
    citation_counts[t] = citation_counts.get(t, 0) + c

# Load papers
with open(papers_path, 'r') as f:
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
    header = text[:500]
    # Check for 2016 in header or '16
    if '2016' in header or "'16" in header or "’16" in header:
        pass
    else:
        continue
        
    total_citations = citation_counts.get(title, 0)
    results.append({"title": title, "total_citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2089186070141819768': 'file_storage/function-call-2089186070141819768.json', 'var_function-call-17809202052441850212': 'file_storage/function-call-17809202052441850212.json', 'var_function-call-17961397819046338500': [{'count(*)': '1405'}], 'var_function-call-2833110841078300927': 'file_storage/function-call-2833110841078300927.json', 'var_function-call-14128661174357449322': 'file_storage/function-call-14128661174357449322.json'}

exec(code, env_args)
