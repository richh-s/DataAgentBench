code = """import json

# Load data again
citations_path = locals()['var_function-call-10128853651664279531']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

acm_papers_path = locals()['var_function-call-2153954921317662099']
with open(acm_papers_path, 'r') as f:
    acm_papers_data = json.load(f)

# Extract titles
citation_titles = set(item['title'] for item in citations_data)
acm_titles = set()
for p in acm_papers_data:
    if p.get('filename', '').endswith('.txt'):
        acm_titles.add(p['filename'][:-4])

# Intersection
intersection = citation_titles.intersection(acm_titles)

debug_info = {
    "count_citations_2018": len(citation_titles),
    "count_acm_papers_returned": len(acm_papers_data),
    "count_intersection": len(intersection),
    "sample_citation_titles": list(citation_titles)[:5],
    "sample_acm_titles": list(acm_titles)[:5]
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10128853651664279531': 'file_storage/function-call-10128853651664279531.json', 'var_function-call-13767594165860701791': 'file_storage/function-call-13767594165860701791.json', 'var_function-call-447385373725122589': 'file_storage/function-call-447385373725122589.json', 'var_function-call-2153954921317662099': 'file_storage/function-call-2153954921317662099.json', 'var_function-call-2779362211671997774': {'matched_papers_count': 2, 'average_citations': 68.5}}

exec(code, env_args)
