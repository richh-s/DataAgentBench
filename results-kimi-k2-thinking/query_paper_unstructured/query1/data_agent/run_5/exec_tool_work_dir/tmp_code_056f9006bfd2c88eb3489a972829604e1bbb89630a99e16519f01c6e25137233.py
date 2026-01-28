code = """import json
import re

# Read the paper documents from the file
with open('file_storage/functions.query_db:14.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citations from the file  
with open('file_storage/functions.query_db:8.json', 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(paper_docs)} papers and {len(citations)} citation records")

# Extract paper titles and identify food domain papers
food_papers = []
paper_titles = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    paper_titles.append(title)
    
    # Check if paper is in food domain by searching text
    text = doc.get('text', '').lower()
    if 'food' in text:
        food_papers.append(title)

print(f"Found {len(food_papers)} papers mentioning 'food'")
print(f"Sample food papers: {food_papers[:5]}")

# Create a set for faster lookup
food_papers_set = set(food_papers)

# Sum citations for food domain papers
total_citations = 0
food_citation_count = 0

for citation in citations:
    citation_title = citation.get('title', '')
    if citation_title in food_papers_set:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        food_citation_count += 1

print(f"Matched {food_citation_count} citation records for food papers")
print(f"Total citation count for food domain papers: {total_citations}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'paper_docs_file': 'file_storage/functions.query_db:6.json', 'citations_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
