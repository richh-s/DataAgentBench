code = """import json
import re

# Load paper documents
paper_docs_path = locals()['var_functions.query_db:28']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print('Sample paper analysis:')
for i, doc in enumerate(paper_docs[:3]):
    text = doc['text']
    filename = doc['filename']
    print('\n=== Paper', i+1, ':', filename, '===')
    
    # Show first 500 chars to see structure
    print(text[:500])
    
    # Count frequency of contribution keywords
    text_lower = text.lower()
    keywords = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
    found = [k for k in keywords if k in text_lower]
    print('Found keywords:', found)

# Let's also check some papers after 2016 more specifically
print('\n\n=== Papers potentially after 2016 ===')
recent_papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Look for recent years
    year_match = re.search(r'(\b20(1[7-9]|20)\b)', text[:2000])
    if year_match:
        year = int(year_match.group(1))
        if year > 2016:
            print('\n', filename, '- Year:', year)
            text_lower = text.lower()
            if 'empirical' in text_lower:
                print('  HAS EMPIRICAL KEYWORD')
                recent_papers.append({'title': filename.replace('.txt', ''), 'year': year})

print('\nFound', len(recent_papers), 'papers after 2016 with empirical keyword')
if recent_papers:
    print('\nTop 5:')
    for i, paper in enumerate(recent_papers[:5]):
        print(i+1, paper['title'], '(', paper['year'], ')')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': []}

exec(code, env_args)
