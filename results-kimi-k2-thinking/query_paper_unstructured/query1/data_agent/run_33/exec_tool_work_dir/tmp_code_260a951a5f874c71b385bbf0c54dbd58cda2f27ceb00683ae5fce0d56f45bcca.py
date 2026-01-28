code = """import json

# Load papers from file path
papers_path = 'paper_docs_database_papers.json'
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except:
    papers = []

# Load citations from file path
citations_path = 'citations_database_citations.json'
try:
    with open(citations_path, 'r') as f:
        citations = json.load(f)
except:
    citations = []

if not papers or not citations:
    print('Using storage variables')
    papers = query_db_56_data
    citations = query_db_57_data

print('Papers count:', len(papers))
print('Citations count:', len(citations))

# Extract food paper titles
food_titles = set()
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        text = paper.get('text', '').lower()
        if 'food' in text or 'diet' in text:
            food_titles.add(title)

print('Food papers:', len(food_titles))

# Sum citations for food papers
total = sum(int(c.get('citation_count', 0)) for c in citations if c.get('title') in food_titles)

result = {'total_food_citations': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
