code = """import json
import pandas as pd

# Assuming var_function-call-7904453032601314041 is the path to the JSON file
with open(locals()['var_function-call-7904453032601314041'], 'r') as f:
    paper_docs = json.load(f)

papers_with_food_keyword = []
for doc in paper_docs:
    text = doc['text'].lower()
    if 'food' in text:
        papers_with_food_keyword.append(doc['filename'].replace('.txt', ''))

# Remove duplicates
papers_with_food_keyword = list(set(papers_with_food_keyword))

print('__RESULT__:')
print(json.dumps(papers_with_food_keyword))"""

env_args = {'var_function-call-6657107240565952788': ['paper_docs'], 'var_function-call-2391682954640005035': [], 'var_function-call-7904453032601314041': 'file_storage/function-call-7904453032601314041.json', 'var_function-call-7121668566034915059': []}

exec(code, env_args)
