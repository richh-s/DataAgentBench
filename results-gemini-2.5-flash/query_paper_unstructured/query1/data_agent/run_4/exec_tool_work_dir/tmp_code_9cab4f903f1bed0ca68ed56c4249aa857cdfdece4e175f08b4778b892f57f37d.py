code = """import json
import pandas as pd

# Assuming var_function-call-7904453032601314041 is the path to the JSON file
with open(locals()['var_function-call-7904453032601314041'], 'r') as f:
    paper_docs = json.load(f)

papers_in_food_domain = []
for doc in paper_docs:
    text = doc['text'].lower()
    if 'domain: food' in text or 'domains: food' in text:
        papers_in_food_domain.append(doc['filename'].replace('.txt', ''))
    elif 'food' in text and ('domain' in text or 'domains' in text):
        # A more flexible check if 'food' is mentioned near 'domain' or 'domains'
        # This might require more sophisticated NLP if simple substring isn't enough
        domain_index = text.find('domain')
        if domain_index == -1:
            domain_index = text.find('domains')
        if domain_index != -1:
            # Check a window around 'domain' for 'food'
            # This is a heuristic and might need tuning
            window_start = max(0, domain_index - 20)
            window_end = min(len(text), domain_index + 50)
            if 'food' in text[window_start:window_end]:
                papers_in_food_domain.append(doc['filename'].replace('.txt', ''))

# Remove duplicates in case a paper was added by multiple conditions
papers_in_food_domain = list(set(papers_in_food_domain))

print('__RESULT__:')
print(json.dumps(papers_in_food_domain))"""

env_args = {'var_function-call-6657107240565952788': ['paper_docs'], 'var_function-call-2391682954640005035': [], 'var_function-call-7904453032601314041': 'file_storage/function-call-7904453032601314041.json'}

exec(code, env_args)
