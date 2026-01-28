code = """import json
import re

# Load paper documents from MongoDB
mongo_path = var_functions.query_db:18
with open(mongo_path, 'r') as f:
    paper_docs = json.load(f)

# Extract empirical papers published after 2016
empirical_papers = []
for doc in paper_docs:
    try:
        # Get title from filename
        filename = doc.get('filename', '')
        if not filename:
            continue
        title = filename.replace('.txt', '')
        
        # Check if text exists
        text = doc.get('text', '')
        if not text:
            continue
            
        # Extract year - look for 4-digit year patterns
        year_match = re.search(r'20(1[7-9]|[2-9][0-9])', text)
        if not year_match:
            continue
        year = int(year_match.group())
        
        # Check for empirical contribution (case-insensitive)
        if not re.search(r'\bempirical\b', text, re.IGNORECASE):
            continue
            
        empirical_papers.append({'title': title, 'year': year})
        
    except Exception:
        continue

# Load citation data
citation_path = var_functions.query_db:12
with open(citation_path, 'r') as f:
    citations = json.load(f)

# Create citations lookup dictionary
citation_dict = {}
for cit in citations:
    title = cit['title']
    count = int(cit['citation_count'])
    if title in citation_dict:
        citation_dict[title] += count
    else:
        citation_dict[title] = count

# Join papers with citations
result = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_dict.get(title, 0)
    result.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by title for consistent output
result = sorted(result, key=lambda x: x['title'])

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
