code = """import json
import re

paper_docs_file = locals()['var_function-call-990683616783124079']

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')
    year = None
    domain = []

    # Extract year (looking for patterns like 'UBICOMP '15, SEPTEMBER 7–11, 2015')
    year_match = re.search(r'\b\d{4}\b', text)
    if year_match:
        year = int(year_match.group(0))

    # Extract domain (looking for 'physical activity' in the text, especially near keywords or abstract)
    if re.search(r'physical activity', text, re.IGNORECASE):
        domain.append('physical activity')

    if year is not None:
        extracted_papers.append({
            'title': title,
            'year': year,
            'domain': domain
        })

# Filter for year 2016 and 'physical activity' domain
filtered_papers = [
    p for p in extracted_papers
    if p['year'] == 2016 and 'physical activity' in p['domain']
]

# Extract titles of filtered papers
filtered_titles = [p['title'] for p in filtered_papers]

print('__RESULT__:')
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-13053415289831067663': ['paper_docs'], 'var_function-call-990683616783124079': 'file_storage/function-call-990683616783124079.json'}

exec(code, env_args)
