code = """import json
import re

# Load citation data for 2018
citations_file = var_functions.query_db:0
citations_2018 = []
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = var_functions.query_db:0

# Load paper documents
papers_file = var_functions.query_db:2
paper_docs = []
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:2

print(f"Total 2018 citations: {len(citations_2018)}")
print(f"Total papers in database: {len(paper_docs)}")

# Create a mapping of paper titles to their documents for faster lookup
# The title in citations matches filename without .txt
papers_by_title = {}
for paper in paper_docs:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    papers_by_title[title] = paper

# Process each citation and check if it was published by ACM
acm_citations = []

for citation in citations_2018:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Find the corresponding paper document
    paper_doc = papers_by_title.get(citation_title, None)
    
    if paper_doc:
        text = paper_doc.get('text', '')
        
        # Extract source/publisher information - looking for ACM mentions
        # Common patterns in academic papers:
        # - "ACM Classification Keywords"
        # - "Permission to make digital or hard copies... ACM"
        # - Copyright lines with ACM
        # - "http://dx.doi.org/10.1145/" (ACM DOI pattern)
        
        # Check if the paper is published by ACM
        is_acm = False
        
        # Check for ACM in the text (case insensitive)
        if re.search(r'\bACM\b', text, re.IGNORECASE):
            # Check for ACM-specific patterns to ensure it's the publisher, not just a reference
            if re.search(r'Permission[^\n]+ACM[^\n]+', text) or \
               re.search(r'http://dx\.doi\.org/10\.1145/', text) or \
               re.search(r'ACM Classification Keywords', text):
                is_acm = True
        
        if is_acm:
            acm_citations.append({
                'title': citation_title,
                'citation_count': citation_count,
                'text': text[:500]  # First 500 chars for verification
            })

print(f"ACM papers counted: {len(acm_citations)}")

if acm_citations:
    total_citations = sum(c['citation_count'] for c in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    print(f"Total citations for ACM papers: {total_citations}")
    print(f"Average citations: {avg_citations:.2f}")
    
    # Show first few examples for verification
    print("\nFirst 3 ACM papers:")
    for i, c in enumerate(acm_citations[:3], 1):
        print(f"{i}. {c['title'][:80]}... - Citations: {c['citation_count']}")
else:
    print("No ACM papers found in 2018 citations")

result = avg_citations if acm_citations else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
