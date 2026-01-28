code = """import json

# Open the two result files
try:
    with open('var_functions.query_db:18', 'r') as f:
        citations_2018 = json.load(f)
except:
    citations_2018 = []

try:
    with open('var_functions.query_db:20', 'r') as f:
        paper_docs = json.load(f)
except:
    paper_docs = []

print('Citations 2018:', len(citations_2018))
print('Paper docs:', len(paper_docs))

# Identify ACM papers from documents
acm_paper_titles = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if this is an ACM paper
    is_acm = False
    
    # Method 1: Direct ACM mention
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        is_acm = True
    
    # Method 2: ACM venue with copyright
    if not is_acm:
        venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'PervasiveHealth', 'WWW', 'OzCHI']
        for venue in venues:
            if venue in text and 'Permission to make digital or hard copies' in text:
                is_acm = True
                break
    
    # Method 3: ACM DOI pattern
    if not is_acm:
        if '10.1145' in text or '978-1-4503' in text:
            is_acm = True
    
    if is_acm:
        acm_paper_titles.append(title)

print('ACM papers:', len(acm_paper_titles))

# Map citation titles to counts
citation_dict = {}
for citation in citations_2018:
    citation_dict[citation['title']] = int(citation['citation_count'])

# Find matching papers
matched_citations = []
for paper_title in acm_paper_titles:
    if paper_title in citation_dict:
        matched_citations.append(citation_dict[paper_title])

print('Matched papers:', len(matched_citations))

# Calculate average
if matched_citations:
    average = sum(matched_citations) / len(matched_citations)
    result = {
        'average_citations': round(average, 2),
        'total_papers': len(matched_citations),
        'total_citations': sum(matched_citations)
    }
else:
    result = {
        'average_citations': 0,
        'total_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
