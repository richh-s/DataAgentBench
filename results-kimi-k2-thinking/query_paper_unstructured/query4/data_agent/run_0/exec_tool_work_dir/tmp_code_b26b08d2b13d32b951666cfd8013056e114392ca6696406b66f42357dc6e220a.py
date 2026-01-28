code = """import json
import re
from collections import defaultdict

# Read data
citations_file = var_functions.query_db:16
paper_docs_file = var_functions.query_db:6

if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = paper_docs_file

# Build citation totals by paper title
title_to_total_citations = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title:
        title_to_total_citations[title] += count

# Find 2016 physical activity papers
papers_2016_physical_activity = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Get title
    title = filename.replace('.txt', '').strip()
    
    # Extract year from beginning of text
    year = None
    text_start = text[:2000]
    
    # Pattern 1: Full year like 2016
    m = re.search(r'\b20(16)\b', text_start)
    if m:
        year = 2016
    else:
        # Pattern 2: CHI '16 format
        m = re.search(r"[A-Z]+\s*'?(16)\b", text_start)
        if m:
            year = 2016
    
    if year != 2016:
        continue
        
    # Check for physical activity
    text_lower = text.lower()
    if 'physical activity' not in text_lower and 'exercise' not in text_lower:
        continue
    
    papers_2016_physical_activity.append(title)

# Add citation counts
results = []
for title in papers_2016_physical_activity:
    total_cites = title_to_total_citations.get(title, 0)
    results.append({
        'title': title,
        'total_citation_count': total_cites
    })

# Sort by citation count descending
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
