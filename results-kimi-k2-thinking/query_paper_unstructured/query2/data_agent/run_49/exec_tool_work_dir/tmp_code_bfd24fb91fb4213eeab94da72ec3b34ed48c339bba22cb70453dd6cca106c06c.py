code = """import json
import re

# Load the 2018 citations data
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

# Load the paper documents
papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

# Create dictionary of papers with their titles (without .txt extension)
papers_dict = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    papers_dict[title] = paper

print('Total citations in 2018: {}'.format(len(citations_data)))
print('Total papers in database: {}'.format(len(papers_dict)))

# Identify ACM papers and collect their citation counts
acm_citations = []
missing_papers = []
non_acm_papers = []

for citation in citations_data:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Find the paper document
    paper = papers_dict.get(title)
    if not paper:
        # Try to find by normalized title
        matching_found = False
        for paper_title, paper_doc in papers_dict.items():
            if paper_title.strip().lower() == title.strip().lower():
                paper = paper_doc
                matching_found = True
                break
        if not matching_found:
            missing_papers.append(title)
            continue
    
    # Check if it's an ACM paper by searching for ACM in the text
    text = paper.get('text', '').lower()
    
    # Look for ACM indicators
    if 'acm' in text:
        # Additional verification - check for common ACM patterns
        acm_patterns = ['acm', 'association for computing machinery']
        if any(pattern in text for pattern in acm_patterns):
            acm_citations.append(citation_count)
        else:
            non_acm_papers.append((title, 'found ACM but not pattern'))
    else:
        # Also check if it's an IEEE or other publisher to be sure
        if 'ieee' in text or 'pubmed' in text:
            non_acm_papers.append((title, 'other publisher'))
        else:
            non_acm_papers.append((title, 'no publisher found'))

print('ACM papers with 2018 citations: {}'.format(len(acm_citations)))
print('Non-ACM/undetermined papers: {}'.format(len(non_acm_papers)))
print('Missing papers: {}'.format(len(missing_papers)))
print('Sample missing papers: {}'.format(missing_papers[:5]))

if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    print('Average citation count for ACM papers in 2018: {}'.format(avg_citations))
    print('Total citations for ACM papers: {}'.format(sum(acm_citations)))
    print('Min/Max citations: {}, {}'.format(min(acm_citations), max(acm_citations)))
else:
    print('No ACM papers found with 2018 citations')

__RESULT__:
print(json.dumps({
    'acm_papers_count': len(acm_citations),
    'total_2018_citations': len(citations_data),
    'missing_papers': len(missing_papers),
    'average_citations': sum(acm_citations) / len(acm_citations) if acm_citations else 0,
    'total_citations_for_acm_papers': sum(acm_citations) if acm_citations else 0
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
