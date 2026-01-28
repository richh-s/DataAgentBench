code = """import json
import re

# Access the stored results
citations_key = 'var_functions.query_db:0'
papers_key = 'var_functions.query_db:8'

citations_data = locals()[citations_key]
papers_data = locals()[papers_key]

# Handle file paths if results are stored as files
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)
        
if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        papers_data = json.load(f)

print(f"Total citations in 2018: {len(citations_data)}")
print(f"Total paper documents: {len(papers_data)}")

# Process paper documents to extract title and source - more robust approach
paper_info = []
acm_papers = []
for i, paper in enumerate(papers_data):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for ACM in the text as the source/publisher - more patterns
    source = None
    # Check for various ACM indicators
    acm_patterns = [
        r'\bACM\b',
        r'ACM Classification',
        r'ACM Digital Library',
        r'Permission to make digital or hard copies.*ACM',
        r'Copyright.*ACM'
    ]
    
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            source = 'ACM'
            acm_papers.append(title)
            break
    
    if title:  # Only add if we have a title
        paper_info.append({
            'title': title,
            'source': source,
            'filename': filename
        })

print(f"Processed {len(paper_info)} papers with titles")
print(f"Found {len(acm_papers)} papers with ACM as source")
print(f"Sample ACM papers: {acm_papers[:10]}")

# Create a dictionary for easy lookup by title with normalization
def normalize_title(title):
    """Normalize title for matching"""
    return re.sub(r'[^a-zA-Z0-9]', '', title.lower().strip())

paper_dict = {}
for paper in paper_info:
    key = normalize_title(paper['title'])
    paper_dict[key] = paper

print(f"Paper dictionary has {len(paper_dict)} entries")

# Match citations with papers and filter for ACM - with better matching
matched_citations = []
unmatched_citations = []

for citation in citations_data:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Normalize citation title
    citation_key = normalize_title(citation_title)
    
    # Find matching paper
    if citation_key in paper_dict:
        paper = paper_dict[citation_key]
        if paper['source'] == 'ACM':
            matched_citations.append({
                'title': paper['title'],
                'citation_count': citation_count,
                'source': paper['source']
            })
        else:
            unmatched_citations.append({
                'citation_title': citation_title,
                'paper_title': paper['title'],
                'source': paper['source'],
                'reason': 'Not ACM'
            })
    else:
        unmatched_citations.append({
            'citation_title': citation_title,
            'reason': 'No matching paper found'
        })

print(f"Matched {len(matched_citations)} ACM papers cited in 2018")
print(f"Unmatched citations: {len(unmatched_citations)}")

# Show some examples of unmatched citations
print("Sample unmatched citations:")
for i, uc in enumerate(unmatched_citations[:5]):
    print(f"  {i+1}. {uc}")

# Calculate average citation count
if matched_citations:
    total_citations = sum(c['citation_count'] for c in matched_citations)
    avg_citations = total_citations / len(matched_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers': len(matched_citations),
        'total_citations': total_citations
    }
else:
    # Let's check if we have any citations at all
    total_citation_counts = sum(int(c.get('citation_count', 0)) for c in citations_data)
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0,
        'note': f'Found {len(citations_data)} total citations in 2018, but none from ACM papers',
        'total_citation_count_all': total_citation_counts
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'average_citation_count': 0, 'total_acm_papers': 0, 'total_citations': 0}}

exec(code, env_args)
