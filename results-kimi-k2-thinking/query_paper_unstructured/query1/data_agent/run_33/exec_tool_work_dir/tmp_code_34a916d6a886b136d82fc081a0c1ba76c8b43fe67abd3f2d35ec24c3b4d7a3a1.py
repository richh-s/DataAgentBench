code = """import json

# Load papers from file path stored in previous result
papers_path = query_db_56  # This should be the file path
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations from file path stored in previous result
citations_path = query_db_57  # This should be the file path  
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Papers:', len(papers))
print('Citations:', len(citations))

# Extract food paper titles
food_titles = []
for paper in papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        text = paper.get('text', '').lower()
        # Check for food domain
        if 'food' in text or 'diet' in text or 'nutrition' in text:
            food_titles.append(title)

# Sum citations for food papers
food_titles_set = set(food_titles)
total = sum(int(c.get('citation_count', 0)) for c in citations if c.get('title') in food_titles_set)

print('Total food citations:', total)
print('__RESULT__:')
print(json.dumps({'total_food_citations': total}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
