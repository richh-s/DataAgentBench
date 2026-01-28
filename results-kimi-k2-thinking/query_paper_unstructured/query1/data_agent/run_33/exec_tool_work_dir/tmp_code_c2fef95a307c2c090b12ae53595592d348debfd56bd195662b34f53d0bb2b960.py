code = """import json

# Get data from storage
papers = locals()['var_functions.query_db:2']
citations = locals()['var_functions.query_db:5']

print('Papers loaded', len(papers))
print('Citations loaded', len(citations))

# Find food papers
food_titles = set()
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        text = paper.get('text', '').lower()
        if 'food' in text:
            food_titles.add(title)

print('Food papers', len(food_titles))

# Calculate total citations
total_citations = 0
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_titles:
        total_citations += int(citation.get('citation_count', 0))

print('Total food citations', total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
