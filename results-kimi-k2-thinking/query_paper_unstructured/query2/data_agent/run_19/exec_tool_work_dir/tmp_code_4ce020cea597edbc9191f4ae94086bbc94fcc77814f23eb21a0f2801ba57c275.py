code = """import json

# Load the citations data
citations_file_path = var_functions.query_db:2
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Load the paper docs data  
papers_file_path = var_functions.query_db:4
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Create a dictionary to store paper titles and their extracted metadata
paper_metadata = {}

for paper in papers_data:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract metadata from text
    text = paper['text']
    
    # Look for source/publisher information
    source = None
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    # Look for venue information (common HCI venues)
    venue = None
    text_upper = text.upper()
    venues = ['CHI', 'UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 'WWW', 'IUI', 'OZCHI', 'TEI', 'AH']
    for v in venues:
        if v in text_upper:
            venue = v
            break
    
    # Look for year
    year = None
    # Common patterns for years in academic papers
    import re
    year_matches = re.findall(r'(?:19|20)\d{2}', text)
    if year_matches:
        # Take the most recent year that looks like a publication year
        for y in year_matches:
            y_int = int(y)
            if 1900 <= y_int <= 2025:
                year = y_int
                break
    
    paper_metadata[title] = {
        'source': source,
        'venue': venue,
        'year': year
    }

# Now match citations with paper metadata
acm_citations = []
for citation in citations_data:
    title = citation['title']
    citation_count = int(citation['citation_count'])
    
    # Try to find matching paper
    if title in paper_metadata:
        metadata = paper_metadata[title]
        if metadata['source'] == 'ACM':
            acm_citations.append(citation_count)
    else:
        # Try partial matching
        for paper_title, metadata in paper_metadata.items():
            if metadata['source'] == 'ACM':
                # Check if the citation title is a substring of paper title or vice versa
                if title.lower() in paper_title.lower() or paper_title.lower() in title.lower():
                    acm_citations.append(citation_count)
                    break

# Calculate average
average_citation = sum(acm_citations) / len(acm_citations) if acm_citations else 0

result = {
    "total_citations_2018": len(citations_data),
    "acm_papers_cited": len(acm_citations),
    "average_citation_count": round(average_citation, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
