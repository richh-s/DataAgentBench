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
    # Try to find a 4-digit year (e.g., 2017) directly in the text
    year_4_digit_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_4_digit_match:
        year = int(year_4_digit_match.group(0))
    else:
        # Try to find year in a common conference format like '15 (for 2015)
        # This often appears after a conference acronym like 'CHI '15
        conf_year_match = re.search(r'[A-Z]{2,5}\s\'(\d{2})', text)
        if conf_year_match:
            year_suffix = int(conf_year_match.group(1))
            year = 2000 + year_suffix if year_suffix < 50 else 1900 + year_suffix

    # Check for 'empirical' contribution by searching for the word anywhere in the text
    is_empirical = bool(re.search(r'empirical', text, re.IGNORECASE))

    if year and is_empirical:
        papers_data.append({'title': title, 'year': year})

# Filter papers published after 2016
filtered_papers = [p for p in papers_data if p['year'] > 2016]

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-1330267927777135001': ['paper_docs'], 'var_function-call-8451556604040005886': 'file_storage/function-call-8451556604040005886.json', 'var_function-call-4293209901039072546': []}

exec(code, env_args)
