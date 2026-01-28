code = """import json
import re

# Get the documents from the storage variable using locals()
documents_key = 'var_functions.query_db:2'
result_path = locals()[documents_key]

# Read the JSON file
with open(result_path, 'r') as f:
    documents = json.load(f)

print('Total documents: ' + str(len(documents)))

# Look for papers with 'food' domain
food_papers = []
food_titles = []

for doc in documents:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc.get('text', '').lower()
    
    # Count food mentions
    food_count = text.count('food')
    
    # Check if this is a food paper by looking for patterns
    has_food_citation = 'food [' in doc.get('text', '')
    has_food_comma = 'food,' in doc.get('text', '')
    has_food_pattern = re.search(r'\bfood\s*[,\[]', text) is not None
    has_food_journal = re.search(r'food\s+journal', text) is not None
    has_food_tracking = re.search(r'food\s+track', text) is not None
    
    # If it has significant food mentions or food citations, include it
    if food_count >= 3 or has_food_citation or has_food_pattern or has_food_journal or has_food_tracking:
        food_papers.append({
            'title': title,
            'filename': filename,
            'food_count': food_count
        })
        food_titles.append(title)

print('Found ' + str(len(food_papers)) + ' food papers')

# Show some examples
for i in range(min(5, len(food_papers))):
    paper = food_papers[i]
    print(str(i+1) + '. ' + paper['title'] + ' (' + str(paper['food_count']) + ' food mentions)')

output = {
    'food_papers_count': len(food_papers),
    'food_titles': food_titles
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
