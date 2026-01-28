code = """import json

# Load the data
citations_var = locals()['var_functions.query_db:0']
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

papers_var = locals()['var_functions.query_db:2']
if isinstance(papers_var, str) and papers_var.endswith('.json'):
    with open(papers_var, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_var

print('Total citations in 2018: ' + str(len(citations_data)))
print('Total paper documents: ' + str(len(papers_data)))

# Extract ACM papers - look for ACM mentions
acm_papers = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Simple check for ACM mentions
    text_lower = text.lower()
    has_acm = 'acm' in text_lower
    has_association = 'association for computing machinery' in text_lower
    
    # Check for ACM venues
    venue_indicators = ['chi', 'cscw', 'dis', 'tei', 'iui', 'www', 'ubicomp', 'pervasive']
    has_acm_venue = any(venue in text_lower for venue in venue_indicators)
    
    if has_acm or has_association or (has_acm_venue and has_acm):
        paper_title = filename.replace('.txt', '') if filename else ''
        if paper_title:  # Only add if we have a title
            acm_papers.append({'title': paper_title, 'filename': filename})

print('ACM papers found: ' + str(len(acm_papers)))

# Create citation map (case-insensitive)
citation_map = {}
for citation in citations_data:
    citation_map[citation['title'].lower()] = int(citation['citation_count'])

print('Papers with 2018 citations: ' + str(len(citation_map)))

# Match papers with citations
acm_citation_counts = []
matched_titles = []

for paper in acm_papers:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        acm_citation_counts.append(citation_map[title_lower])
        matched_titles.append(paper['title'])

print('Matched ACM papers with 2018 citations: ' + str(len(acm_citation_counts)))

if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
    total_citations = sum(acm_citation_counts)
    print('Average citation count: ' + str(round(avg_citations, 2)))
    print('Total citations: ' + str(total_citations))
    print('First 3 matches:')
    for i in range(min(3, len(matched_titles))):
        print('  - ' + matched_titles[i] + ': ' + str(acm_citation_counts[i]) + ' citations')
else:
    avg_citations = 0
    total_citations = 0
    print('No matches found')

result = {
    'total_acm_papers': len(acm_papers),
    'matched_papers': len(acm_citation_counts),
    'average_citations': round(avg_citations, 2),
    'total_citations': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
