code = """import json
import re

# Access paper documents
paper_docs_file = locals()['var_functions.query_db:22']

# Load JSON data
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Process all papers
all_papers = []
empirical_papers = []

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
    
    # Check for empirical contribution more broadly
    text_lower = text.lower()
    empirical_indicators = [
        'empirical', 'empirically',
        'user study', 'user studies',
        'field study', 'field studies', 
        'case study', 'case studies',
        'experiment', 'experiments', 'experimental',
        'evaluation', 'evaluated', 'evaluating',
        'participants', 'subjects',
        'interview', 'interviews', 'interviewed',
        'survey', 'questionnaire',
        'data collection', 'we collected', 'we gathered',
        'we conducted', 'we performed'
    ]
    
    # Also check if it's from a venue that typically publishes empirical work
    venue_indicators = ['chi', 'ubicomp', 'cscw', 'dis', 'pervasivehealth', 'uist', 'iui']
    text_lower_venue = text.lower()
    has_venue = any(venue in text_lower_venue for venue in venue_indicators)
    
    has_empirical_terms = any(term in text_lower for term in empirical_indicators)
    
    is_empirical = has_empirical_terms and has_venue
    
    paper_info = {
        'title': title,
        'year': year,
        'is_empirical': is_empirical,
        'year_matches': year_matches[:3] if year_matches else []
    }
    
    all_papers.append(paper_info)
    if is_empirical:
        empirical_papers.append(paper_info)

# Statistics
print('=== STATISTICS ===')
print(f'Total papers: {len(all_papers)}')
print(f'Empirical papers (total): {len(empirical_papers)}')

# Check year distribution
years = [p['year'] for p in all_papers if p['year'] is not None]
print(f'Year range: {min(years) if years else "N/A"} - {max(years) if years else "N/A"}')

# Show empirical papers after 2016
empirical_after_2016 = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
print(f'Empirical papers after 2016: {len(empirical_after_2016)}')

# Show top years for empirical papers
empirical_years = [p['year'] for p in empirical_papers if p['year']]
year_dist = {}
for year in empirical_years:
    year_dist[year] = year_dist.get(year, 0) + 1

print('\nEmpirical papers by year (top 10):')
for year, count in sorted(year_dist.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'  {year}: {count}')

# Show some empirical papers after 2016
print('\nSample empirical papers after 2016:')
for p in empirical_after_2016[:10]:
    print(f"  {p['title']} ({p['year']})")

result_data = {
    'total_papers': len(all_papers),
    'empirical_total': len(empirical_papers),
    'empirical_after_2016': empirical_after_2016,
    'empirical_after_2016_count': len(empirical_after_2016)
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'status': 'info', 'count': 5, 'sample_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:18': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': []}

exec(code, env_args)
