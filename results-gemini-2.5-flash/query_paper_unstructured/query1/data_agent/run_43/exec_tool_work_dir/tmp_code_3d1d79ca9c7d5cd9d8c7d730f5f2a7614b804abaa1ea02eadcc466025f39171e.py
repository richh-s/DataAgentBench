code = """import json
import pandas as pd

with open(locals()['var_function-call-17415221888068049620'], 'r') as f:
    paper_docs = json.load(f)

food_papers_titles = []
for doc in paper_docs:
    text = doc['text'].lower()
    if 'domain: food' in text or 'domains: food' in text:
        title = doc['filename'].replace('.txt', '')
        food_papers_titles.append(title)

print('__RESULT__:')
print(json.dumps(food_papers_titles))"""

env_args = {'var_function-call-288462182814586690': ['paper_docs'], 'var_function-call-17415221888068049620': 'file_storage/function-call-17415221888068049620.json'}

exec(code, env_args)
