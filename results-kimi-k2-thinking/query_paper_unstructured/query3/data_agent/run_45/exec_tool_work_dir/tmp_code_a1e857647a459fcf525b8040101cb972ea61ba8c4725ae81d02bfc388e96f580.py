code = """# Let's see what variables are available
import json
import os

# Get the variable names to understand the pattern
all_vars = list(globals().keys()) + list(locals().keys())
db_vars = [v for v in all_vars if 'query_db' in v]
print('Available variables:', db_vars)

# Look for our specific variables
papers_var = None
citations_var = None
for var in db_vars:
    if ':12' in var:
        papers_var = var
    elif ':13' in var:
        citations_var= var

print('papers var:', papers_var)
print('citations var:', citations_var)

# Access them using the proper names
if papers_var:
    papers_data = globals().get(papers_var) or locals().get(papers_var)
    print('papers_data type:', type(papers_data))
    if isinstance(papers_data, str) and '.json' in papers_data:
        with open(papers_data, 'r') as f:
            papers = json.load(f)
        print('Loaded papers:', len(papers))
    else:
        papers = papers_data
        print('Papers data (first 2):', papers[:2] if papers else 'None')

if citations_var:
    citations_data = globals().get(citations_var) or locals().get(citations_var)
    print('citations_data type:', type(citations_data))
    if isinstance(citations_data, str) and '.json' in citations_data:
        with open(citations_data, 'r') as f:
            citations = json.load(f)
        print('Loaded citations:', len(citations))
    else:
        citations = citations_data
        print('Citations data (first 2):', citations[:2] if citations else 'None')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
