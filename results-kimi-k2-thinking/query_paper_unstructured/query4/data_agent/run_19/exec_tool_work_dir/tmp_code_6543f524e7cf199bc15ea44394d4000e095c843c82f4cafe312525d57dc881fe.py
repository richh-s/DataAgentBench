code = """import json, re

# Load data
mongo_path = locals()['var_functions.query_db:26']
with open(mongo_path) as f:
    papers = json.load(f)

citation_path = locals()['var_functions.query_db:6']
with open(citation_path) as f:
    citation_data = json.load(f)

# Build citation lookup
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['total_citations'])

# Find 2016 papers
result = []

for doc in papers:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for 2016 in various patterns
    year = None
    
    # Copyright pattern
    m = re.search(r'Copyright.{0,100}?(2016)', text)
    if m:
        year = 2016
    
    # Conference pattern
    if not year:
        m = re.search(r'\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp)\b.{0,20}?\b2016\b', text, re.IGNORECASE)
        if m:
            year = 2016
    
    # If year is 2016, add to results
    if year == 2016:
        citations = citation_dict.get(title, 0)
        result.append({'title': title, 'total_citations': citations})

# Sort by citations descending
result.sort(key=lambda x: x['total_citations'], reverse=True)

# Format result as simple string
out = ''
for r in result:
    out += 'Title: ' + r['title'] + '\n'
    out += 'Total Citations: ' + str(r['total_citations']) + '\n\n'

# Remove trailing newlines
out = out.strip()

print('__RESULT__:')
print(out)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
