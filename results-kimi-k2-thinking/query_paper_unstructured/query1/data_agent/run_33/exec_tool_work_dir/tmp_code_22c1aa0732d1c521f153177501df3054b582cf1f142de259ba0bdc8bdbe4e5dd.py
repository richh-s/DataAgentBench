code = """import json
import os

# This should be our storage key for the big papers data
papers_storage_key = 'query_db_40'
citations_storage_key = 'query_db_5'

# Debug: check what we have
print('Current variables:', list(locals().keys()))
print('Looking for papers_storage_key', papers_storage_key)
print('Looking for citations_storage_key', citations_storage_key)

# Try to access citations (should be in storage already)
if citations_storage_key in locals():
    citations = locals()[citations_storage_key]
    print('Citations loaded:', len(citations))
else:
    print('Citations not found')
    citations = []

# For papers, check if it's a file path
papers_file = '/tmp/query_db_40.json'
if os.path.exists(papers_file):
    with open(papers_file, 'r') as f:
        papers = json.load(f)
    print('Papers loaded from file:', len(papers))
else:
    print('Papers file not found:', papers_file)
    papers = []

# Now find food papers and calculate citations
if papers and citations:
    food_titles = set()
    for paper in papers:
        filename = paper.get('filename', '')
        if filename and filename.endswith('.txt'):
            title = filename[:-4]
            text = paper.get('text', '').lower()
            if 'food' in text:
                food_titles.add(title)
    
    total_citations = 0
    for citation in citations:
        if citation.get('title') in food_titles:
            total_citations += int(citation.get('citation_count', 0))
    
    result = {"total_food_citations": total_citations}
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('Missing data')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
