code = """import json
import re

# Load the citation data for 2020
citation_data = []
with open('/tmp/tmp_jp8x6g8q.json', 'r') as f:
    citation_data = json.load(f)

print(f"Loaded {len(citation_data)} citation records for 2020")

# Load the paper documents data
paper_data = []
with open('/tmp/tmp_61gt6v5d.json', 'r') as f:
    paper_data = json.load(f)

print(f"Loaded {len(paper_data)} paper documents")

# Extract venue information from paper texts
# Look for venue patterns like: CHI '15, CHI 2015, CHI'15, etc.
chi_papers = []
venue_pattern = r"CHI\s*'?(\d{2})'?\s*(\d{4})?|\bCHI\b"

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

# Create a dictionary for quick lookup of CHI papers by title
chi_paper_titles = {paper['title'].lower().strip(): paper for paper in chi_papers}

# Match citations with CHI papers and sum citation counts
total_citations = 0
matched_citations = []

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

print(f"Found {len(matched_citations)} citations matching CHI papers")
print(f"Total citation count for CHI papers in 2020: {total_citations}")

# Also check for partial matches (in case of slight differences)
partial_matches = []
for citation in citation_data:
    citation_title = citation.get('title', '').lower().strip()
    citation_count = int(citation.get('citation_count', 0))
    
    # Check for partial matches if not already matched
    if citation_title not in chi_paper_titles:
        for chi_title in chi_paper_titles.keys():
            # Check if one is contained in the other
            if citation_title in chi_title or chi_title in citation_title:
                # Verify it's a meaningful match (not just common words)
                if len(citation_title) > 10 and len(chi_title) > 10:
                    partial_matches.append({
                        'citation_title': citation.get('title'),
                        'chi_title': chi_paper_titles[chi_title]['title'],
                        'citation_count': citation_count
                    })
                    break

print(f"Found {len(partial_matches)} potential partial matches")

# Print results in required format
result = {
    'total_citation_count': total_citations,
    'matched_papers_count': len(matched_citations),
    'sample_matched_papers': matched_citations[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
