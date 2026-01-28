code = """import json

# Access food papers list from storage
food_papers = locals()['var_functions.execute_python:8']

# Load citations data
citations_path = locals()['var_functions.query_db:12']
with open(citations_path, 'r') as f:
    citations_list = json.load(f)

# Create a dictionary for quick lookup
citations_dict = {}
for item in citations_list:
    citations_dict[item['title']] = int(item['total_citations'])

# Find and sum citations for food papers
total = 0
count = 0
for paper in food_papers:
    title = paper['title']
    if title in citations_dict:
        total += citations_dict[title]
        count += 1

result = {'total_citations': total, 'paper_count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [{'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt', '_id': '694f5530284b10b11dc0a869'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt', '_id': '694f5530284b10b11dc0a86a'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', '_id': '694f5530284b10b11dc0a86c'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', '_id': '694f5530284b10b11dc0a86e'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', '_id': '694f5530284b10b11dc0a870'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
