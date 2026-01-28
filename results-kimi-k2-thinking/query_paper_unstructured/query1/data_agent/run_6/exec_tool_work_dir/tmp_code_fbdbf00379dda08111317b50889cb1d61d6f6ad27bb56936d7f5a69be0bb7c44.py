code = """import json
import re

# Load the MongoDB documents
mongo_result = locals()['var_functions.query_db:0']

# If it's a file path, read the file
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        papers = json.load(f)
else:
    papers = mongo_result

print(f"Number of papers from MongoDB: {len(papers)}")

# Extract paper information from documents
paper_info = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for domain keywords in the text
    text_lower = text.lower()
    domain_keywords = ['food', 'nutrition', 'eating', 'diet', 'meal']
    has_food_domain = any(keyword in text_lower for keyword in domain_keywords)
    
    if has_food_domain:
        paper_info.append(title)

print(f"Papers with food domain: {len(paper_info)}")

print("__RESULT__:")
print(json.dumps(paper_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
