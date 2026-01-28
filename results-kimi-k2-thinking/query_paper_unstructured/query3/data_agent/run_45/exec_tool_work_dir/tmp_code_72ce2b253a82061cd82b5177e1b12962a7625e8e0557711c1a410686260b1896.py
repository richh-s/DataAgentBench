code = """import json

# Access the stored data variables
citations_path = var_functions.query_db_13
papers = var_functions.query_db_12

print('citations_path type:', type(citations_path))
print('papers type:', type(papers))

# Load citations from file path
if isinstance(citations_path, str) and '.json' in citations_path:
    with open(citations_path, 'r') as f:
        citations = json.load(f)
    print('Loaded citations, sample:', citations[0] if citations else None)
else:
    citations = citations_path
    print('Citations is already data, sample:', citations[0] if citations else None)

# Check papers data
print('Papers sample:', papers[0] if papers else None)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
