code = """import json
import re

# Load the citations data (direct list from previous query)
citations_debug = locals()['var_functions.query_db:16']
if isinstance(citations_debug, str) and 'json' in citations_debug:
    with open(citations_debug, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_debug

# Load the paper documents data from the file
papers_file_path = locals()['var_functions.query_db:17']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Debug: Check what domains are mentioned in the first paper
first_paper = papers_data[0]
text = first_paper.get('text', '')
print('First paper text snippet:', text[:500])

# Extract all paper titles from citations to see what we're working with
citation_titles = set()
for citation in citations_data:
    citation_titles.add(citation.get('title', '').lower())

print('Total unique citation titles:', len(citation_titles))
print('Sample citation titles:', list(citation_titles)[:10])

# Now let's check the paper documents more carefully
paper_titles_in_docs = set()
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '').lower() if filename else ''
    paper_titles_in_docs.add(title)

print('Total paper titles in docs:', len(paper_titles_in_docs))
print('Sample paper titles from docs:', list(paper_titles_in_docs)[:10])

# Check for overlap
overlap = citation_titles.intersection(paper_titles_in_docs)
print('Titles that appear in both:', len(overlap))
print('Sample overlaps:', list(overlap)[:5])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:24': {'total_citation_count': 0, 'papers_in_food_domain': 0, 'matched_paper_titles': []}}

exec(code, env_args)
