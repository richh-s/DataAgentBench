code = """import json
import re

# Load papers
papers = json.load(open(var_functions.query_db:8))

# Analyze papers
papers_with_years = []
empirical_papers_all = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Try different year extraction methods
    year = None
    
    # Method 1: Look for year patterns
    year_patterns = re.findall(r"(?:'|\b)(\d{2})\b|(?:\b)(20[12]\d)\b", text)
    years_found = []
    for pattern in year_patterns:
        if pattern[0]:  # '15 format
            y = int('20' + pattern[0])
            if 2010 <= y <= 2030:
                years_found.append(y)
        elif pattern[1]:  # 2015 format
            y = int(pattern[1])
            if 2010 <= y <= 2030:
                years_found.append(y)
    
    if years_found:
        year = max(years_found)
    
    if year:
        papers_with_years.append({'title': title, 'year': year})
    
    # Check for empirical
    if 'empirical' in text.lower():
        empirical_papers_all.append({'title': title, 'year': year})

# Statistics
df_all = pd.DataFrame(papers_with_years)
df_empirical = pd.DataFrame(empirical_papers_all)

print('Total papers with years:', len(df_all))
print('Year distribution:', df_all['year'].value_counts().sort_index().to_dict())
print('Total empirical papers:', len(df_empirical))
print('Empirical year distribution:', df_empirical['year'].value_counts().sort_index().to_dict())

# Filter empirical papers after 2016
empirical_after_2016 = [p for p in empirical_papers_all if p['year'] and p['year'] > 2016]
print('Empirical papers after 2016:', len(empirical_after_2016))

if len(empirical_after_2016) > 0:
    print('Papers:', empirical_after_2016)
    result = empirical_after_2016
else:
    # Let's see empirical papers from all years to debug
    print('All empirical papers by year:')
    for y in sorted(set([p['year'] for p in empirical_papers_all if p['year']])):
        count = len([p for p in empirical_papers_all if p['year'] == y])
        print(f'  {y}: {count} papers')
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': []}

exec(code, env_args)
