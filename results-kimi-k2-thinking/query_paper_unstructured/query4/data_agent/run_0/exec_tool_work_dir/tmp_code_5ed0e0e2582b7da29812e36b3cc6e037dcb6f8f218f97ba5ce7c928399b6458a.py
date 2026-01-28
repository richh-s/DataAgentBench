code = """import json
import re
from collections import defaultdict

# Get data
citations_data = locals().get('var_functions.query_db:16', [])
paper_docs_data = locals().get('var_functions.query_db:6', [])

if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

# Build complete citation map
citation_map = defaultdict(int)
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_map[title] += count

# Check all 2016 papers with physical activity keywords
all_2016_activity_papers = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '').strip()
    text_start = text[:5000].lower()
    
    # Check for 2016 year indicators
    is_2016 = False
    if '2016' in text_start:
        is_2016 = True
    if re.search(r"chi\s*'16|ubicomp\s*'16|cscw\s*'16|dis\s*'16|pervasivehealth\s*'16", text_start):
        is_2016 = True
    
    if not is_2016:
        continue
    
    # Check for physical activity domain keywords
    keywords = ['physical activity', 'exercise', 'fitness', 'rehabilitation', 'stroke rehabilitation']
    for keyword in keywords:
        if keyword in text_start:
            all_2016_activity_papers.append({
                'title': title,
                'keyword': keyword
            })
            break

# Get citation counts for all matches
total_results = []
for paper in all_2016_activity_papers:
    title = paper['title']
    total_cites = citation_map.get(title, 0)
    total_results.append({
        'title': title,
        'total_citation_count': total_cites,
        'matched_keyword': paper['keyword']
    })

# Sort by citation count
total_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('Total 2016 physical activity papers found:', len(total_results))
for result in total_results:
    print(f"  {result['title']} - {result['total_citation_count']} citations (matched: {result['matched_keyword']})")

# Return all results without filtering
to_return = [
    {'title': r['title'], 'total_citation_count': r['total_citation_count']}
    for r in total_results
]

print('__RESULT__:')
print(json.dumps(to_return))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citation_count': 452}]}

exec(code, env_args)
