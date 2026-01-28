code = """import json
import re

# Load the citations data for 2018
citations_file = var_functions.query_db:0
try:
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
except TypeError:
    # If it's already a list (not a file path)
    citations_data = var_functions.query_db:0

# Load the paper documents data
papers_file = var_functions.query_db:2
try:
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
except TypeError:
    # If it's already a list (not a file path)
    papers_data = var_functions.query_db:2

print(f"Total citations in 2018: {len(citations_data)}")
print(f"Total paper documents: {len(papers_data)}")

# Extract ACM papers from the paper documents
# The hint says source can be extracted from the text, and common sources include "ACM"
acm_papers = []

for paper in papers_data:
    # Check if the text contains ACM as a source/publisher
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Look for ACM mentions that indicate it's the publisher
    # Common patterns: "ACM Classification", "ACM 2015", "ACM Classification Keywords"
    # Also look for venue information that might indicate ACM
    acm_indicators = [
        r'ACM\s+Classification',
        r'ACM\s+[^\s]+\s+\d{4}',  # ACM conference with year
        r'Permission[^.]*ACM[^.]*\.',  # ACM copyright
        r'Copyright[^.]*ACM[^.]*\.',  # ACM copyright
        r'the\s+Association\s+for\s+Computing\s+Machinery',  # ACM full name
    ]
    
    is_acm = False
    for pattern in acm_indicators:
        if re.search(pattern, text, re.IGNORECASE):
            is_acm = True
            break
    
    # Also check if it's from known ACM venues
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for ACM venues in the text
    # Common ACM venues from hints: CHI, CSCW, DIS, TEI, IUI, WWW, Ubicomp
    acm_venues = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'UbiComp', 'Ubicomp', 'Pervasive']
    
    for venue in acm_venues:
        # Look for venue mentions that might be associated with ACM
        venue_pattern = rf'{re.escape(venue)}[^\n]*\n[^\n]*ACM'
        if re.search(venue_pattern, text, re.IGNORECASE):
            is_acm = True
            break
        
        # Also check if the paper mentions it's from ACM conference
        if re.search(rf'ACM[^\n]*{re.escape(venue)}', text, re.IGNORECASE):
            is_acm = True
            break
    
    if is_acm:
        acm_papers.append({
            'title': title,
            'filename': filename,
            'text': text[:500]  # Store first 500 chars for debugging
        })

print(f"ACM papers found: {len(acm_papers)}")

# Create a mapping of titles to citation counts for 2018
citation_map = {}
for citation in citations_data:
    citation_map[citation['title']] = int(citation['citation_count'])

print(f"Papers with citations in 2018: {len(citation_map)}")

# Match ACM papers with their 2018 citations
acm_citations = []
matched_papers = []

for paper in acm_papers:
    paper_title = paper['title']
    # Exact match first
    if paper_title in citation_map:
        acm_citations.append(citation_map[paper_title])
        matched_papers.append(paper_title)
    else:
        # Try fuzzy matching - sometimes titles might have slight differences
        for citation_title, count in citation_map.items():
            # Check if titles are very similar (case-insensitive)
            if paper_title.lower() == citation_title.lower():
                acm_citations.append(count)
                matched_papers.append(paper_title)
                break
            # Or if one is a substring of the other
            elif paper_title.lower() in citation_title.lower() or citation_title.lower() in paper_title.lower():
                if len(paper_title) > 10:  # Avoid very short titles
                    acm_citations.append(count)
                    matched_papers.append(paper_title)
                    break

print(f"Matched ACM papers with 2018 citations: {len(acm_citations)}")

# Show first few matches for verification
if matched_papers:
    print("First 5 matched papers:")
    for i, title in enumerate(matched_papers[:5]):
        print(f"  {i+1}. {title} - Citations: {acm_citations[i]}")

# Calculate average citation count
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    print(f"Average citation count: {avg_citations:.2f}")
    print(f"Total citations: {sum(acm_citations)}")
else:
    print("No ACM papers found with 2018 citations")

result = {
    'total_acm_papers': len(acm_papers),
    'matched_with_citations': len(acm_citations),
    'average_citation_count': avg_citations if acm_citations else 0,
    'total_citations': sum(acm_citations) if acm_citations else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
