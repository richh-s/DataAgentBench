code = """import json
import re

# Access the stored results - use the exact keys provided
citations_data = var_functions.query_db_0
papers_data = var_functions.query_db_8

print(f"Total citations in 2018: {len(citations_data)}")
print(f"Total paper documents: {len(papers_data)}")

# Process paper documents to extract title and source
paper_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for ACM in the text as the source/publisher
    source = None
    if re.search(r'\bACM\b', text, re.IGNORECASE):
        source = 'ACM'
    
    if title:  # Only add if we have a title
        paper_info.append({
            'title': title,
            'source': source
        })

print(f"Processed {len(paper_info)} papers with titles")

# Create a dictionary for easy lookup by title (case-insensitive)
paper_dict = {}
for paper in paper_info:
    key = paper['title'].lower().strip()
    paper_dict[key] = paper

# Match citations with papers and filter for ACM
matched_citations = []
for citation in citations_data:
    citation_title = citation.get('title', '').lower().strip()
    citation_count = int(citation.get('citation_count', 0))
    
    # Find matching paper
    if citation_title in paper_dict:
        paper = paper_dict[citation_title]
        if paper['source'] == 'ACM':
            matched_citations.append({
                'title': paper['title'],
                'citation_count': citation_count,
                'source': paper['source']
            })

print(f"Matched {len(matched_citations)} ACM papers cited in 2018")

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
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
