code = """import json, re

cit_key = 'var_functions.query_db:14'
papers_key = 'var_functions.query_db:16'

citations_var = locals()[cit_key]
papers_var = locals()[papers_key]

citations = json.load(open(citations_var)) if isinstance(citations_var, str) else citations_var
papers = json.load(open(papers_var)) if isinstance(papers_var, str) else papers_var

# Build paper lookup - extract title and source
paper_lookup = {}
for doc in papers:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename[:-4].lower().strip() if filename.endswith('.txt') else filename.lower().strip()
    
    # Determine source
    source = None
    t = text.lower()
    if 'association for computing machinery' in t or 'acm' in t:
        source = 'ACM'
    elif 'ieee' in t:
        source = 'IEEE'
    elif 'pubmed' in t or 'nih' in t:
        source = 'PubMed'
    
    paper_lookup[title] = source

# Match citations with papers and find ACM
acm_counts = []
matched = 0

for citation in citations:
    cit_title = citation.get('title', '').lower().strip()
    count = int(citation.get('citation_count', 0))
    
    if cit_title in paper_lookup:
        matched += 1
        if paper_lookup[cit_title] == 'ACM':
            acm_counts.append(count)

avg = sum(acm_counts) / len(acm_counts) if acm_counts else 0

result_str = '%.2f' % avg

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
