code = """import json
import re

# Load citations data from 2018
citations_file = var_functions.query_db:8
try:
    if isinstance(citations_file, str):
        with open(citations_file, 'r') as f:
            citations_2018 = json.load(f)
    else:
        citations_2018 = citations_file
except Exception as e:
    print(f"Error loading citations: {e}")
    citations_2018 = []

# Load paper documents
paper_docs_file = var_functions.query_db:4
try:
    if isinstance(paper_docs_file, str):
        with open(paper_docs_file, 'r') as f:
            paper_docs = json.load(f)
    else:
        paper_docs = paper_docs_file
except Exception as e:
    print(f"Error loading paper docs: {e}")
    paper_docs = []

print(f"Total citations in 2018: {len(citations_2018)}")
print(f"Total paper documents: {len(paper_docs)}")

# Create a dictionary of citations for easy lookup
citations_dict = {}
for citation in citations_2018:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citations_dict[title] = count

print(f"Citations dictionary size: {len(citations_dict)}")

# Process paper documents to extract information
acm_papers_with_citations = []

for paper in paper_docs:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if this paper has citations in 2018
    if title in citations_dict:
        # Look for ACM in the text (source information)
        # Common patterns for ACM publications
        if 'ACM' in text or 'acm' in text or re.search(r'Proceedings of.*ACM', text, re.IGNORECASE):
            citation_count = citations_dict[title]
            acm_papers_with_citations.append({
                'title': title,
                'citation_count': citation_count
            })

print(f"ACM papers with 2018 citations: {len(acm_papers_with_citations)}")

# Calculate average citation count
if acm_papers_with_citations:
    total_citations = sum(paper['citation_count'] for paper in acm_papers_with_citations)
    average_citations = total_citations / len(acm_papers_with_citations)
    print(f"Total citations for ACM papers: {total_citations}")
    print(f"Average citations: {average_citations:.2f}")
    
    # Show some examples
    print(f"\nFirst few ACM papers:")
    for i, paper in enumerate(acm_papers_with_citations[:5]):
        print(f"  {paper['title']}: {paper['citation_count']} citations")
else:
    average_citations = 0
    print("No ACM papers found with 2018 citations")

# Return the result
result = {
    'average_citation_count': round(average_citations, 2),
    'acm_papers_count': len(acm_papers_with_citations),
    'total_citations': sum(paper['citation_count'] for paper in acm_papers_with_citations) if acm_papers_with_citations else 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
