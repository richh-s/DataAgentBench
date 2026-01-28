code = """import json
import re
from collections import defaultdict

# Load the data from the variables
citations_data = locals().get('var_functions.query_db:16', [])
paper_docs_data = locals().get('var_functions.query_db:6', [])

# If they're strings (file paths), load the JSON
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

# Build citation mapping (title -> total citations)
citation_map = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title:
        citation_map[title] += count

# Find 2016 papers about physical activity
papers_2016_with_activity = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Title from filename
    paper_title = filename.replace('.txt', '').strip()
    
    # Check if text contains 2016
    text_start = text[:3000].lower()
    is_2016 = '2016' in text_start
    
    if not is_2016:
        # Check for venue year format
        if re.search(r"chi\s*'16|ubicomp\s*'16|cscw\s*'16|dis\s*'16", text_start):
            is_2016 = True
    
    if not is_2016:
        continue
    
    # Check for physical activity domain
    if 'physical activity' in text_start or 'exercise' in text_start:
        papers_2016_with_activity.append(paper_title)

# Match with citations and create results
results = []
for title in papers_2016_with_activity:
    total_cites = citation_map.get(title, 0)
    if total_cites > 0:  # Only include if there are citations
        results.append({
            'title': title,
            'total_citation_count': total_cites
        })

# Sort by citation count
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
