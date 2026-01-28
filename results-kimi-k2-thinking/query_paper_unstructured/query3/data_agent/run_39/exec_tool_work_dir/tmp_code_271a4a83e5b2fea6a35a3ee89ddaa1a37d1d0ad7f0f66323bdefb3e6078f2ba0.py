code = """import json
import re

# Access paper documents
paper_docs_file = locals()['var_functions.query_db:22']

# Load JSON data
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
paper_info_list = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    # Check for empirical contribution
    text_lower = text.lower()
    empirical_keywords = ['empirical', 'empirically', 'study', 'studies', 'survey', 'experiment', 
                         'evaluation', 'evaluated', 'user study', 'field study', 'case study', 
                         'participants', 'interviews', 'questionnaire', 'data collection']
    has_empirical = any(keyword in text_lower for keyword in empirical_keywords)
    
    paper_info_list.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Filter empirical papers after 2016
empirical_after_2016 = [p for p in paper_info_list if p['year'] and p['year'] > 2016 and p['has_empirical']]

print('__RESULT__:')
print(json.dumps(empirical_after_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
