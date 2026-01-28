code = """import json
import re

# Read the citations data for 2018
citations_file = var_functions.query_db:0
citations_data = json.load(open(citations_file))

# Read the paper documents
papers_file = var_functions.query_db:2
papers_data = json.load(open(papers_file))

# Create a dictionary to store paper title to source mapping
paper_sources = {}

# Extract source from each paper document
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Look for source information in the text
    # Common patterns: "ACM", "IEEE", "PubMed"
    source = None
    
    # Check for ACM
    if 'ACM' in text or 'acm' in text:
        source = 'ACM'
    # Check for IEEE
    elif 'IEEE' in text or 'ieee' in text:
        source = 'IEEE'
    # Check for PubMed
    elif 'PubMed' in text or 'pubmed' in text:
        source = 'PubMed'
    
    # Also check for more specific patterns
    if not source:
        # Look for copyright notices, publication info
        acm_patterns = [
            r'ACM\s+[\w\s]+\d{4}',
            r'ACM\s+Classification',
            r'Permission.*ACM',
            r'Copyright.*ACM'
        ]
        
        ieee_patterns = [
            r'IEEE\s+[\w\s]+\d{4}',
            r'Copyright.*IEEE',
            r'IEEE\s+Transactions'
        ]
        
        for pattern in acm_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                source = 'ACM'
                break
        
        if not source:
            for pattern in ieee_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    source = 'IEEE'
                    break
    
    if source:
        paper_sources[title] = source

# Create a mapping of titles to citation counts for 2018
citation_counts = {}
for citation in citations_data:
    title = citation['title']
    count = int(citation['citation_count'])
    citation_counts[title] = count

# Find papers published by ACM that have citation data in 2018
acm_citations = []
matched_papers = []

for title, source in paper_sources.items():
    if source == 'ACM' and title in citation_counts:
        acm_citations.append(citation_counts[title])
        matched_papers.append({
            'title': title,
            'citation_count': citation_counts[title],
            'source': source
        })

# Calculate average citation count for ACM papers
if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citation, 2),
        'total_acm_papers_with_citations': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_with_citations': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
