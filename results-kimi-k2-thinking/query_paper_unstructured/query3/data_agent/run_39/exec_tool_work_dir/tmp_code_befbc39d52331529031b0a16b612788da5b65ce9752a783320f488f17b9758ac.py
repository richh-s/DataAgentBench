code = """import json
import re

# Get the paper documents variable
paper_docs_var = locals()['var_functions.query_db:22']

# Load the paper documents
if isinstance(paper_docs_var, str) and '.json' in paper_docs_var:
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

print('Total paper documents:', len(paper_docs))

# Extract information from each paper document
paper_info_list = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 4-digit years between 1900-2030
    year = None
    year_matches = re.findall(r"(?:\b|')((?:19|20)\d{2})\b", text)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 1900 <= int(y) <= 2030]
        if valid_years:
            year = max(valid_years)  # Most recent year is likely publication year
    
    # Determine contribution type by keyword matching
    contribution = []
    text_lower = text.lower()
    
    # Define keywords for empirical contribution
    empirical_keywords = ['empirical', 'empirically', 'study', 'studies', 'survey', 'experiment', 'experiments', 
                         'evaluation', 'evaluated', 'user study', 'field study', 'case study', 'participants', 
                         'interviews', 'questionnaire', 'data collection', 'we conducted', 'we collected']
    
    has_empirical = any(keyword in text_lower for keyword in empirical_keywords)
    if has_empirical:
        contribution.append('empirical')
    
    paper_info_list.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'contribution': contribution
    })

# Show statistics
years = [p['year'] for p in paper_info_list if p['year'] is not None]
print(f'Year range: {min(years) if years else "N/A"} - {max(years) if years else "N/A"}')

# Count papers by year
year_counts = {}
for year in years:
    year_counts[year] = year_counts.get(year, 0) + 1

print('\nTop years:')
for year in sorted(year_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'  {year[0]}: {year[1]}')

# Count empirical papers
empirical_papers = [p for p in paper_info_list if p['has_empirical']]
print(f'\nTotal empirical papers: {len(empirical_papers)}')

# Filter papers after 2016 with empirical contribution
empirical_after_2016 = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
print(f'Empirical papers after 2016: {len(empirical_after_2016)}')

# If none found, show debug info
if not empirical_after_2016:
    print('\nDebug - All papers with year > 2016:')
    all_after_2016 = [p for p in paper_info_list if p['year'] and p['year'] > 2016]
    print(f'Total papers after 2016: {len(all_after_2016)}')
    
    print('\nSample papers after 2016:')
    for p in all_after_2016[:5]:
        print(f"  {p['title']} ({p['year']}) - Empirical: {p['has_empirical']}")

result = {
    'total_papers': len(paper_info_list),
    'empirical_papers_total': len(empirical_papers),
    'empirical_after_2016': empirical_after_2016,
    'all_after_2016_count': len([p for p in paper_info_list if p['year'] and p['year'] > 2016])
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
