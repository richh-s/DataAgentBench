code = """import json
import re

# Access the storage variable - stored as a file path
file_path = locals()['var_functions.query_db:2']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Debug: Let's see what papers we have and their years
year_counts = {}
papers_with_years = []

domain_indicators = [
    'physical activity', 'activity tracking', 'fitness', 'exercise', 
    'steps', 'walking', 'running', 'workout', 'physical', 'fitness'
]

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 4-digit year patterns (2010-2025)
    year_match = re.search(r'\b(20[12][0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    text_lower = text.lower()
    is_physical_activity = any(indicator in text_lower for indicator in domain_indicators)
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        if is_physical_activity:
            papers_with_years.append({
                'title': title,
                'year': year,
                'domain': 'physical activity'
            })

# Filter for 2016 physical activity papers
papers_2016 = [p for p in papers_with_years if p['year'] == 2016]

result = {
    'year_distribution': year_counts,
    'physical_activity_papers_by_year': {}
}

# Group physical activity papers by year
for paper in papers_with_years:
    yr = paper['year']
    if yr not in result['physical_activity_papers_by_year']:
        result['physical_activity_papers_by_year'][yr] = []
    result['physical_activity_papers_by_year'][yr].append(paper['title'])

# Count papers for each year
result['counts_by_year'] = {yr: len(titles) for yr, titles in result['physical_activity_papers_by_year'].items()}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
