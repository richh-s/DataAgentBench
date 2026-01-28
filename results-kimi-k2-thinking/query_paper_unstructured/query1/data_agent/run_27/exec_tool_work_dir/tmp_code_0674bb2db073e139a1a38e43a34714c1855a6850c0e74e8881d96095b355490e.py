code = """import json

# Read paper documents
paper_docs_path = './var_functions.query_db:8.json'
citations_path = './var_functions.query_db:12.json'

# Load and process the data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(paper_docs)} paper documents")
print(f"Loaded {len(citations)} citation records")

# Identify food papers
food_paper_titles = []
for paper in paper_docs:
    title = paper['filename'].replace('.txt', '')
    # Check if 'food' appears in the text (case-insensitive)
    if 'food' in paper.get('text', '').lower():
        food_paper_titles.append(title)

print(f"Found {len(food_paper_titles)} food-related papers")
print(f"Food papers: {food_paper_titles}")

# Sum citations for food papers
total_citations = 0
food_citations = []
for citation in citations:
    if citation['title'] in food_paper_titles:
        total_citations += int(citation['citation_count'])
        food_citations.append(citation)

print(f"Total citation count for food domain papers: {total_citations}")
print(f"Number of citation records for food papers: {len(food_citations)}")

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
