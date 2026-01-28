code = """import json

# Load the papers data
# Get the file path from the previous query result
papers_file_path = var_functions.query_db_56

# Read papers from the JSON file
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Citations data should already be in storage from the last query
citations_key = 'var_functions.query_db:57'
nested = locals()

citations = nested[citations_key] if citations_key in nested else []

# If citations is empty, check if it's a file path
if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('Papers loaded:', len(papers))
print('Citations loaded:', len(citations))

# Create food paper list
food_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        text = paper.get('text', '').lower()
        if 'food' in text or 'calorie' in text or 'nutrition' in text:
            food_papers.append(title)

print('Food papers:', len(food_papers))

# Calculate total citations
total = sum(int(citation.get('citation_count', 0)) for citation in citations if citation.get('title') in food_papers)

result = {'total_food_citations': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
