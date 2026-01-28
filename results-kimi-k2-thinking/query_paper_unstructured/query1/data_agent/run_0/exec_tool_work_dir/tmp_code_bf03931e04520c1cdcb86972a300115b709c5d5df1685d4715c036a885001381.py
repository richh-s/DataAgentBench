code = """# Get all paper documents and extract food domain papers
import json
import os

# Check available variables
all_vars = dir()
print('Available vars count:', len([v for v in all_vars if v.startswith('var_')]))

# Get the MongoDB file path
mongo_key = 'var_functions.query_db:30'
mongo_file = None
if mongo_key in all_vars:
    mongo_file = eval(mongo_key)
elif mongo_key in locals():
    mongo_file = locals()[mongo_key]

print('MongoDB file path:', str(mongo_file)[:100])

# Load paper data
papers = []
if mongo_file and os.path.exists(str(mongo_file)):
    with open(mongo_file, 'r') as f:
        papers = json.load(f)

print('Loaded papers:', len(papers))

# Extract food domain paper titles
food_titles = []
keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Check if this is about food research
    for keyword in keywords:
        if keyword in text and ('track' in text or 'domain' in text):
            title = filename.replace('.txt', '')
            food_titles.append(title)
            break

print('Food papers found:', len(food_titles))
print('Sample titles:', food_titles[:5])

result = {'food_titles': food_titles, 'count': len(food_titles)}

output = '__RESULT__:' + json.dumps(result)
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:26': {'food_paper_titles': [], 'food_paper_count': 0, 'citation_sample': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
