code = """import json, os

# List files in storage/result
base_dir = 'storage/result'
print('Files in storage/result:')
for file in os.listdir(base_dir):
    print('  ', file)
    
# Try to load the most recent files
citations_path = os.path.join(base_dir, 'query_Citations_citations_database_12.json')
papers_path = os.path.join(base_dir, 'query_paper_docs_paper_docs_database_11.json')

print('\nTrying to load:', citations_path)
print('Trying to load:', papers_path)

# Load citations
citations = []
with open(citations_path) as f:
    citations = json.load(f)
    print('Citations loaded:', len(citations))

# Load papers  
papers = []
with open(papers_path) as f:
    papers = json.load(f)
    print('Papers loaded:', len(papers))

# Find food papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    if any(kw in text for kw in food_keywords):
        title = filename.replace('.txt', '')
        food_titles.append(title)

print('Food papers identified:', len(food_titles))

# Match with citations
citation_map = dict(
    (item['title'], int(item.get('total_citations', 0))) for item in citations
)

total_citations = sum(
    citation_map[title] for title in food_titles if title in citation_map
)

print('Total citations for food domain:', total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
