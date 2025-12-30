code = """import json
import re

file_path = locals()['var_function-call-12833057213824030696']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers = []
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']

    # Search for '2016' or '\'16' anywhere in the text
    found_year_2016 = re.search(r'\\b2016\\b|\\'\\s*16\\b', text)
    domain_match = re.search(r'physical activity', text, re.IGNORECASE)

    if found_year_2016 and domain_match:
        extracted_papers.append({'title': title, 'year': 2016, 'domain': 'physical activity'})

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-13855130215716654146': ['paper_docs'], 'var_function-call-12833057213824030696': 'file_storage/function-call-12833057213824030696.json', 'var_function-call-10685984074466707249': []}

exec(code, env_args)
