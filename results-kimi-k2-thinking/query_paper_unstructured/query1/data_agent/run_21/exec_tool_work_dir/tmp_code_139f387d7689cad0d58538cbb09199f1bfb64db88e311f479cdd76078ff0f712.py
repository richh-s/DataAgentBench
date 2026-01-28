code = """import json

# Load all papers from MongoDB
with open('/tmp/tmp_result_36.json', 'r') as f:
    papers = json.load(f)

print('Loaded ' + str(len(papers)) + ' papers')

# Find food domain papers
food_papers = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text'].lower()
    
    # Check if this is about food tracking/domain
    # Look for multiple mentions or specific patterns
    if 'food' in text:
        food_mentions = text.count('food')
        # Look for context that indicates food is a domain being studied
        if food_mentions > 2 or 'track food' in text or 'food tracking' in text:
            food_papers.append(title)

food_papers = list(set(food_papers))  # Remove duplicates
print('Food papers: ' + str(len(food_papers)))

result = {
    'food_papers': food_papers,
    'count': len(food_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:10': ['paper_docs'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:34': {'food_papers_count': 0, 'citations_count': 0, 'files_checked': []}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
