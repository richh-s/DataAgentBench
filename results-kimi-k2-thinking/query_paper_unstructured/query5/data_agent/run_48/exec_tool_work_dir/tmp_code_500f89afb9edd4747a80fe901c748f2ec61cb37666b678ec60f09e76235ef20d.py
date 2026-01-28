code = """import json
import re

# Load the citation data for 2020 from the stored result
citation_file = var_functions.query_db:0
if isinstance(citation_file, str) and citation_file.endswith('.json'):
    with open(citation_file, 'r') as f:
        citation_data = json.load(f)
else:
    citation_data = citation_file

# Load the paper documents data from the stored result  
paper_file = var_functions.query_db:5
if isinstance(paper_file, str) and paper_file.endswith('.json'):
    with open(paper_file, 'r') as f:
        paper_data = json.load(f)
else:
    paper_data = paper_file

print(f"Loaded {len(citation_data)} citation records for 2020")
print(f"Loaded {len(paper_data)} paper documents")

# Look for CHI venue patterns in paper texts
chi_papers = []
venue_patterns = [
    r"CHI\s*'\d{2}.*\n",  # CHI '15 style
    r"CHI\s*\d{4}\s*",    # CHI 2015 style
    r"\s+CHI\s+.*\d{4}",  # ACM CHI format
    r"Conference on Human Factors in Computing Systems"  # Full name
]

for paper in paper_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Check if text contains CHI venue information
    is_chi = False
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        # Extract title from filename (remove .txt)
        title = filename.replace('.txt', '') if filename else ''
        chi_papers.append({
            'title': title,
            'filename': filename,
            'venue': 'CHI'
        })

print(f"Found {len(chi_papers)} papers from CHI venue")

# Create a set of CHI paper titles for fast lookup
chi_titles_set = set()
chi_titles_map = {}

for paper in chi_papers:
    title = paper['title'].lower().strip()
    chi_titles_set.add(title)
    chi_titles_map[title] = paper['title']
    
    # Also add variations without punctuation
    title_clean = re.sub(r'[^\w\s]', '', title)
    chi_titles_set.add(title_clean)
    chi_titles_map[title_clean] = paper['title']

# Match citations with CHI papers and sum citation counts
total_citations = 0
matched_citations = []
unmatched_count = 0

for citation in citation_data:
    citation_title = citation.get('title', '').lower().strip()
    citation_count = int(citation.get('citation_count', 0))
    
    # Check for exact match
    if citation_title in chi_titles_set:
        total_citations += citation_count
        matched_citations.append({
            'title': citation.get('title'),
            'citation_count': citation_count,
            'venue': 'CHI'
        })
    else:
        # Check for cleaned version match
        citation_clean = re.sub(r'[^\w\s]', '', citation_title)
        if citation_clean in chi_titles_set:
            total_citations += citation_count
            matched_citations.append({
                'title': citation.get('title'),
                'citation_count': citation_count,
                'venue': 'CHI'
            })
        else:
            unmatched_count += 1

print(f"Matches found: {len(matched_citations)}")
print(f"Total citations for CHI papers in 2020: {total_citations}")
print(f"Unmatched citations: {unmatched_count}")

# Show sample matched papers
print("\nSample of matched CHI papers:")
for i, paper in enumerate(matched_citations[:5]):
    print(f"  {paper['title']}: {paper['citation_count']} citations")

# Return the final answer
result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(matched_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
