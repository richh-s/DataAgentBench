code = """import json

# Access the stored file path from locals()
file_path = locals()['var_functions.query_db:2']

print('File path:', file_path)

# Read the file to get paper documents
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded', len(paper_docs), 'paper documents')

# Initialize list to store food domain paper titles
food_paper_titles = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Normalize text to lowercase for searching
    lower_text = text.lower()
    
    # Check if this is a food domain paper
    food_keywords = ['food', 'eating', 'nutrition', 'diet', 'meal', 'calorie', 'dietary']
    is_food = any(keyword in lower_text for keyword in food_keywords)
    
    if is_food:
        food_paper_titles.append(title)

food_papers_count = len(food_paper_titles)
print(f'Found {food_papers_count} food domain papers')

# Create result dictionary
result = {
    'food_papers_count': food_papers_count,
    'food_paper_titles': food_paper_titles
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
