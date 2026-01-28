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

# Create a mapping from paper titles to documents
# Extract title from filename
citation_titles = set()
for c in citations_data:
    title = c.get('title', '').strip().lower()
    citation_titles.add(title)

print('Number of unique citation titles: {}'.format(len(citation_titles)))

# Build a dictionary of papers with extracted titles
papers_dict = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    if filename:
        # Extract title from filename
        title_from_filename = filename.replace('.txt', '').strip().lower()
        papers_dict[title_from_filename] = paper
        
        # Also try to extract title from the text content for verification
        text = paper.get('text', '')
        lines = text.split('\n')
        for line in lines[:15]:  # Check first 15 lines for title
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('Permission'):
                # Title is often uppercase or title case
                if line.isupper() or (line[0].isupper() and len(line.split()) > 3):
                    title_from_text = line.strip().lower()
                    if title_from_text not in papers_dict:
                        papers_dict[title_from_text] = paper
                    break

print('Number of papers in dictionary: {}'.format(len(papers_dict)))

# Now match citations with papers
acm_citations = []
matched_papers = []
missing_papers = []

for citation in citations_data:
    citation_title = citation.get('title', '').strip().lower()
    citation_count = int(citation.get('citation_count', 0))
    
    # Find matching paper
    paper = papers_dict.get(citation_title)
    
    if not paper:
        # Try fuzzy matching - look for papers containing the citation title
        for paper_title, paper_doc in papers_dict.items():
            if citation_title in paper_title or paper_title in citation_title:
                paper = paper_doc
                break
    
    if paper:
        matched_papers.append(citation_title)
        # Check if ACM paper
        text = paper.get('text', '').lower()
        if 'acm' in text:
            acm_citations.append(citation_count)
    else:
        missing_papers.append(citation.get('title'))

print('Matched papers: {}'.format(len(matched_papers)))
print('Missing papers: {}'.format(len(missing_papers)))
print('ACM papers with citations: {}'.format(len(acm_citations)))

if len(acm_citations) > 0:
    avg = sum(acm_citations) / len(acm_citations)
    total = sum(acm_citations)
    print('Average citations for ACM papers: {}'.format(avg))
    print('Total citations for ACM papers: {}'.format(total))
else:
    avg = 0
    total = 0

result = {
    'matched_papers': len(matched_papers),
    'missing_papers': len(missing_papers),
    'acm_papers_count': len(acm_citations),
    'average_citations': avg,
    'total_acm_citations': total,
    'sample_missing': missing_papers[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}}

exec(code, env_args)
