code = """import json, os

# Initialize variables
citations_path = None
papers_path = None

# Walk through storage directory to find data files
for root, dirs, files in os.walk('storage/result'):
    for file in files:
        if file.startswith('query_') and file.endswith('.json'):
            filepath = os.path.join(root, file)
            if 'Citations' in filepath:
                citations_path = filepath
            elif 'paper_docs' in filepath:
                papers_path = filepath

# Load citations data
citations = []
with open(citations_path) as f:
    citations = json.load(f)

# Load papers data
papers = []
with open(papers_path) as f:
    papers = json.load(f)

# Find food domain papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie', 'cuisine']
food_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    if any(keyword in text for keyword in food_keywords):
        title = filename.replace('.txt', '')
        food_titles.append(title)

# Calculate citations for food papers
citation_lookup = dict([
    (item['title'], int(item.get('total_citations', 0))) for item in citations
])

total_citations = 0
for title in food_titles:
    if title in citation_lookup:
        total_citations += citation_lookup[title]

print('__RESULT__:')
print(str(total_citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
