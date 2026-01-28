code = """import json
import re

# Get the documents from the storage variable
result = var_functions.query_db_2

# Check if result is a string (file path) or already loaded
if isinstance(result, str) and result.endswith('.json'):
    # It's a file path
    with open(result, 'r') as f:
        documents = json.load(f)
else:
    # It's already loaded
    documents = result

print('Total documents: ' + str(len(documents)))

# Function to extract paper information from text
food_papers = []

for doc in documents:
    filename = doc['filename']
    text = doc['text'].lower()
    title = filename.replace('.txt', '')
    
    # Look for domain indicators in the text
    # Count food mentions to determine if it's a primary domain
    food_count = text.count('food')
    
    # Check for food-related patterns
    has_food_keyword = False
    food_patterns = [
        r'\bfood\s*journaling\b',
        r'\bfood\s*track\w*\b',
        r'\btrack\s*food\b',
        r'\beating\s*habits\b',
        r'\bdiet\w*\b',
        r'\bnutrition\w*\b',
        r'\bmeal\w*\b'
    ]
    
    for pattern in food_patterns:
        if re.search(pattern, text):
            has_food_keyword = True
            break
    
    # Consider it a food paper if it has significant mentions or specific keywords
    if food_count >= 5 or (food_count >= 2 and has_food_keyword):
        food_papers.append({
            'title': title,
            'filename': filename,
            'food_mentions': food_count,
            'has_food_keyword': has_food_keyword
        })

print('Found ' + str(len(food_papers)) + ' food domain papers')

# Show some examples
for i in range(min(10, len(food_papers))):
    paper = food_papers[i]
    print(str(i+1) + '. ' + paper['title'] + ' (food mentions: ' + str(paper['food_mentions']) + ', has keyword: ' + str(paper['has_food_keyword']) + ')')

result = {
    "food_papers_count": len(food_papers),
    "papers": food_papers
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
