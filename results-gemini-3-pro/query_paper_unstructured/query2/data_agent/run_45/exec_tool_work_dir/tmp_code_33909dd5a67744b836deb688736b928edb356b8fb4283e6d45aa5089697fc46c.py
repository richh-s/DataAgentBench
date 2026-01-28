code = """import json

# Load citations
with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations_list = json.load(f)

# Load papers
with open(locals()['var_function-call-17448438011554741318'], 'r') as f:
    papers_list = json.load(f)

# Create a map of title -> citation_count
citation_map = {c['title']: c['citation_count'] for c in citations_list}

acm_citations = []

for paper in papers_list:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if published by ACM
    # Check first 5000 characters for ACM
    if 'ACM' in text[:5000]:
        if title in citation_map:
            acm_citations.append(citation_map[title])

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json'}

exec(code, env_args)
