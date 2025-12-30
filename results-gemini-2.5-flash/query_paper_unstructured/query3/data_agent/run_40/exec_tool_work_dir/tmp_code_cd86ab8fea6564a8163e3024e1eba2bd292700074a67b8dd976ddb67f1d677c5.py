code = """import json
import re

file_path = locals()['var_function-call-8974985645401887369']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None

    if year and year > 2016 and 'empirical' in text.lower():
        extracted_papers.append({
            'title': title,
            'year': year
        })

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-3627491098943866791': ['paper_docs'], 'var_function-call-8974985645401887369': 'file_storage/function-call-8974985645401887369.json', 'var_function-call-5569876237921393981': []}

exec(code, env_args)
