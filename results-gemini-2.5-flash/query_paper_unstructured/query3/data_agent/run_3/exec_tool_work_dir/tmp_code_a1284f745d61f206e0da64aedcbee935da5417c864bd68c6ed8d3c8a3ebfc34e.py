code = """import json
import re

file_path = locals()['var_function-call-8451556604040005886']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Attempt to find a 4-digit year
    year_4_digit_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_4_digit_match:
        year = int(year_4_digit_match.group(0))
    else:
        # Attempt to find conference year format like '15 (for 2015) or '99 (for 1999)
        year_conf_match = re.search(r"'(\d{2})", text)
        if year_conf_match:
            year_suffix = int(year_conf_match.group(1))
            if year_suffix < 50:  # Assuming 20xx
                year = 2000 + year_suffix
            else:  # Assuming 19xx
                year = 1900 + year_suffix

    is_empirical = False
    if re.search(r'empirical', text, re.IGNORECASE):
        is_empirical = True

    if year and is_empirical:
        papers_data.append({'title': title, 'year': year, 'contribution': 'empirical'})

filtered_papers = [p for p in papers_data if p['year'] > 2016]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-1330267927777135001': ['paper_docs'], 'var_function-call-8451556604040005886': 'file_storage/function-call-8451556604040005886.json'}

exec(code, env_args)
