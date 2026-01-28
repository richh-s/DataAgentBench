code = """import json

# Read the citations data
citations_file = var_functions.query_db:0
with open(citations_file) as f:
    citations_2018 = json.load(f)

# Read paper documents
papers_file = var_functions.query_db:5
with open(papers_file) as f:
    paper_docs = json.load(f)

# Build ACM papers dictionary
acm_titles = set()
for doc in paper_docs:
    text = doc.get('text', '').upper()
    if 'ACM' in text:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        if title:
            acm_titles.add(title)

# Find ACM papers cited in 2018
acm_citations = []
for citation in citations_2018:
    cit_title = citation.get('title', '')
    if cit_title in acm_titles:
        acm_citations.append(int(citation.get('citation_count', 0)))

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_papers': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
