code = """import json
import re

# Read the papers data
papers_file = var_functions.query_db:12
with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Find papers from 2016 in physical activity domain
papers_2016_pa = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    # Extract year - look for 2016 in text
    year = None
    # Check first 30 lines for year
    lines = text.split('\n')[:30]
    for line in lines:
        # Look for 2016 specifically
        if '2016' in line:
            year = 2016
            break
        # Also check for other year patterns
        year_matches = re.findall(r'20\d{2}', line)
        for y in year_matches:
            if y == '2016':
                year = 2016
                break
        if year:
            break
    
    if year != 2016:
        continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    title_lower = title.lower()
    
    # Physical activity keywords
    pa_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 
                   'step count', 'activity tracking', 'walking', 'running', 
                   'sports', 'fitbit', 'fitness tracking']
    
    is_physical_activity = False
    # If title contains physical activity terms, it's likely in that domain
    for kw in pa_keywords:
        if kw in title_lower:
            is_physical_activity = True
            break
    
    # If not in title, check if mentioned multiple times in text
    if not is_physical_activity:
        count = sum(1 for kw in pa_keywords if kw in text_lower)
        if count >= 3:  # At least 3 mentions
            is_physical_activity = True
    
    if is_physical_activity:
        papers_2016_pa.append(title)

print(f"Found {len(papers_2016_pa)} papers from 2016 in physical activity domain")
for title in papers_2016_pa:
    print(f"  - {title}")

result = {'titles': papers_2016_pa, 'count': len(papers_2016_pa)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
