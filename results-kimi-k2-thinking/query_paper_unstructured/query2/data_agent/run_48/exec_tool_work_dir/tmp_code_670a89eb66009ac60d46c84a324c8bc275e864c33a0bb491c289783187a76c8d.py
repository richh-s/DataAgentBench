code = """import json
import re

# Load the citations data for 2018
citations_2018_val = locals().get('var_functions.query_db:2', [])
if isinstance(citations_2018_val, str) and '.json' in citations_2018_val:
    with open(citations_2018_val, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_2018_val

# Load the paper documents data
paper_docs_val = locals().get('var_functions.query_db:5', [])
if isinstance(paper_docs_val, str) and '.json' in paper_docs_val:
    with open(paper_docs_val, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_val

# Create a mapping of paper titles to their publisher
paper_publishers = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Look for publisher information in the text
    # Common patterns: "ACM", "IEEE", "PubMed", etc.
    publisher = None
    
    # Search for publisher mentions
    if 'ACM' in text or 'acm' in text:
        publisher = 'ACM'
    elif 'IEEE' in text or 'ieee' in text:
        publisher = 'IEEE'
    elif 'PubMed' in text or 'pubmed' in text:
        publisher = 'PubMed'
    
    # Store the mapping
    if title and publisher:
        paper_publishers[title] = publisher

# Filter citations for ACM papers and calculate average
acm_citations = []
for cit in citations_2018:
    cit_title = cit.get('title', '')
    if cit_title in paper_publishers and paper_publishers[cit_title] == 'ACM':
        citation_count = int(cit.get('citation_count', 0))
        acm_citations.append(citation_count)

# Calculate average
average_citations = sum(acm_citations) / len(acm_citations) if acm_citations else 0

result = {
    'average_citation_count': round(average_citations, 2),
    'total_acm_papers': len(acm_citations),
    'total_citations_2018': len(citations_2018)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
