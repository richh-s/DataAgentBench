code = """import json
import re

# Load the 2018 citations (stored in var_functions.query_db:0)
citations_2018_path = locals()['var_functions.query_db:0']
with open(citations_2018_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents (stored in var_functions.query_db:2)
paper_docs_path = locals()['var_functions.query_db:2']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total 2018 citations: {len(citations_2018)}")
print(f"Total paper documents: {len(paper_docs)}")

# Create a mapping from paper title (without .txt) to document
paper_map = {}
for doc in paper_docs:
    if 'filename' in doc:
        title = doc['filename'].replace('.txt', '')
        paper_map[title] = doc

print(f"Mapped {len(paper_map)} papers")

# Function to extract source from paper text
def extract_source(text):
    # Look for ACM, IEEE, PubMed indicators in the text
    text_upper = text.upper()
    
    # Common patterns that indicate ACM publications
    acm_patterns = [
        'ACM ', 'ACM.', 'ACM,', 'ACM\n',
        'ASSOCIATION FOR COMPUTING MACHINERY',
        'UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW'
    ]
    
    # Check if it's an ACM publication
    for pattern in acm_patterns:
        if pattern in text_upper:
            # Additional check for IEEE to avoid false positives
            if 'IEEE' in text_upper and 'ACM' not in text_upper:
                return 'IEEE'
            return 'ACM'
    
    # Check for IEEE
    if 'IEEE' in text_upper:
        return 'IEEE'
    
    # Check for PubMed
    if 'PUBMED' in text_upper or 'NCBI' in text_upper:
        return 'PubMed'
    
    return 'Unknown'

# Extract source for each paper
paper_sources = {}
for title, doc in paper_map.items():
    if 'text' in doc:
        source = extract_source(doc['text'])
        paper_sources[title] = source

# Count sources
source_counts = {}
for source in paper_sources.values():
    source_counts[source] = source_counts.get(source, 0) + 1

print(f"Source distribution: {source_counts}")

# Find ACM papers and their 2018 citations
acm_citations = []
for citation in citations_2018:
    title = citation['title']
    if title in paper_sources and paper_sources[title] == 'ACM':
        acm_citations.append(int(citation['citation_count']))

print(f"Found {len(acm_citations)} ACM papers cited in 2018")

# Calculate average if we have data
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    print(f"Average citation count: {avg_citations:.2f}")
    
    # Prepare result
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
