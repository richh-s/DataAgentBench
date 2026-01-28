code = """import json
import re

result_path = var_functions.query_db_2

with open(result_path, 'r') as f:
    documents = json.load(f)

print('Total documents: ' + str(len(documents)))

food_papers = []
food_titles = []

for doc in documents:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc.get('text', '').lower()
    
    food_count = text.count('food')
    
    pattern1 = 'food [' in doc.get('text', '')
    pattern2 = 'food,' in doc.get('text', '')
    pattern3 = re.search(r'\bfood\s*[,\[]', text)
    pattern4 = re.search(r'food\s+journal', text)
    pattern5 = re.search(r'food\s+track', text)
    
    if food_count >= 3 or pattern1 or pattern2 or pattern3 or pattern4 or pattern5:
        food_papers.append({
            'title': title,
            'filename': filename,
            'food_count': food_count
        })
        food_titles.append(title)

print('Found ' + str(len(food_papers)) + ' food papers')

for i in range(min(3, len(food_papers))):
    paper = food_papers[i]
    print(str(i+1) + '. ' + paper['title'] + ' (' + str(paper['food_count']) + ' mentions)')

output = {
    'count': len(food_papers),
    'titles': food_titles,
    'papers': food_papers[:3]
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
