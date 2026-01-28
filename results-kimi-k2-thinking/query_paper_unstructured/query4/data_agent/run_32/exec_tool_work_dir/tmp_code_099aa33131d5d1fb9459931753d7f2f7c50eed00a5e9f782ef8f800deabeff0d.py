code = """import json, re

paper_docs_file = locals()['var_functions.query_db:2']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Analyze each document
analysis = []
for i, doc in enumerate(paper_docs):
    filename = doc.get('filename', '')
    text = doc.get('text', '')[:2000]  # first 2000 chars preview
    title = filename.replace('.txt', '')
    
    # Look for year patterns
    year_matches = re.findall(r'(\b(20|19)\d{2})\b', text)  # find all 4-digit years
    # Extract domains
    domain_keywords = ['physical activity', 'food', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    domains = []
    for keyword in domain_keywords:
        if keyword in text.lower():
            domains.append(keyword)
    
    analysis.append({
        'index': i,
        'title': title,
        'year_candidates': year_matches,
        'domains': domains
    })

print('__RESULT__:')
print(json.dumps(analysis, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:21': [], 'var_functions.execute_python:18': {'total_papers': 5, 'years_distribution': {}, 'papers_2016_count': 0, 'physical_activity_count': 4, 'physical_activity_2016_count': 0, 'sample_papers_2016_physical_activity': []}}

exec(code, env_args)
