code = """# Debug: Check available variables and their types
import json

# Try different ways to access the variables
all_keys = [k for k in locals().keys() if k.startswith('var_functions')]
print('Available var_functions keys:', all_keys)

# Access citations data
cit_key = 'var_functions.query_db:5'
if cit_key in locals():
    citations = locals()[cit_key]
    print('Citations type:', type(citations))
    print('Citations length:', len(citations))
    print('First citation:', citations[0] if citations else 'No citations')
else:
    print('Citations key not found')

# Access papers data  
papers_key = 'var_functions.query_db:2'
if papers_key in locals():
    papers_data = locals()[papers_key]
    print('\nPapers data type:', type(papers_data))
    if isinstance(papers_data, str):
        print('Papers data is a file path:', papers_data)
else:
    print('Papers key not found')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
