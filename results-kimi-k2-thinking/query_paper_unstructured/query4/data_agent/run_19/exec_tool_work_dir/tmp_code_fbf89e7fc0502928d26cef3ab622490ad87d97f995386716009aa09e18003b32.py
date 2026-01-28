code = """import json, re

# Load data
mongo_path = locals()['var_functions.query_db:2']
citation_path = locals()['var_functions.query_db:6']

with open(mongo_path) as f:
    mongo = json.load(f)

with open(citation_path) as f:
    citations = json.load(f)

# Build citation lookup
cite_dict = {item['title']: int(item['total_citations']) for item in citations}

# Find 2016 physical activity papers
papers = []

for doc in mongo:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    if not title or 'physical activity' not in text.lower():
        continue
    
    # Check for 2016
    y2016 = len(re.findall(r'\b2016\b', text))
    y2015 = len(re.findall(r'\b2015\b', text))
    y2017 = len(re.findall(r'\b2017\b', text))
    
    if y2016 > 0 and y2016 >= y2015 and y2016 >= y2017:
        total_cites = cite_dict.get(title, 0)
        papers.append([title, total_cites])

# Sort by citations
papers.sort(key=lambda x: x[1], reverse=True)

# Format output
result = []
for p in papers:
    result.append({'title': p[0], 'total_citations': p[1]})

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
