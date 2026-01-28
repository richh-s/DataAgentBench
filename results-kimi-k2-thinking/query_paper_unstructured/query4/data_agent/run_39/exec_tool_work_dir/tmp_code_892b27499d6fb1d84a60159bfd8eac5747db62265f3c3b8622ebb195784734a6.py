code = """import json
import re
import os

# Load paper documents from file
paper_docs_file = locals()['var_functions.query_db:14']
print('Loading papers from file')

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print('Total papers: ' + str(len(paper_docs)))

# Find 2016 physical activity papers
papers_2016_pa = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = os.path.splitext(filename)[0]
    
    # Check for 2016
    if '2016' not in text:
        continue
    
    # Check for physical activity keywords
    text_lower = text.lower()
    pa_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking']
    
    if any(kw in text_lower for kw in pa_keywords):
        papers_2016_pa.append(title)

print('Found ' + str(len(papers_2016_pa)) + ' 2016 physical activity papers')

# Load citation data
citations_file = locals()['var_functions.query_db:16']
print('Loading citations from file')

with open(citations_file, 'r') as f:
    citations = json.load(f)

citation_dict = {}
for item in citations:
    citation_dict[item['title']] = int(item['total_citations'])

print('Citation records: ' + str(len(citation_dict)))

# Create results
results = []
for title in papers_2016_pa:
    citation_count = citation_dict.get(title, 0)
    if citation_count > 0:
        results.append({'title': title, 'total_citations': citation_count})
        print('Match: ' + title + ' (' + str(citation_count) + ')')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
