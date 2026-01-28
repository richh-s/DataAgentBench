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
    
    # Check if ACM is mentioned in the text
    has_acm = False
    
    # Look for explicit ACM mentions
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        has_acm = True
    
    # Look for ACM venues and publication patterns
    if not has_acm:
        acm_venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'PervasiveHealth', 'WWW', 'OzCHI']
        for venue in acm_venues:
            if venue in text and 'Permission to make digital or hard copies' in text:
                has_acm = True
                break
    
    if has_acm:
        acm_papers.append(title)

print('Identified ACM papers:', len(acm_papers))

# Create a mapping of titles to citation counts
citation_map = {}
for item in citations_2018:
    citation_map[item['title']] = int(item['citation_count'])

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
    
    print('Average citation count for ACM papers in 2018:', round(avg_citations, 2))
    print('Total citations:', total_citations)
    print('Number of ACM papers cited:', len(matched_citations))
    
    # Show first few matches for verification
    print('\nFirst 5 matched papers:')
    for i in range(min(5, len(matched_titles))):
        print('  ' + str(i+1) + '. ' + str(matched_titles[i]) + ': ' + str(matched_citations[i]) + ' citations')
else:
    print('No matches found')
    
    # Try to find why no matches
    print('Sample citation titles:')
    cnt = 0
    for title in list(citation_map.keys())[:10]:
        print('  - ' + str(title))
        cnt += 1
    
    print('Sample ACM paper titles:')
    for i in range(min(10, len(acm_papers))):
        print('  - ' + str(acm_papers[i]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
