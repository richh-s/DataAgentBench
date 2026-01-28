code = """import json

# Load the papers data from JSON file
papers_file_path = 'paper_docs_results.json'
citations_file_path = 'citations_results.json'

# Load papers
try:
    with open(papers_file_path, 'r') as f:
        papers = json.load(f)
    print(f'Loaded {len(papers)} papers')
except FileNotFoundError:
    print(f'Papers file not found, reading from storage')
    papers = []

# Load citations  
try:
    with open(citations_file_path, 'r') as f:
        citations = json.load(f)
    print(f'Loaded {len(citations)} citations')
except FileNotFoundError:
    print(f'Citations file not found, reading from storage')
    citations = []

if not papers or not citations:
    print('Reading from storage variables')
    # Get from storage if file reading failed
    papers = locals().get('var_functions.query_db:56', [])
    citations = locals().get('var_functions.query_db:57', [])
    print(f'Papers: {len(papers)}, Citations: {len(citations)}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
