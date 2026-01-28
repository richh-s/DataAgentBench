code = """import json, os, sys

# Get the papers file path
papers_file = var_functions_query_db_40

# Get the citations file path
citations_file = var_functions_query_db_56

print('Papers file:', papers_file)
print('Citations file:', citations_file)

# Load the data
with open(papers_file, 'r') as f:
    papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

print('Loaded', len(papers), 'papers')
print('Loaded', len(citations), 'citations')

# Find food papers
food_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        text = paper.get('text', '').lower()
        if 'food' in text:
            food_papers.append(title)

# Calculate total citations
total = sum(int(c['citation_count']) for c in citations if c['title'] in food_papers)

print('Food papers:', len(food_papers))
print('Total citations:', total)
print('__RESULT__:')
print(json.dumps({'total_food_citations': total}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
