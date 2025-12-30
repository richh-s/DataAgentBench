code = """import json
import re

# Load data
with open(locals()['var_function-call-15899723909047088907'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-3855934582646754385'], 'r') as f:
    paper_docs = json.load(f)

citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

chi_papers_found = []
debug_headers = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    header_text = text[:1000] # First 1000 chars
    
    # Check
    if re.search(r'\bCHI\b', header_text) or re.search(r'Conference on Human Factors in Computing Systems', header_text, re.IGNORECASE):
        title = filename.replace('.txt', '')
        count = citation_map.get(title, 0)
        chi_papers_found.append({'title': title, 'count': count})
    else:
        # Collect some non-CHI headers for inspection
        if len(debug_headers) < 5:
            debug_headers.append({'title': filename, 'header': header_text[:200]})

print("__RESULT__:")
print(json.dumps({
    "total_docs": len(paper_docs),
    "chi_papers_count": len(chi_papers_found),
    "total_citations": sum(p['count'] for p in chi_papers_found),
    "sample_chi_papers": chi_papers_found[:5],
    "sample_non_chi_headers": debug_headers
}))"""

env_args = {'var_function-call-15899723909047088907': 'file_storage/function-call-15899723909047088907.json', 'var_function-call-3855934582646754385': 'file_storage/function-call-3855934582646754385.json', 'var_function-call-1503467888585593551': 16}

exec(code, env_args)
