code = """import json

# Read the papers file using the correct variable name
papers_file = var_functions.query_db:2
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Number of papers:', len(papers))

# Check first paper structure
if papers:
    first_paper = papers[0]
    print('Keys in first paper:', list(first_paper.keys()))
    print('Filename:', first_paper.get('filename'))

# Find papers related to food
food_papers = []
for paper in papers:
    text = paper.get('text', '').lower()
    if 'food' in text or 'diet' in text or 'nutrition' in text:
        food_papers.append(paper)

print('Food-related papers count:', len(food_papers))

# Extract titles
food_titles = []
for paper in food_papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        food_titles.append(title)

print('Sample titles:', food_titles[:5])
print('Total titles extracted:', len(food_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
