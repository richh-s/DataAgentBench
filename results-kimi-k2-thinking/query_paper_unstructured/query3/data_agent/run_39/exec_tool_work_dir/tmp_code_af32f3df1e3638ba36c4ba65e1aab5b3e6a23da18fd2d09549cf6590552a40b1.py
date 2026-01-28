code = """import json
import re

# Get the paper documents
paper_docs_var = locals()['var_functions.query_db:6']
if isinstance(paper_docs_var, str) and '.json' in paper_docs_var:
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

# Process all papers with debug info
def extract_paper_info_debug(doc):
    filename = doc['filename']
    text = doc['text']
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    if year_matches:
        years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if years:
            year = max(years)
    
    # Extract contribution
    contribution = []
    text_lower = text.lower()
    
    contribution_keywords = {
        'empirical': ['empirical', 'empirically', 'study', 'studies', 'survey', 'experiment', 'experiments', 'evaluation', 'evaluated', 'user study', 'field study', 'case study', 'participants', 'interviews', 'questionnaire', 'data collection'],
        'artifact': ['artifact', 'system', 'tool', 'prototype', 'implementation', 'design', 'architecture'],
        'theoretical': ['theory', 'theoretical', 'framework', 'model', 'conceptual', 'taxonomy'],
        'survey': ['survey', 'literature review', 'systematic review', 'meta-analysis'],
        'methodological': ['method', 'methodology', 'methodological', 'approach', 'technique']
    }
    
    for contrib_type, keywords in contribution_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            contribution.append(contrib_type)
    
    contribution = list(set(contribution))
    
    return {
        'title': title,
        'year': year,
        'contribution': contribution,
        'year_matches': year_matches[:5] if year_matches else []
    }

# Process all papers
debug_info = [extract_paper_info_debug(doc) for doc in paper_docs]

# Show stats
years = [p['year'] for p in debug_info if p['year'] is not None]
print('Year range:', min(years) if years else 'None', '-', max(years) if years else 'None')
print('Papers by year:')
for year in sorted(set(years))[-10:]:
    print(f'  {year}: {sum(1 for p in debug_info if p["year"] == year)}')

print('\nContribution types:')
all_contributions = []
for p in debug_info:
    all_contributions.extend(p['contribution'])
for contrib in set(all_contributions):
    print(f'  {contrib}: {all_contributions.count(contrib)}')

# Check papers after 2016
papers_after_2016 = [p for p in debug_info if p['year'] and p['year'] > 2016]
print(f'\nPapers after 2016: {len(papers_after_2016)}')

# Check empirical papers after 2016
empirical_after_2016 = [p for p in papers_after_2016 if 'empirical' in p['contribution']]
print(f'Empirical papers after 2016: {len(empirical_after_2016)}')

# If none, show some samples of empirical papers
empirical_all = [p for p in debug_info if 'empirical' in p['contribution']]
print(f'\nAll empirical papers: {len(empirical_all)}')
if empirical_all:
    print('Sample empirical papers:')
    for p in empirical_all[:5]:
        print(f'  {p["title"]} ({p["year"]}): {p["contribution"]}')

print('__RESULT__:')
print(json.dumps(debug_info[:10]))  # Return first 10 for inspection"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': []}

exec(code, env_args)
