code = """# Let's access the papers data we already have
papers_file = var_functions.query_db:4
print('Papers file path:', papers_file)

# Read the papers data
import json
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Number of papers loaded:', len(papers))

# Let's examine the first paper more carefully
if papers:
    first_paper = papers[0]
    print('\nFirst paper filename:', first_paper.get('filename'))
    print('\nFirst paper text snippet:')
    print(first_paper.get('text', '')[:500])

# Now let's search for papers in the food domain
# Since domain might be mentioned in various ways, let's look for food-related keywords
food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'culinary']

food_papers = []
for paper in papers:
    text = paper.get('text', '').lower()
    # Check if any food keyword appears in the text
    if any(keyword in text for keyword in food_keywords):
        food_papers.append(paper)

print('\nFood domain papers found:', len(food_papers))

# Extract titles from food papers
food_titles = []
for paper in food_papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        food_titles.append(title)

print('Food paper titles sample:', food_titles[:10])
print('Total food papers extracted:', len(food_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
