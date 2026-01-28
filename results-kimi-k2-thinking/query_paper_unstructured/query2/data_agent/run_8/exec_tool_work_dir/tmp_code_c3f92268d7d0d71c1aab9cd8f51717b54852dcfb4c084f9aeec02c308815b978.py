code = """import pandas as pd

# Access the query results from storage
citations_2018 = locals()['var_functions.query_db:0']
paper_docs = locals()['var_functions.query_db:2']

print('Total citations in 2018:', len(citations_2018))
print('Total paper documents:', len(paper_docs))

# Extract ACM papers from paper_docs
acm_papers = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check if ACM is mentioned
    has_acm = False
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        has_acm = True
    else:
        acm_venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'PervasiveHealth', 'WWW', 'OzCHI']
        for venue in acm_venues:
            if venue in text and 'Permission to make digital or hard copies' in text:
                has_acm = True
                break
    
    if has_acm:
        acm_papers.append(title)

print('Identified ACM papers:', len(acm_papers))

# Map titles to citation counts
citation_map = {item['title']: int(item['citation_count']) for item in citations_2018}

# Match ACM papers with citations
matched_citations = []
matched_titles = []

for paper_title in acm_papers:
    if paper_title in citation_map:
        matched_citations.append(citation_map[paper_title])
        matched_titles.append(paper_title)

print('Matched ACM papers with 2018 citations:', len(matched_citations))

if matched_citations:
    total_citations = sum(matched_citations)
    avg_citations = total_citations / len(matched_citations)
    
    result = {
        'average_citations': round(avg_citations, 2),
        'total_citations': total_citations,
        'num_papers': len(matched_citations),
        'sample_papers': [{'title': matched_titles[i], 'citations': matched_citations[i]} for i in range(min(5, len(matched_titles)))]
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('No matches found')
    result = {'average_citations': 0, 'message': 'No ACM papers found in 2018 citations'}
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
