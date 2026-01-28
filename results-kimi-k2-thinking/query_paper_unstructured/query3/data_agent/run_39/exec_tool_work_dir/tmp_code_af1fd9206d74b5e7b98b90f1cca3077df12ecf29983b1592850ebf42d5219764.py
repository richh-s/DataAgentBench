code = """import json
import re

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:22']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Debug: Check first few papers
print('Sample papers:')
for i, doc in enumerate(paper_docs[:3]):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')[:500]
    print(f'{i+1}. {title}')
    print(f'   Text preview: {text[:100]}...')
    print()

# Process papers and extract years
papers_with_years = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year
    year = None
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)
    
    papers_with_years.append({
        'title': title,
        'year': year,
        'text_length': len(text)
    })

# Show year distribution
years = [p['year'] for p in papers_with_years if p['year'] is not None]
print(f'Year range: {min(years) if years else "N/A"} - {max(years) if years else "N/A"}')

# Count by year
from collections import Counter
year_counts = Counter(years)
print('\nTop 10 years:')
for year, count in year_counts.most_common(10):
    print(f'  {year}: {count}')

# Filter for papers after 2016
papers_after_2016 = [p for p in papers_with_years if p['year'] and p['year'] > 2016]
print(f'\nTotal papers after 2016: {len(papers_after_2016)}')

# Debug: Show sample papers after 2016
print('\nSample papers after 2016:')
for p in papers_after_2016[:5]:
    print(f"  {p['title']} ({p['year']})")

# Check for empirical indicators
empirical_papers_after_2016 = []
for p in papers_after_2016:
    for doc in paper_docs:
        if doc['filename'].replace('.txt', '') == p['title']:
            text = doc.get('text', '').lower()
            empirical_terms = ['empirical','user study','field study','case study','experiment','evaluation',
                             'participants','interview','survey','data collection','we conducted']
            if any(term in text for term in empirical_terms):
                empirical_papers_after_2016.append(p['title'])
            break

print(f'\nEmpirical papers after 2016: {len(empirical_papers_after_2016)}')
print('List:', empirical_papers_after_2016[:10])

result = {
    'papers_after_2016': len(papers_after_2016),
    'empirical_after_2016': empirical_papers_after_2016,
    'sample_papers': papers_after_2016[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': []}

exec(code, env_args)
