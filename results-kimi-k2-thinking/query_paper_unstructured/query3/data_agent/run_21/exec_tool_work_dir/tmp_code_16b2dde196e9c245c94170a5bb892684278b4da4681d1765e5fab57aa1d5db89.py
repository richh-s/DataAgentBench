code = """import json, re

# Access stored results from previous tool calls
mongo_path = locals()['var_functions.query_db:18']
citation_path = locals()['var_functions.query_db:12']

# Load paper documents from MongoDB
with open(mongo_path, 'r') as f:
    docs = json.load(f)

# Find empirical papers published after 2016
papers = []
for doc in docs:
    try:
        filename = doc.get('filename', '')
        if not filename:
            continue
        title = filename.replace('.txt', '')
        text = doc.get('text', '')
        
        # Extract year from text
        year_match = re.search('20(1[7-9]|[2-9][0-9])', text)
        if not year_match:
            continue
        
        year = int(year_match.group())
        
        # Check for empirical contribution
        if not re.search('empirical', text, re.IGNORECASE):
            continue
            
        papers.append({'title': title, 'year': year})
    except:
        continue

# Load citation data
with open(citation_path, 'r') as f:
    cites = json.load(f)

# Calculate total citations per paper
from collections import defaultdict
citation_counts = defaultdict(int)
for c in cites:
    title = c['title']
    count = int(c['citation_count'])
    citation_counts[title] += count

# Create final result
result = []
for p in papers:
    title = p['title']
    total_citations = citation_counts.get(title, 0)
    result.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by title
result = sorted(result, key=lambda x: x['title'])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
