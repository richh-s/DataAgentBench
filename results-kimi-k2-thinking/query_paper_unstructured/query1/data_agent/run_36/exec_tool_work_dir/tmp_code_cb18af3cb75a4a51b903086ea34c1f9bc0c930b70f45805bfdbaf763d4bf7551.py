code = """import json
food_papers = json.loads(locals()['var_functions.execute_python:8'])
print(f'Food papers count: {len(food_papers)}')
print('Food paper titles:')
for p in food_papers[:5]:
    print(f'- {p["title"]}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [{'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt', '_id': '694f5530284b10b11dc0a869'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt', '_id': '694f5530284b10b11dc0a86a'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', '_id': '694f5530284b10b11dc0a86c'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', '_id': '694f5530284b10b11dc0a86e'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', '_id': '694f5530284b10b11dc0a870'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
