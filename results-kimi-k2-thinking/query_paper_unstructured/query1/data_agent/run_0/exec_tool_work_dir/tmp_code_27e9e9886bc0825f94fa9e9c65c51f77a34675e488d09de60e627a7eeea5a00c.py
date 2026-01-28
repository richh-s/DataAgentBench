code = """import json
import os

# Get the MongoDB file path from environment
mongo_file_key = 'var_functions.query_db:30'
if mongo_file_key in dir():
    mongo_file = eval(mongo_file_key)
    print('Using mongo file from eval')
elif mongo_file_key in locals():
    mongo_file = locals()[mongo_file_key]
    print('Using mongo file from locals')
else:
    print('MongoDB file key not found')
    mongo_file = None

print('Mongo file: ' + str(mongo_file))

# Load the data
paper_docs = []
if mongo_file and os.path.exists(mongo_file):
    with open(mongo_file, 'r') as f:
        paper_docs = json.load(f)
    print('Loaded ' + str(len(paper_docs)) + ' documents')

# Find food papers
food_papers = []
keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary']

for doc in paper_docs:
    text_lower = doc.get('text', '').lower()
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    for keyword in keywords:
        if keyword in text_lower:
            food_papers.append(title)
            break

result = {
    'food_titles': food_papers,
    'count': len(food_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:26': {'food_paper_titles': [], 'food_paper_count': 0, 'citation_sample': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
