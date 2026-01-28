code = """import json

# Load citations data for 2018
citations_data = var_functions.query_db:0
if isinstance(citations_data, str):
    with open(citations_data) as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data

# Load paper documents
papers_data = var_functions.query_db:5
if isinstance(papers_data, str):
    with open(papers_data) as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Build ACM titles set
acm_titles = set()
for doc in paper_docs:
    text = doc.get('text', '').upper()
    if 'ACM' in text:
        filename = doc.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            acm_titles.add(title)

# Match with 2018 citations
acm_citations = []
for citation in citations_2018:
    cit_title = citation.get('title', '')
    if cit_title in acm_titles:
        acm_citations.append(int(citation.get('citation_count', 0)))

# Calculate results
if acm_citations:
    avg = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg, 2),
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
