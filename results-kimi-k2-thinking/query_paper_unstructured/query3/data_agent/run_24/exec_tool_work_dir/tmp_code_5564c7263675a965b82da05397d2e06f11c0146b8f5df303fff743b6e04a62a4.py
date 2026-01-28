code = """import json
import re

# Read paper documents
paper_docs_path = var_functions.query_db:2
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information from documents
papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    year = None
    # Find year in venue context  
    pattern = r'CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP'
    match = re.search(pattern + r'.+?(20\d{2})', text, re.IGNORECASE)
    if match:
        year = int(match.group(1))
    
    if not year:
        year_match = re.search(r'20\d{2}', text)
        if year_match:
            year = int(year_match.group())
    
    contribution = ''
    if 'empirical' in text.lower():
        contribution = 'empirical'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Read citations  
citations_path = var_functions.query_db:3
with open(citations_path, 'r') as f:
    citations = json.load(f)

citation_sums = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    citation_sums[title] = citation_sums.get(title, 0) + count

# Filter empirical papers after 2016
results = []
for paper in papers_info:
    if paper['year'] and paper['year'] > 2016 and paper['contribution'] == 'empirical':
        title = paper['title']
        if title in citation_sums:
            results.append({
                'title': title,
                'total_citation_count': citation_sums[title]
            })

# Debug info if no results
if not results:
    debug = []
    for p in papers_info:
        if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016:
            debug.append(p['title'])
    results = {'debug_titles': debug[:10]}

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
