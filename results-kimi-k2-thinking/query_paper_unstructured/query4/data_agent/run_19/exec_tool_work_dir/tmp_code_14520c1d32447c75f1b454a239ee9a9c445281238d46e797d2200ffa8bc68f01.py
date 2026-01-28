code = """import json
import re

# Load MongoDB results - the key is var_functions.query_db:2
mongo_path = locals()['var_functions.query_db:2']

# Load the file
with open(mongo_path, 'r') as f:
    mongo_results = json.load(f)

# Load citation data - the key is var_functions.query_db:6
citation_path = locals()['var_functions.query_db:6']
with open(citation_path, 'r') as f:
    citation_results = json.load(f)

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
    # Check for 2016 in venue patterns
    if re.search(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp).{0,5}2016', text, re.IGNORECASE):
        year = 2016
    # Check for copyright 2016
    elif re.search(r'Copyright.{0,50}2016', text):
        year = 2016
    # Check for proceedings 2016
    elif re.search(r'Proceedings.{0,50}2016', text):
        year = 2016
    
    # If not found by patterns, check year frequency
    if not year:
        y2016 = len(re.findall(r'\b2016\b', text))
        y2015 = len(re.findall(r'\b2015\b', text))
        y2017 = len(re.findall(r'\b2017\b', text))
        if y2016 > y2015 and y2016 > y2017:
            year = 2016
    
    if year == 2016:
        total_citations = citation_dict.get(title, 0)
        papers_2016.append({'title': title, 'total_citations': total_citations})

# Sort by citations descending
papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Format output
output_lines = []
for paper in papers_2016:
    line = 'Title: ' + paper['title'] + ' | Total Citations: ' + str(paper['total_citations'])
    output_lines.append(line)

result = '\n'.join(output_lines) if output_lines else 'No papers found'

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
