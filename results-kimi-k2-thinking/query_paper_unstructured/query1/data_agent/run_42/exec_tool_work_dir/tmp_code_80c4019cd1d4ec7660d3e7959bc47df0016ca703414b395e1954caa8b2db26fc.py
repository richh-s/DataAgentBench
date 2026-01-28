code = """import json
import re

# Load the paper documents from the file path
with open(locals()['var_functions.query_db:0'], 'r') as f:
    paper_docs = json.load(f)

print(f'Total paper documents loaded: {len(paper_docs)}')

# Function to extract paper information and check for food domain
def is_food_related(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = re.sub(r'\.txt$', '', filename)
    
    # Check for food-related terms in text
    text_lower = text.lower()
    
    # More comprehensive food-related terms including typical research contexts
    food_keywords = [
        'food', 'eating', 'diet', 'nutrition', 'calorie', 'meal', 
        'restaurant', 'dietary', 'weight loss', 'weight management',
        'dieting', 'food intake', 'eating habits', 'nutritional'
    ]
    
    # Check if any food keyword appears in text
    for keyword in food_keywords:
        if keyword in text_lower:
            return True, title, keyword
    
    return False, title, None

# Find all food-related papers
food_papers = []
for doc in paper_docs:
    is_food, title, keyword = is_food_related(doc)
    if is_food:
        food_papers.append({'title': title, 'keyword': keyword})

print(f'Number of food-related papers found: {len(food_papers)}')

if food_papers:
    print('Sample food papers:')
    for i, paper in enumerate(food_papers[:10]):
        print(f'  {i+1}. {paper["title"]} (matched: {paper["keyword"]})')

# Get titles for joining with citations
food_paper_titles = [p['title'] for p in food_papers]

result = {
    'food_paper_titles': food_paper_titles,
    'count': len(food_paper_titles),
    'food_papers': food_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'food_paper_titles': [], 'count': 0}, 'var_functions.execute_python:12': {'food_paper_titles': [], 'count': 0}}

exec(code, env_args)
