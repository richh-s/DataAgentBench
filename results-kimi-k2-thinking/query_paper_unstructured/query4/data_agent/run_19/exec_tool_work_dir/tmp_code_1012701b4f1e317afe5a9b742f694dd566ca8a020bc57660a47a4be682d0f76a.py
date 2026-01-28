code = """import json
import re

# Load MongoDB results
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    mongo_results = json.load(f)

# Load citation data
citation_path = locals()['query_db:6']
if isinstance(citation_path, str):
    with open(citation_path, 'r') as f:
        citation_results = json.load(f)
else:
    citation_results = citation_path

# Build citation lookup dictionary
citation_dict = {}
for item in citation_results:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    citation_dict[title] = citations

# Process papers
papers_2016 = []

for doc in mongo_results:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title or 'physical activity' not in text.lower():
        continue
    
    year = None
    # Check for 2016 patterns
    patterns = [
        r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp).{0,5}2016',
        r'Copyright.{0,50}2016',
        r'Proceedings.{0,50}2016'
    ]
    
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            year = 2016
            break
    
    # If not found by patterns, check year frequency
    if not year:
        y2016 = len(re.findall(r'\b2016\b', text))
        y2015 = len(re.findall(r'\b2015\b', text))
        y2017 = len(re.findall(r'\b2017\b', text))
        if y2016 > max(y2015, y2017):
            year = 2016
    
    if year == 2016:
        total_citations = citation_dict.get(title, 0)
        papers_2016.append({'title': title, 'total_citations': total_citations})

# Sort by citations descending
papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare output
output = []
for paper in papers_2016:
    output.append({'title': paper['title'], 'total_citations': paper['total_citations']})

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
