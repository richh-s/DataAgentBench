code = """import json
import re

with open(locals()['var_function-call-2733064720136673673'], 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for paper in paper_docs:
    filename = paper['filename']
    text = paper['text']

    title = filename.replace('.txt', '')

    year = None
    # Try to find year from copyright notice
    match_copyright = re.search(r'Copyright \d{4}', text)
    if match_copyright:
        year = int(match_copyright.group(0)[9:])
    else:
        # Fallback: look for a year in the first 500 characters
        match_year = re.search(r'\b(19|20)\d{2}\b', text[:500])
        if match_year:
            year = int(match_year.group(0))

    contribution_empirical = 'empirical' in text.lower()

    if year and contribution_empirical and year > 2016:
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution_empirical': contribution_empirical
        })

print('__RESULT__:')
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-16794463878987829511': ['paper_docs'], 'var_function-call-2733064720136673673': 'file_storage/function-call-2733064720136673673.json'}

exec(code, env_args)
