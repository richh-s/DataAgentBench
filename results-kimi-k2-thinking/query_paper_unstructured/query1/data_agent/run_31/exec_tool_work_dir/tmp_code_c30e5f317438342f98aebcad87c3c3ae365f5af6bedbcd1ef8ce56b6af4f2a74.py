code = """import json, os

# Load citations and papers data
citations = json.load(open('storage/result/query_Citations_citations_database_12.json'))
papers = json.load(open('storage/result/query_paper_docs_paper_docs_database_11.json'))

# Find all food-related papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_papers = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if any(keyword in text for keyword in food_keywords):
        title = filename.replace('.txt', '')
        food_papers.append(title)

# Calculate total citations for food papers
citation_totals = {}
for citation in citations:
    citation_totals[citation['title']] = int(citation['total_citations'])

total_sum = 0
matched_count = 0
for paper_title in food_papers:
    if paper_title in citation_totals:
        total_sum += citation_totals[paper_title]
        matched_count += 1

result = {'total_citations': total_sum}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:52': {'total_citations': 0}}

exec(code, env_args)
