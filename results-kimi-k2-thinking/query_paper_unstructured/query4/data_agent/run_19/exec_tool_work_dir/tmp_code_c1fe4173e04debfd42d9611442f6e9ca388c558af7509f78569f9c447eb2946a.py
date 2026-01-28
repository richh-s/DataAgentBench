code = """import json
import re

# Load MongoDB results
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    mongo_results = json.load(f)

# Load citation data
citation_path = locals()['var_functions.query_db:6']
with open(citation_path, 'r') as f:
    citation_results = json.load(f)

# Build citation lookup dictionary
citation_dict = {}
for item in citation_results:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    citation_dict[title] = citations

# Process papers and find those from 2016 in physical activity domain
papers_2016 = []

for doc in mongo_results:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    # Check if paper is in physical activity domain
    if 'physical activity' not in text.lower():
        continue
    
    # Check for 2016 publication year
    year = None
    
    # Method 1: Look for venue + year patterns
    venue_match = re.search(r'\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp)\b[\s\S]{0,20}?\b2016\b', text, re.IGNORECASE)
    if venue_match:
        year = 2016
    
    # Method 2: Look for copyright year
    if not year and re.search(r'Copyright[\s\S]{0,50}?\b2016\b', text, re.IGNORECASE):
        year = 2016
    
    # Method 3: Count year mentions
    if not year:
        count_2016 = len(re.findall(r'\b2016\b', text))
        count_2015 = len(re.findall(r'\b2015\b', text))
        count_2017 = len(re.findall(r'\b2017\b', text))
        
        if count_2016 > count_2015 and count_2016 > count_2017:
            year = 2016
    
    if year == 2016:
        total_citations = citation_dict.get(title, 0)
        papers_2016.append({'title': title, 'total_citations': total_citations})

# Sort by citations
papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Build result string
result_parts = []
for paper in papers_2016:
    result_parts.append('Title: ' + paper['title'])
    result_parts.append('Total Citations: ' + str(paper['total_citations']))
    result_parts.append('')

result = '\n'.join(result_parts).strip()

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
