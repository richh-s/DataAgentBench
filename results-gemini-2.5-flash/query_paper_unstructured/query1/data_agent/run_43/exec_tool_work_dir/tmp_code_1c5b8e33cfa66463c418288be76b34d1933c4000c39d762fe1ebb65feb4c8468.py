code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-17415221888068049620'], 'r') as f:
    paper_docs = json.load(f)

food_papers_titles = []
for doc in paper_docs:
    text = doc['text'].lower()
    title = doc['filename'].replace('.txt', '')
    
    # Find the line containing 'domain:'
    domain_match = re.search(r'domain(?:s)?:\s*(.*)', text)
    if domain_match:
        domains_string = domain_match.group(1)
        if 'food' in domains_string:
            food_papers_titles.append(title)

print('__RESULT__:')
print(json.dumps(food_papers_titles))"""

env_args = {'var_function-call-288462182814586690': ['paper_docs'], 'var_function-call-17415221888068049620': 'file_storage/function-call-17415221888068049620.json', 'var_function-call-7078895685832278017': [], 'var_function-call-1270969914095325749': 'file_storage/function-call-1270969914095325749.json'}

exec(code, env_args)
