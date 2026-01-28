code = """import json
import re
import pandas as pd

# Load paper documents
paper_docs_var = locals()['var_functions.query_db:14']
if isinstance(paper_docs_var, str):
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

# Load citation totals
citations_var = locals()['var_functions.query_db:17']
if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_var

# Build citation lookup
citation_lookup = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('total_citations', 0))
    citation_lookup[title] = count

print('Processing', len(paper_docs), 'papers with', len(citation_lookup), 'citation records')

# Find 2016 physical activity papers
results = []
activity_keywords = ['physical activity', 'fitness', 'exercise', 'steps', 'walking', 
                    'running', 'workout', 'activit', 'fitbit', 'stroke', 'rehabilitation']

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check publication year
    year_match = re.search(r'20(1[0-9]|20)', text)
    year = int(year_match.group()) if year_match else None
    
    # Check physical activity domain
    lower_text = text.lower()
    is_activity = False
    for kw in activity_keywords:
        if kw in lower_text:
            is_activity = True
            break
    
    if year == 2016 and is_activity and title:
        total_cites = citation_lookup.get(title, 0)
        results.append({
            'title': title,
            'total_citation_count': total_cites
        })
        print(f'Paper: {title} = {total_cites} citations')

# Sort by citation count
results = sorted(results, key=lambda x: x['total_citation_count'], reverse=True)

result_str = json.dumps(results)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:26': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citation_count': 96}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
