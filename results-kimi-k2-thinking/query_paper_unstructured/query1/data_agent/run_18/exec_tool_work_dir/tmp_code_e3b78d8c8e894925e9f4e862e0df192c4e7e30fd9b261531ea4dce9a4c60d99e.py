code = """import json
import re

# Load the citations data (direct list)
citations_data = locals()['var_functions.query_db:3']

# Load the paper documents data from the file
papers_file_path = locals()['var_functions.query_db:7']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Convert citation_count to integer for proper aggregation
for citation in citations_data:
    citation['citation_count'] = int(citation['citation_count'])

print('__RESULT__:')
print(json.dumps({
    'citations_count': len(citations_data),
    'papers_count': len(papers_data),
    'sample_citations': citations_data[:3],
    'sample_papers': papers_data[:1]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
