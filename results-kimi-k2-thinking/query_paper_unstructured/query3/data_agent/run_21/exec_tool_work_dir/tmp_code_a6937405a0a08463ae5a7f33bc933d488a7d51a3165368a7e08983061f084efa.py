code = """import json, re

# Load paper documents
with open(var_functions.query_db:18, 'r') as f:
    docs = json.load(f)

# Find empirical papers after 2016
papers = []
for doc in docs:
    try:
        title = doc['filename'].replace('.txt', '')
        text = doc.get('text', '')
        year_match = re.search('20(1[7-9]|[2-9][0-9])', text)
        if year_match and re.search('empirical', text, re.IGNORECASE):
            papers.append({'title': title, 'year': int(year_match.group())})
    except:
        pass

# Load citations
with open(var_functions.query_db:12, 'r') as f:
    cites = json.load(f)

# Sum citations
from collections import defaultdict
citation_counts = defaultdict(int)
for c in cites:
    citation_counts[c['title']] += int(c['citation_count'])

# Merge
result = []
for p in papers:
    result.append({
        'title': p['title'],
        'total_citation_count': citation_counts.get(p['title'], 0)
    })

result = sorted(result, key=lambda x: x['title'])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
