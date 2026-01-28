code = """import json

# Read the paper documents
with open('./var_functions.query_db:8.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citation data
with open('./var_functions.list_db:0.json', 'r') as f:
    citation_data = json.load(f)

print('Loaded', len(paper_docs), 'paper documents')
print('Loaded citation data with', len(citation_data), 'records')

# Extract titles and check for food domain
food_papers = []
for paper in paper_docs:
    title = paper['filename'].replace('.txt', '')
    # Check if text contains "food" (case-insensitive) to determine domain
    if 'food' in paper['text'].lower():
        food_papers.append(title)

print('Found', len(food_papers), 'papers related to food domain')
print('Sample food papers:', food_papers[:5])

# Now sum citations for these papers
citation_count = 0
for citation in citation_data:
    if citation['title'] in food_papers:
        citation_count += int(citation['citation_count'])

print('Total citation count for food papers:', citation_count)
print('__RESULT__:')
print(json.dumps(citation_count))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
