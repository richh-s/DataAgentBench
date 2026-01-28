code = """import json
import re

# Access papers data
paper_docs_key = 'var_functions.query_db:2'
paper_docs_path = locals()[paper_docs_key]

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
def extract_paper_info(text, filename):
    title = filename.replace('.txt', '') if filename else ''
    
    year_matches = re.findall(r'(19|20)\d{2}', text)
    year = None
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2025]
        if valid_years:
            year = max(valid_years)
    
    text_lower = text.lower()
    domains = []
    
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains.append('physical activity')
    if 'food' in text_lower or 'diet' in text_lower:
        domains.append('food')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'mood' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower:
        domains.append('finances')
    if 'location' in text_lower:
        domains.append('location')
    
    return title, year, domains

papers = []
for doc in paper_docs:
    title, year, domains = extract_paper_info(doc.get('text', ''), doc.get('filename', ''))
    if title and year and domains:
        papers.append({'title': title, 'year': year, 'domains': domains})

# Filter for 2016 physical activity papers
papers_2016_physical_activity = []
for paper in papers:
    if paper['year'] == 2016 and 'physical activity' in paper['domains']:
        papers_2016_physical_activity.append(paper['title'])

print('Total papers analyzed:', len(papers))
print('2016 physical activity papers:', len(papers_2016_physical_activity))
print(papers_2016_physical_activity[:5])

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
