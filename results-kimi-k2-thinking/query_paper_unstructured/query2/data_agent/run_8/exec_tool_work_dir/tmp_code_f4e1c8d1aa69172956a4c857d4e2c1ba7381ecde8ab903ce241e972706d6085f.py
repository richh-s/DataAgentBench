code = """import json

# Load the 2018 citations data
citations_2018_path = 'var_functions.query_db:18'
with open(citations_2018_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents
paper_docs_path = 'var_functions.query_db:20'
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded {} citations from 2018'.format(len(citations_2018)))
print('Loaded {} paper documents'.format(len(paper_docs)))

# Identify ACM papers from the documents
acm_papers = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for ACM indicators
    is_acm = False
    
    # Explicit ACM mentions
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        is_acm = True
    
    # ACM venues with copyright notice
    if not is_acm:
        acm_venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'PervasiveHealth', 'WWW', 'OzCHI', 'AH']
        for venue in acm_venues:
            if venue in text and 'Permission to make digital or hard copies' in text:
                is_acm = True
                break
    
    # ACM digital library pattern
    if not is_acm:
        if 'http://dx.doi.org/10.1145/' in text or '978-1-4503-' in text:
            is_acm = True
    
    if is_acm:
        acm_papers.append(title)

print('Identified {} ACM papers'.format(len(acm_papers)))

# Map citation titles to counts
citation_map = {}
for item in citations_2018:
    citation_map[item['title']] = int(item['citation_count'])

# Match ACM papers with 2018 citations
matched_citations = []
matched_titles = []

for paper_title in acm_papers:
    if paper_title in citation_map:
        matched_citations.append(citation_map[paper_title])
        matched_titles.append(paper_title)

print('Found {} ACM papers cited in 2018'.format(len(matched_citations)))

if matched_citations:
    total_citations = sum(matched_citations)
    avg_citations = total_citations / len(matched_citations)
    
    print('\n=== RESULTS ===')
    print('Average citation count: {:.2f}'.format(avg_citations))
    print('Total citations: {}'.format(total_citations))
    print('Number of ACM papers: {}'.format(len(matched_citations)))
    
    # Sample matches
    print('\nSample matched papers:')
    for i in range(min(5, len(matched_titles))):
        print('  {}. {}: {} citations'.format(i+1, matched_titles[i], matched_citations[i]))
    
    result = {
        'average_citations': round(avg_citations, 2),
        'total_citations': total_citations,
        'num_papers': len(matched_citations)
    }
    
    print('\n__RESULT__:')
    print(json.dumps(result))
else:
    print('No matches found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
