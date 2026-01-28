code = """import json, re

# Access paper documents file path
paper_docs_file = locals()['var_functions.query_db:22']

# Load data
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract info
results = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text'].lower()
    
    # Find year
    year_matches = re.findall(r'((?:19|20)\d{2})', text)
    year = max([int(y) for y in year_matches if 1900 <= int(y) <= 2030]) if year_matches else None
    
    # Check empirical
    empirical_terms = ['empirical','user study','field study','case study','experiment','evaluation','participants','interview','survey','data collection']
    venues = ['chi','ubicomp','cscw','dis','pervasivehealth','uist','iui']
    
    has_empirical = any(term in text for term in empirical_terms)
    has_venue = any(venue in text for venue in venues)
    
    if year and year > 2016 and has_empirical and has_venue:
        results.append({'title': title, 'year': year})

# Output
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': []}

exec(code, env_args)
