code = """import json
import re

# Load the citation data for 2018
citations_2018_file = var_functions.query_db:8
citations_2018 = []
if isinstance(citations_2018_file, str) and citations_2018_file.endswith('.json'):
    with open(citations_2018_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_2018_file

# Load the paper documents
paper_docs_file = var_functions.query_db:9
paper_docs = []
if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_file

print(f"Loaded {len(citations_2018)} citations for 2018")
print(f"Loaded {len(paper_docs)} paper documents")

# Let's see the structure of the data
if citations_2018:
    print(f"\nFirst citation: {citations_2018[0]}")
if paper_docs:
    print(f"\nFirst paper doc keys: {list(paper_docs[0].keys())}")
    print(f"First paper doc filename: {paper_docs[0].get('filename', 'N/A')}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
