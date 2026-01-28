code = """import json

# Access the citations data for 2018 from stored variables
citations_2018 = locals()['var_functions.query_db:0']

# Access the paper documents data from stored variables
paper_docs = locals()['var_functions.query_db:2']

# Check if these are file paths (strings) or actual data
if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Create title to document mapping
title_to_doc = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        title_to_doc[title] = doc

# Extract ACM papers from citations
acm_papers = []
for citation in citations_2018:
    cit_title = citation.get('title', '')
    if cit_title in title_to_doc:
        doc = title_to_doc[cit_title]
        text = doc.get('text', '')
        # Check if paper is from ACM
        if 'ACM' in text or 'acm' in text or 'Association for Computing Machinery' in text:
            acm_papers.append({
                'title': cit_title,
                'citation_count': int(citation.get('citation_count', 0))
            })

# Calculate average citation count
if acm_papers:
    total_citations = sum(p['citation_count'] for p in acm_papers)
    avg_citations = total_citations / len(acm_papers)
    result = {
        'acm_papers_count': len(acm_papers),
        'total_citations': total_citations,
        'average_citations': round(avg_citations, 2)
    }
else:
    result = {'acm_papers_count': 0, 'total_citations': 0, 'average_citations': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
