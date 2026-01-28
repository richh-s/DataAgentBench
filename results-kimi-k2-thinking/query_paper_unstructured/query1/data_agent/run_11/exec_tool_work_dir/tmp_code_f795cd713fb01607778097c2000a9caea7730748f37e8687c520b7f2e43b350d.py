code = """import json
import re

# Load the citations data
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load the paper documents
paper_docs_file = locals()['var_functions.query_db:6']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of paper title (without .txt) to its text
paper_mapping = {}
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    paper_mapping[title] = doc['text'].lower()  # Store lowercase for easier searching

# Identify papers in the 'food' domain
# Look for food-related keywords in the paper text
food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'dietary']
food_papers = []

for title, text in paper_mapping.items():
    # Check if any food keyword appears in the text
    if any(keyword in text for keyword in food_keywords):
        food_papers.append(title)

# Now filter citations for these food papers
food_citations = []
total_citations = 0

for citation in citations:
    cit_title = citation['title']
    if cit_title in food_papers:
        food_citations.append(citation)
        total_citations += int(citation['citation_count'])

result = {
    'food_papers_found': len(food_papers),
    'food_paper_titles': food_papers,
    'food_citation_records': len(food_citations),
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_citations': 1405, 'total_papers': 5, 'sample_citations': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}]}}

exec(code, env_args)
