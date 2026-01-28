code = """import json
import re

# Load the citations data for 2018
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
    
    # Look for ACM indicators in the text (case-insensitive)
    acm_indicators = [
        'ACM Classification',
        'Association for Computing Machinery',
    ]
    
    is_acm = False
    text_lower = text.lower()
    
    # Check for copyright/permission lines mentioning ACM
    if 'permission' in text_lower and 'acm' in text_lower:
        is_acm = True
    elif 'copyright' in text_lower and 'acm' in text_lower:
        is_acm = True
    elif 'association for computing machinery' in text_lower:
        is_acm = True
    
    # Check for ACM Classification Keywords
    if 'acm classification' in text_lower:
        is_acm = True
    
    # Check for known ACM venues (if not already identified as ACM)
    if not is_acm:
        title = filename.replace('.txt', '') if filename else ''
        acm_venues = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'UbiComp', 'Ubicomp', 'Pervasive']
        
        for venue in acm_venues:
            if venue.lower() in text_lower:
                # Look for ACM near the venue mention
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if venue.lower() in line.lower():
                        # Check nearby lines for ACM
                        context = ' '.join(lines[max(0, i-2):min(len(lines), i+3)]).lower()
                        if 'acm' in context:
                            is_acm = True
                            break
                if is_acm:
                    break
    
    if is_acm:
        acm_papers.append({
            'title': filename.replace('.txt', '') if filename else '',
            'filename': filename
        })

print(f"ACM papers found: {len(acm_papers)}")

# Create a mapping of titles to citation counts for 2018
citation_map = {}
for citation in citations_data:
    citation_map[citation['title'].lower()] = int(citation['citation_count'])

print(f"Papers with citations in 2018: {len(citation_map)}")

# Match ACM papers with their 2018 citations
acm_citations = []
matched_papers = []

for paper in acm_papers:
    paper_title = paper['title'].lower()
    # Check if the exact title (case-insensitive) is in the citations
    if paper_title in citation_map:
        acm_citations.append(citation_map[paper_title])
        matched_papers.append(paper['title'])

print(f"Matched ACM papers with 2018 citations: {len(acm_citations)}")

# Show first few matches for verification
if matched_papers:
    print("First 5 matched papers:")
    for i, title in enumerate(matched_papers[:5]):
        print(f"  {i+1}. {title} - Citations: {acm_citations[i]}")

# Calculate average citation count
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    total_citations = sum(acm_citations)
    print(f"Average citation count: {avg_citations:.2f}")
    print(f"Total citations: {total_citations}")
else:
    print("No ACM papers found with 2018 citations")
    avg_citations = 0
    total_citations = 0

result = {
    'total_acm_papers': len(acm_papers),
    'matched_with_citations': len(acm_citations),
    'average_citation_count': avg_citations,
    'total_citations': total_citations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
