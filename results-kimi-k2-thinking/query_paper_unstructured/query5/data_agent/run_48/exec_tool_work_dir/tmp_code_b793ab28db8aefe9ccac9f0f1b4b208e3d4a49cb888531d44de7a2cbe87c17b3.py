code = """import json
import re

# Access the stored data from previous tool calls
citation_data = var_functions.query_db:0
paper_data = var_functions.query_db:5

# Handle the case where data might be stored in files vs. directly in variables
if isinstance(citation_data, str) and citation_data.endswith('.json'):
    with open(citation_data, 'r') as f:
        citation_data = json.load(f)

if isinstance(paper_data, str) and paper_data.endswith('.json'):
    with open(paper_data, 'r') as f:
        paper_data = json.load(f)

print(f"Loaded {len(citation_data)} citation records")
print(f"Loaded {len(paper_data)} paper documents")

# Look for CHI venue patterns in paper texts
chi_papers = []
venue_pattern = r"CHI\s*'?(\d{2})'?\s*(\d{4})?|\bCHI\b|\bCHI\s+\d{4}\b"

for paper in paper_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Check if text contains CHI venue information
    if re.search(venue_pattern, text, re.IGNORECASE):
        # Extract title from filename (remove .txt)
        title = filename.replace('.txt', '') if filename else ''
        chi_papers.append({
            'title': title,
            'filename': filename,
            'venue': 'CHI'
        })

print(f"Found {len(chi_papers)} papers from CHI venue")

# Create a dictionary for quick lookup of CHI papers by title (normalized)
chi_paper_titles = {}
for paper in chi_papers:
    title = paper['title'].lower().strip()
    chi_paper_titles[title] = paper
    
    # Also add version without common punctuation
    title_clean = re.sub(r'[^\w\s]', '', title)
    chi_paper_titles[title_clean] = paper

# Match citations with CHI papers and sum citation counts
total_citations = 0
matched_citations = []
unmatched_citations = []

for citation in citation_data:
    citation_title = citation.get('title', '').lower().strip()
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if this citation matches a CHI paper
    if citation_title in chi_paper_titles:
        total_citations += citation_count
        matched_citations.append({
            'title': citation.get('title'),
            'citation_count': citation_count,
            'venue': 'CHI'
        })
    else:
        # Try matching with cleaned version (no punctuation)
        citation_clean = re.sub(r'[^\w\s]', '', citation_title)
        if citation_clean in chi_paper_titles:
            total_citations += citation_count
            matched_citations.append({
                'title': citation.get('title'),
                'citation_count': citation_count,
                'venue': 'CHI'
            })
        else:
            unmatched_citations.append({
                'title': citation.get('title'),
                'citation_count': citation_count
            })

print(f"Found {len(matched_citations)} citations matching CHI papers")
print(f"Total citation count for CHI papers in 2020: {total_citations}")

# Show a few sample matched papers
print("\nSample matched CHI papers:")
for i, match in enumerate(matched_citations[:5]):
    print(f"  {i+1}. {match['title']}: {match['citation_count']} citations")

# Print results in required format
result = {
    'total_citation_count': total_citations,
    'matched_papers_count': len(matched_citations),
    'unmatched_citations_count': len(unmatched_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
