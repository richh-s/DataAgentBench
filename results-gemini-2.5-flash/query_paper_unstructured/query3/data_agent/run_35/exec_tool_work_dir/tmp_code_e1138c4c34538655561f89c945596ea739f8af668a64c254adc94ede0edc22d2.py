code = """import json
import re

with open(locals()['var_function-call-5400047117669112550'], 'r') as f:
    paper_docs = json.load(f)

parsed_papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')

    year_match = re.search(r'([12][0-9]{3})', text)
    year = int(year_match.group(1)) if year_match else None

    parsed_papers.append({
        'title': title,
        'year': year,
        'full_text': text # Keep full text for 'empirical' check
    })

filtered_titles_by_year_and_contribution = [
    p['title'] for p in parsed_papers
    if p['year'] and p['year'] > 2016 and p['full_text'] and 'empirical' in p['full_text'].lower()
]

print("__RESULT__:")
print(json.dumps(filtered_titles_by_year_and_contribution))"""

env_args = {'var_function-call-16356890130241980815': ['paper_docs'], 'var_function-call-5400047117669112550': 'file_storage/function-call-5400047117669112550.json'}

exec(code, env_args)
