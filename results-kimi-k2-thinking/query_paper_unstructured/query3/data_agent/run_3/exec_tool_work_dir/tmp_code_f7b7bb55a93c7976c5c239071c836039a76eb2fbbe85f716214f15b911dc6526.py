code = """import json
import re

# Load paper documents
papers_path = locals()['var_functions.query_db:28']
print("Paper docs path:", papers_path)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Debug first few papers
print('Total papers:', len(papers))
print('\nFirst 3 papers analysis:')

for i in range(min(3, len(papers))):
    p = papers[i]
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    print('\n--- Paper', i+1, ':', filename, '---')
    
    # Extract title
    title = filename.replace('.txt', '')
    print('Title:', title)
    
    # Extract year
    year_match = re.search(r'(\b20\d{2}\b)', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    print('Year:', year)
    
    # Check for contribution types
    text_lower = text.lower()
    keywords = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
    found_keywords = []
    for kw in keywords:
        if kw in text_lower:
            # Find context
            idx = text_lower.find(kw)
            context = text[max(0, idx-50):idx+50]
            found_keywords.append((kw, context))
    
    print('Found contribution keywords:', len(found_keywords))
    for kw, ctx in found_keywords:
        print(f'  {kw}: ...{ctx}...')

# Let's search more broadly in all papers for recent empirical papers
print('\n\n=== Searching all papers ===')
empirical_recent = []
all_keywords = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    if not text or not filename:
        continue
    
    # Extract year
    year_match = re.search(r'(\b20\d{2}\b)', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    if year and year > 2016:
        text_lower = text.lower()
        if 'empirical' in text_lower:
            title = filename.replace('.txt', '')
            empirical_recent.append(title)
            
            # Track all keywords in this paper
            keywords = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
            found = [kw for kw in keywords if kw in text_lower]
            all_keywords.extend(found)

print('Found', len(empirical_recent), 'recent empirical papers')
print('Keyword frequencies:', {kw: all_keywords.count(kw) for kw in set(all_keywords)})

# Show some examples
if empirical_recent:
    print('\nSample empirical papers after 2016:')
    for i, title in enumerate(empirical_recent[:5]):
        print(i+1, title)
else:
    print('\nNo empirical papers found after 2016')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': []}

exec(code, env_args)
