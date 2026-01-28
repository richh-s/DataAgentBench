code = """import json

# Load the citations data
citations_data = var_functions.query_db:11
papers_data = var_functions.query_db:10

# Print summary info
print('Citations records:', len(citations_data))
print('Papers total:', len(papers_data))

# Find food domain papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_titles = []

for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if any(keyword in text for keyword in food_keywords):
        title = filename.replace('.txt', '')
        food_titles.append(title)

print('Food papers found:', len(food_titles))

# Calculate total citations for food papers
citation_dict = {citation['title']: int(citation['total_citations']) for citation in citations_data}

total_citations = 0
matched_count = 0

for title in food_titles:
    if title in citation_dict:
        total_citations += citation_dict[title]
        matched_count += 1

print('Matched papers with citations:', matched_count)
print('Total citations for food domain:', total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
