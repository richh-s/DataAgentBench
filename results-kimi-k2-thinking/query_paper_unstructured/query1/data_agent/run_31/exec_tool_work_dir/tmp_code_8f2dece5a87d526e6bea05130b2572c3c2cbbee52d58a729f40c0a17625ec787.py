code = """import json

# Access the stored result from the query
papers_file = var_functions.query_db:1
print('File path:', papers_file)

# Read and examine the papers data
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Number of papers in file:', len(papers))

# Examine structure
if len(papers) > 0:
    print('First paper keys:', list(papers[0].keys()))
    print('First paper filename:', papers[0].get('filename'))

# Find papers in food domain
food_related = []
for paper in papers:
    text = paper.get('text', '').lower()
    # Check for food domain indicators
    if 'food' in text:
        food_related.append(paper)

print('Food-related papers found:', len(food_related))

# Extract titles
food_titles = []
for paper in food_related:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        food_titles.append(title)

print('Food paper titles:', food_titles[:10])
print('Total food titles:', len(food_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
