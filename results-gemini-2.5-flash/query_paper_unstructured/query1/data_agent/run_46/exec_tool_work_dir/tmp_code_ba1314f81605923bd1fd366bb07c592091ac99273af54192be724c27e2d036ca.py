code = """import json
import re

with open(locals()['var_function-call-6893631717039984758'], 'r') as f:
    paper_docs = json.load(f)

food_related_papers = []
for doc in paper_docs:
    text = doc['text'].lower()
    # Look for 'food' as a standalone word or part of a phrase indicating domain/topic
    # Using word boundaries to avoid matching 'food' in other words like 'foodstuff'
    if re.search(r'\bfood\b', text):
        title = doc['filename'].replace('.txt', '')
        food_related_papers.append(title)

print("__RESULT__:")
print(json.dumps(food_related_papers))"""

env_args = {'var_function-call-8792593880583760035': ['paper_docs'], 'var_function-call-9978232910626699419': [], 'var_function-call-6497029258880074568': ['Citations', 'sqlite_sequence'], 'var_function-call-6893631717039984758': 'file_storage/function-call-6893631717039984758.json', 'var_function-call-9273036665786985738': []}

exec(code, env_args)
