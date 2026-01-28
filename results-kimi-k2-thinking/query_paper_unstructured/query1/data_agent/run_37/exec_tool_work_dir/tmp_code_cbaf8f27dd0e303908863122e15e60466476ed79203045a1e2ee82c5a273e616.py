code = """import json
import re

# Read the paper documents from the file
paper_docs_file = locals()['var_functions.query_db:12']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Function to check if a paper is in the food domain
def is_food_domain_paper(text, filename):
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    filename_lower = filename.lower()
    
    # Check if filename contains 'food'
    if 'food' in filename_lower:
        return True
    
    # Patterns that indicate food domain (looking for primary focus, not just mentions)
    patterns = [
        r'food\s+journal',  # food journal
        r'food\s+tracking',  # food tracking
        r'food\s+consumption',  # food consumption
        r'eating\s+habits',  # eating habits
        r'calorie\s+counting',  # calorie counting
        r'nutrition\s+tracking',  # nutrition tracking
        r'weight\s+loss',  # weight loss (often food-focused)
        r'diet\s+tracking',  # diet tracking
        r'meal\s+logging',  # meal logging
        r'food\s+intake',  # food intake
    ]
    
    # Count occurrences of food-related terms
    food_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, text_lower)
        food_count += len(matches)
    
    # Also check for explicit domain mentions
    domain_patterns = [
        r'domain.*?food',
        r'trackers? of.*?food',
        r'study.*?food',
        r'focus on.*?food'
    ]
    
    domain_count = 0
    for pattern in domain_patterns:
        matches = re.findall(pattern, text_lower)
        domain_count += len(matches)
    
    # If we have at least 3 food-related mentions or a domain focus, it's likely a food paper
    if food_count >= 3 or domain_count >= 1:
        return True
    
    return False

# Extract food domain papers
food_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    if is_food_domain_paper(text, filename):
        food_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    'food_papers_count': len(food_papers),
    'food_papers': food_papers
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:7': {'food_papers_count': 2, 'sample_food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_citation_count': 610, 'paper_breakdown': {'A Lived Informatics Model of Personal Informatics': 390, 'A Stage-based Model of Personal Informatics Systems': 220}, 'total_food_papers': 2}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
