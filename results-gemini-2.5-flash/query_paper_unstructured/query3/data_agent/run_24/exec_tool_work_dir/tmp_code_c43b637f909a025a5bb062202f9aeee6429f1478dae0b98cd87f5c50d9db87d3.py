code = """import json
import re

file_path = locals()['var_function-call-11074864686939389486']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

filtered_papers = []
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']

    # Extract year
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'empirical' contribution
    empirical_contribution = 'empirical' in text.lower()

    if year and year > 2016 and empirical_contribution:
        filtered_papers.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-11074864686939389486': 'file_storage/function-call-11074864686939389486.json'}

exec(code, env_args)
