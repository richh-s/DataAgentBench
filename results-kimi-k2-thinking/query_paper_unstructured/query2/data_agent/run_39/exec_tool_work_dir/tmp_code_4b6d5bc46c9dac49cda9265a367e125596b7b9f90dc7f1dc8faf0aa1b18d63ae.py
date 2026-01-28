code = """import json
import re

# Load citations data
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

# Load paper docs data  
paper_docs_data = locals()['var_functions.query_db:2']
if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

# Get all citation titles
citation_titles = [item['title'] for item in citations_data]
print(f"Total citation titles in 2018: {len(citation_titles)}")

# Get all paper titles from MongoDB
paper_titles = []
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    paper_titles.append(title)

print(f"Total paper titles in MongoDB: {len(paper_titles)}")

# Check for exact matches
exact_matches = set(citation_titles) & set(paper_titles)
print(f"Exact title matches: {len(exact_matches)}")

# Check for papers with ACM in their content that also have citations in 2018
acm_candidate_titles = []
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    if re.search(r'\bACM\b', text, re.IGNORECASE):
        acm_candidate_titles.append(title)

print(f"ACM papers in MongoDB: {len(acm_candidate_titles)}")

# Check if any of these ACM papers have citations in 2018
acm_citations = []
for title in acm_candidate_titles:
    for citation in citations_data:
        if citation['title'] == title:
            acm_citations.append({
                'title': title,
                'citations': int(citation['citation_count'])
            })

print(f"ACM papers with 2018 citations: {len(acm_citations)}")

# Let's sample a few titles to see what they look like
print("\nSample citation titles:")
for title in citation_titles[:5]:
    print(f"  - {title}")

print("\nSample paper titles from MongoDB:")
for title in paper_titles[:5]:
    print(f"  - {title}")

result = {
    'citation_titles_count': len(citation_titles),
    'paper_titles_count': len(paper_titles),
    'exact_matches': len(exact_matches),
    'acm_papers_count': len(acm_candidate_titles),
    'acm_papers_with_citations': len(acm_citations)
}

if acm_citations:
    total_citations = sum(item['citations'] for item in acm_citations)
    result['average_citation_count'] = round(total_citations / len(acm_citations), 2)
else:
    result['average_citation_count'] = 0

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'acm_papers_count': 0, 'total_citations': 0, 'average_citation_count': 0, 'message': 'No ACM papers found in 2018 citations'}}

exec(code, env_args)
