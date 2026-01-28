code = """import json, os

# Get file listing
base_dir = 'storage/result'
print('Files in storage:')
for filename in os.listdir(base_dir):
    print('-', filename)

# Load data files
citations_file = 'storage/result/query_Citations_citations_database_12.json'
papers_file = 'storage/result/query_paper_docs_paper_docs_database_11.json'

print('Loading citations...')
citations = json.load(open(citations_file))
print('Citations loaded:', len(citations))

print('Loading papers...')
papers = json.load(open(papers_file))
print('Papers loaded:', len(papers))

# Find food papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    if any(word in text for word in food_keywords):
        title = filename.replace('.txt', '')
        food_titles.append(title)

print('Food papers count:', len(food_titles))

# Create citation lookup
citation_counts = {item['title']: int(item.get('total_citations', 0)) for item in citations}

# Sum citations for food papers
total_food_citations = sum(citation_counts[title] for title in food_titles if title in citation_counts)

print('TOTAL CITATIONS FOR FOOD DOMAIN:', total_food_citations)

# Format and print result
result_output = str(total_food_citations)
print('__RESULT__:')
print(result_output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
