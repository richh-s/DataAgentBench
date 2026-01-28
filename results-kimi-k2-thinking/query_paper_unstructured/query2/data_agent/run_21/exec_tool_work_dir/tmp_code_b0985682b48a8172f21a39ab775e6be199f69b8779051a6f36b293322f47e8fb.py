code = """import json
import re

# Load the citations data for 2018 using locals() to handle special characters in variable names
citations_var = locals()['var_functions.query_db:0']
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

# Load the paper documents data
papers_var = locals()['var_functions.query_db:2']
if isinstance(papers_var, str) and papers_var.endswith('.json'):
    with open(papers_var, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_var

print(f"Total citations in 2018: {len(citations_data)}")
print(f"Total paper documents: {len(papers_data)}")

# Extract ACM papers from the paper documents
acm_papers = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Look for ACM indicators in the text
    acm_indicators = [
        r'ACM\s+Classification',
        r'Permission[^.]*ACM[^.]*\.',  # ACM copyright
        r'Copyright[^.]*ACM[^.]*\.',  # ACM copyright
        r'the\s+Association\s+for\s+Computing\s+Machinery',  # ACM full name
    ]
    
    is_acm = False
    for pattern in acm_indicators:
        if re.search(pattern, text, re.IGNORECASE):
            is_acm = True
            break
    
    # Check for ACM venues
    title = filename.replace('.txt', '') if filename else ''
    acm_venues = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'UbiComp', 'Ubicomp', 'Pervasive']
    
    if not is_acm:
        for venue in acm_venues:
            # Look for venue with ACM reference
            venue_pattern = rf'{re.escape(venue)}[^\n]*\n[^\n]*ACM'
            if re.search(venue_pattern, text, re.IGNORECASE):
                is_acm = True
                break
    
    if is_acm:
        acm_papers.append({
            'title': title,
            'filename': filename
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
    # Exact match (case-insensitive)
    for citation_title, count in citation_map.items():
        if paper_title.lower() == citation_title.lower():
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
    avg_citations = 0

result = {
    'total_acm_papers': len(acm_papers),
    'matched_with_citations': len(acm_citations),
    'average_citation_count': avg_citations,
    'total_citations': sum(acm_citations) if acm_citations else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
