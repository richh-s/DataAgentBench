code = """import json
import re

with open(locals()['var_function-call-16950365781099889160'], 'r') as f:
    paper_docs = json.load(f)

parsed_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract year (assuming it's usually near the beginning or in a header)
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Extract domain (looking for 'physical activity' specifically)
    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if year and domain:
        parsed_papers.append({
            'title': title,
            'year': year,
            'domain': domain
        })

papers_2016_physical_activity = [
    p for p in parsed_papers 
    if p['year'] == 2016 and 'physical activity' in p['domain']
]

__RESULT__:
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_function-call-3004148629208822627': ['paper_docs'], 'var_function-call-16950365781099889160': 'file_storage/function-call-16950365781099889160.json'}

exec(code, env_args)
