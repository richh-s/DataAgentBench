code = """import json
import re

# Load the result from the previous query
with open(locals()['var_function-call-2585691326327215227'], 'r') as f:
    papers = json.load(f)

print(f"Total papers matching 'food' in text: {len(papers)}")

# Let's verify a few papers to see if 'food' is a domain or just a word.
# We'll look for 'Author Keywords' or just occurrence.
titles = []
for p in papers:
    # Extract title from filename
    title = p['filename'].replace('.txt', '')
    text = p['text'].lower()
    
    # Check if 'food' is a distinct word to avoid 'flood', 'seafood' etc if regex didn't handle word boundaries
    # Mongo regex was just "food".
    if re.search(r'\bfood\b', text):
        titles.append(title)

print(f"Total papers with whole word 'food': {len(titles)}")
print(f"First 5 titles: {titles[:5]}")

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-13604834933233695573': 'file_storage/function-call-13604834933233695573.json', 'var_function-call-13672825597397015902': 'file_storage/function-call-13672825597397015902.json', 'var_function-call-2585691326327215227': 'file_storage/function-call-2585691326327215227.json'}

exec(code, env_args)
