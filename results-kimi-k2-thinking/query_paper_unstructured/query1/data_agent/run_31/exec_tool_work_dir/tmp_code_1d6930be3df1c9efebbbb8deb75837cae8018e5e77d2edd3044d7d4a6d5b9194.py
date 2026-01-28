code = """import json
import re

# Read the paper documents file path from storage
file_path = var_functions.query_db_2
print(f"File path: {file_path}")

# Read the papers from the file
with open(file_path, 'r') as f:
    papers = json.load(f)

# Let's examine the structure first
print(f"Number of papers retrieved: {len(papers)}")
if papers:
    print("Sample paper structure (first 500 chars):")
    sample = papers[0]
    print(f"Keys: {list(sample.keys())}")
    print(f"Filename: {sample.get('filename')}")
    print(f"Text preview: {sample.get('text', '')[:200]}")
    
# Now let's look for papers in the 'food' domain
food_papers = []
for paper in papers:
    text = paper.get('text', '').lower()
    # Look for food domain indicators - could be mentioned in various ways
    if 'food' in text or 'diet' in text or 'nutrition' in text:
        food_papers.append(paper)

print(f"\nNumber of papers potentially in food domain: {len(food_papers)}")

# Extract titles from food papers
food_titles = []
for paper in food_papers:
    filename = paper.get('filename', '')
    # Remove .txt extension to get title
    title = filename.replace('.txt', '')
    food_titles.append(title)

print(f"Food-related paper titles found: {food_titles[:10]}")  # Show first 10
print(f"Total food-related papers identified: {len(food_titles)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
