code = """import json
import re

# Access the stored results using locals()
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
print(f"Sample papers with ACM source: {[p for p in paper_info[:10] if p['source'] == 'ACM']}")

# Create a dictionary for easy lookup by title (case-insensitive)
paper_dict = {}
for paper in paper_info:
    key = paper['title'].lower().strip()
    paper_dict[key] = paper

# Match citations with papers and filter for ACM
matched_citations = []
unmatched_titles = []
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
    else:
        unmatched_titles.append(citation_title)

print(f"Matched {len(matched_citations)} ACM papers cited in 2018")
print(f"Unmatched titles (first 5): {unmatched_titles[:5]}")

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
