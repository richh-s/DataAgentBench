code = """import json
import re

# Load data
citations_2018_file = locals()['var_functions.query_db:8']
paper_docs_file = locals()['var_functions.query_db:9']

citations_2018 = []
paper_docs = []

# Load citations
if isinstance(citations_2018_file, str) and citations_2018_file.endswith('.json'):
    with open(citations_2018_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_2018_file

# Load paper docs
if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_file

result = f"Loaded {len(citations_2018)} citations for 2018 and {len(paper_docs)} paper documents"

if citations_2018:
    result = result + f"; First citation: {citations_2018[0]}"
else:
    result = result + "; No citations loaded"
    
if paper_docs:
    result = result + f"; First paper doc filename: {paper_docs[0].get('filename', 'N/A')}"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
