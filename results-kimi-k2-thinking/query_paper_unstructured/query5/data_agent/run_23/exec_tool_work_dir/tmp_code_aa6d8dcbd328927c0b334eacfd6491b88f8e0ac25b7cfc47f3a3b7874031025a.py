code = """import json

# Load the 2020 citations data
citations_2020_path = var_functions.query_db:5
with open(citations_2020_path, 'r') as f:
    citations_2020 = json.load(f)

print(f"Total 2020 citations records: {len(citations_2020)}")
print(f"First few records: {citations_2020[:3]}")

# Extract titles from 2020 citations
titles_2020 = [c['title'] for c in citations_2020]
print(f"Number of unique titles in 2020 citations: {len(set(titles_2020))}")

# Load the paper docs data
paper_docs_path = var_functions.query_db:9
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")
print(f"First paper doc: {paper_docs[0]['filename'] if paper_docs else 'No papers'}")"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
