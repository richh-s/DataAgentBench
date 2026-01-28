code = """import json

# Load all paper documents from MongoDB
with open('/tmp/tmp_result_14.json', 'r') as f:
    papers = json.load(f)

# Load all citations from SQLite
with open('/tmp/tmp_result_12.json', 'r') as f:
    citations = json.load(f)

# Extract paper titles from MongoDB (removing .txt extension)
paper_titles = {}
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    paper_titles[title] = {
        'filename': filename,
        'text': paper['text']
    }

print('Total papers loaded: ' + str(len(papers)))
print('Total citations loaded: ' + str(len(citations)))
print('First 5 paper titles: ' + str(list(paper_titles.keys())[:5]))
print('First 5 citations: ' + str([c['title'] for c in citations[:5]]))

# Look for food-related papers
food_papers = []
for title, paper_info in paper_titles.items():
    text = paper_info['text'].lower()
    # Check if domain is food (look for food keywords, but be careful about false positives)
    # Look for 'food' as a standalone word or in context of research domain
    if ' food ' in text or 'food,' in text or 'food.' in text or 'food;' in text or ':food' in text:
        # Check if it's in a research context (not just random mention)
        # Look for domain indicators
        domain_indicators = ['domain', 'tracking', 'self-tracking', 'informatics', 'research', 'study']
        if any(indicator in text for indicator in domain_indicators):
            food_papers.append(title)

print('')
print('Potential food papers found: ' + str(len(food_papers)))
for i, title in enumerate(food_papers[:10]):
    print('  ' + str(i+1) + '. ' + title)

result = {
    'total_papers': len(papers),
    'total_citations': len(citations),
    'potential_food_papers': len(food_papers),
    'sample_food_papers': food_papers[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:10': ['paper_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
