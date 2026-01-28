code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-13704620957841460900']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

paper_data = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    domain_match = re.search(r'domains? include: \"([^\"]*?food[^\"]*?)\"', text, re.IGNORECASE)
    if not domain_match:
        domain_match = re.search(r'domains? include: .*?(food).*?', text, re.IGNORECASE)
    if not domain_match:
        domain_match = re.search(r'common domains include: \"([^\"]*?food[^\"]*?)\"', text, re.IGNORECASE)
    if not domain_match:
        domain_match = re.search(r'common domains include: .*?(food).*?', text, re.IGNORECASE)

    if domain_match:
        domains_str = domain_match.group(1)
        if 'food' in domains_str.lower():
            paper_data.append({'title': title, 'domain': 'food'})
    else:
        # Fallback to check for 'food' in the entire text if domain field not explicitly found
        if 'food' in text.lower():
            paper_data.append({'title': title, 'domain': 'food'})

food_papers_df = pd.DataFrame(paper_data)
food_paper_titles = food_papers_df['title'].tolist()

__RESULT__:
print(json.dumps(food_paper_titles))"""

env_args = {'var_function-call-6841537143337761221': ['paper_docs'], 'var_function-call-13704620957841460900': 'file_storage/function-call-13704620957841460900.json'}

exec(code, env_args)
