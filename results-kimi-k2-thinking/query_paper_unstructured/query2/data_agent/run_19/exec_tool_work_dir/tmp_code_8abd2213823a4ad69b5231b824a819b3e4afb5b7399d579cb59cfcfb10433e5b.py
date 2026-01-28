code = """import json

# Load the data  
citations_file_path = locals()['var_functions.query_db:2']
papers_file_path = locals()['var_functions.query_db:4']

with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Build a mapping of paper titles to metadata
paper_meta = {}
for p in papers_data:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    source = None
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    paper_meta[title] = {'source': source, 'text': text[:200]}

# Find ACM papers
acm_papers = {k:v for k,v in paper_meta.items() if v['source'] == 'ACM'}

# Match with citations
citation_titles = [c['title'] for c in citations_data]

# Look for exact matches first
exact_matches = []
for ct in citation_titles:
    if ct in acm_papers:
        exact_matches.append(ct)

# Also check for close matches
close_matches = []
for ct in citation_titles:
    for apt in acm_papers.keys():
        if ct.lower() == apt.lower() or (len(ct) > 10 and ct.lower() in apt.lower()):
            close_matches.append((ct, apt))
            break

result = {
    'total_citations_2018': len(citations_data),
    'acm_papers_in_corpus': len(acm_papers),
    'exact_matches': len(exact_matches),
    'close_matches': len(close_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'total_citations_2018': 158, 'acm_papers_count': 2, 'average_citation_count': 68.5, 'acm_citations_list': [50, 87]}}

exec(code, env_args)
