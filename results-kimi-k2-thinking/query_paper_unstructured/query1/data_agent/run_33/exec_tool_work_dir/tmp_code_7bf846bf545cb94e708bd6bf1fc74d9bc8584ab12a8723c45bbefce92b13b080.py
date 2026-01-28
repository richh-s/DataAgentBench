code = """import json

# Access papers from the most recent query result
papers_path = 'paper_docs_query.json'
citations_path = 'citations_query.json'

# Try to load from files first
try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
except:
    papers = []

try:
    with open(citations_path, 'r') as f:
        citations = json.load(f)
except:
    citations = []

# Check for data in accessible form
if not papers:
    papers = query_db_result_56 if 'query_db_result_56' in locals() else []

if not citations:
    citations = query_db_result_57 if 'query_db_result_57' in locals() else []

print('Loaded papers:', len(papers))
print('Loaded citations:', len(citations))

# List available variables to see what's accessible
print('Available variables containing query results:')
for key in locals():
    if 'query' in key.lower() or 'result' in key.lower():
        print(f'  {key}: {type(locals()[key])}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
