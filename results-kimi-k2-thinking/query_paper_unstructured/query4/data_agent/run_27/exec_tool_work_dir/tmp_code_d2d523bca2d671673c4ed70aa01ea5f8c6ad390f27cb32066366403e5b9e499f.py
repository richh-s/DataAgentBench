code = """import json
import re

# Access the storage variable
file_path = locals()['var_functions.query_db:2']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Extract papers and look for years and domains
papers = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    year_match = re.search(r'\b(20[12][0-9])\b', text[:2000])  # Look only in first part to avoid references
    year = int(year_match.group(1)) if year_match else None
    
    # Check for physical activity domain
    text_lower = text.lower()
    has_physical_activity = 'physical activity' in text_lower
    
    if title and has_physical_activity:
        papers.append({
            'title': title,
            'year': year,
            'filename': filename
        })

# Filter for 2016 papers
papers_2016 = [p for p in papers if p['year'] == 2016]

result_json = json.dumps({
    'total_physical_activity_papers': len(papers),
    'papers_2016': papers_2016,
    'count_2016': len(papers_2016)
})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:14': {'year_distribution': {}, 'physical_activity_papers_by_year': {}, 'counts_by_year': {}}}

exec(code, env_args)
