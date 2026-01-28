code = """import json
import re

# Read the paper documents from the file
paper_docs_file = locals()['var_functions.query_db:3']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Function to check if a paper is in the food domain
def is_food_domain_paper(text, filename):
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Patterns that indicate food domain
    patterns = [
        r'food\s*\[',  # food [11]
        r'trackers? of.*?food',  # trackers of ... food
        r'tracking.*?food',  # tracking ... food
        r'food\s+tracking',  # food tracking
        r'food\s+journal',  # food journal
        r'weight loss',  # often related to food
        r'eating habits',  # related to food
        r'diet\s+tracking',  # diet tracking
        r'calorie',  # calorie counting
        r'nutrition',  # nutrition tracking
    ]
    
    for pattern in patterns:
        if re.search(pattern, text_lower):
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
    'sample_food_papers': food_papers[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
