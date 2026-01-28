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

# Count records
print('Total citations in 2018: ' + str(len(citations_data)))
print('Total paper documents: ' + str(len(papers_data)))

# Extract ACM papers from the paper documents
acm_papers = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    text_lower = text.lower()
    
    # Check for ACM copyright/permission indicators
    is_acm = False
    if 'permission' in text_lower and 'acm' in text_lower:
        is_acm = True
    elif 'copyright' in text_lower and 'acm' in text_lower:
        is_acm = True
    elif 'association for computing machinery' in text_lower:
        is_acm = True
    elif 'acm classification' in text_lower:
        is_acm = True
    
    # For known ACM venues, check proximity to ACM mention
    if not is_acm:
        title = filename.replace('.txt', '') if filename else ''
        acm_venues = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW', 'UbiComp', 'Ubicomp', 'Pervensive']
        
        for venue in acm_venues:
            if venue.lower() in text_lower:
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if venue.lower() in line.lower():
                        context_lines = lines[max(0, i-2):min(len(lines), i+3)]
                        context = ' '.join(context_lines).lower()
                        if 'acm' in context:
                            is_acm = True
                            break
                if is_acm:
                    break
    
    if is_acm:
        paper_title = filename.replace('.txt', '') if filename else ''
        acm_papers.append({'title': paper_title, 'filename': filename})

print('ACM papers found: ' + str(len(acm_papers)))

# Create a mapping of titles to citation counts for 2018 (case-insensitive)
citation_map = {}
for citation in citations_data:
    citation_map[citation['title'].lower()] = int(citation['citation_count'])

print('Papers with citations in 2018: ' + str(len(citation_map)))

# Match ACM papers with their 2018 citations (case-insensitive exact match)
acm_citations = []
matched_papers = []

for paper in acm_papers:
    paper_title_lower = paper['title'].lower()
    if paper_title_lower in citation_map:
        acm_citations.append(citation_map[paper_title_lower])
        matched_papers.append(paper['title'])

print('Matched ACM papers with 2018 citations: ' + str(len(acm_citations)))

# Show first few matches
if matched_papers:
    print('First 5 matched papers:')
    for i in range(min(5, len(matched_papers))):
        print('  ' + str(i+1) + '. ' + matched_papers[i] + ' - Citations: ' + str(acm_citations[i]))

# Calculate average citation count
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    total_citations = sum(acm_citations)
    print('Average citation count: ' + str(round(avg_citations, 2)))
    print('Total citations: ' + str(total_citations))
else:
    avg_citations = 0
    total_citations = 0
    print('No ACM papers found with 2018 citations')

result = {
    'total_acm_papers': len(acm_papers),
    'matched_with_citations': len(acm_citations),
    'average_citation_count': avg_citations,
    'total_citations': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
