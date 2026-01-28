code = """import json, os

# Find data files
data_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'query_' in file and file.endswith('.json'):
            data_files.append(os.path.join(root, file))

print('Data files found:')
for i, f in enumerate(data_files):
    print(str(i) + ': ' + f)

# Load data
citations = json.load(open(data_files[1]))
papers = json.load(open(data_files[0]))

print('Citations loaded: ' + str(len(citations)))
print('Papers loaded: ' + str(len(papers)))

# Find food papers
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie']
food_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    if any(kw in text for kw in food_keywords):
        food_titles.append(filename.replace('.txt', ''))

print('Food papers: ' + str(len(food_titles)))

# Calculate citations
citation_dict = {}
for c in citations:
    citation_dict[c.get('title', '')] = int(c.get('total_citations', 0))

total_citations = 0
for title in food_titles:
    if title in citation_dict:
        total_citations += citation_dict[title]

print('Total citations: ' + str(total_citations))

# Output result
result_output = {"total_citations": total_citations}
print('__RESULT__:')
print(json.dumps(result_output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
