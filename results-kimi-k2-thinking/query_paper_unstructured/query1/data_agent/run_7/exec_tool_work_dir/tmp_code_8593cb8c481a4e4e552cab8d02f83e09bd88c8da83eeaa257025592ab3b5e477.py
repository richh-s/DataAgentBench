code = """import json

# Read the MongoDB query result
with open(var_functions.query_db:2, 'r') as f:
    paper_docs = json.load(f)

# Function to check if a paper is in the food domain
def is_food_domain(text):
    # Look for food-related keywords in the text
    food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'dietary']
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in food_keywords)

# Extract food domain papers
food_papers = []
for doc in paper_docs:
    if is_food_domain(doc['text']):
        # Extract title from filename (remove .txt extension)
        title = doc['filename'].replace('.txt', '')
        food_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    'food_papers_count': len(food_papers),
    'food_papers': food_papers[:10]  # Show first 10 for verification
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
