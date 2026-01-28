code = """import json
import re

# Load papers
papers_path = locals()['var_functions.query_db:28']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Loaded', len(papers), 'papers')

# Check year distribution
year_counts = {}
empirical_counts = {}

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Find all years in first 2000 chars
    years = re.findall(r'(\b20\d{2}\b)', text[:2000])
    
    for year in years:
        year_int = int(year)
        year_counts[year_int] = year_counts.get(year_int, 0) + 1
        
        # Check if empirical in same paper
        if 'empirical' in text.lower():
            empirical_counts[year_int] = empirical_counts.get(year_int, 0) + 1

# Show year distribution
print('\nYear distribution:')
sorted_years = sorted(year_counts.items())
for year, count in sorted_years:
    empirical = empirical_counts.get(year, 0)
    print(f'{year}: {count} papers ({empirical} empirical)')

# Check if we have any papers after 2016
total_after_2016 = sum(count for year, count in year_counts.items() if year > 2016)
empirical_after_2016 = sum(count for year, count in empirical_counts.items() if year > 2016)

print(f'\nTotal papers after 2016: {total_after_2016}')
print(f'Empirical papers after 2016: {empirical_after_2016}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': []}

exec(code, env_args)
