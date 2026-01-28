code = """import json
import re

with open('/tmp/pwsxceql.json', 'r') as f:
    papers = json.load(f)

print(f"Total papers retrieved: {len(papers)}")

empirical_papers_after_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    year = None
    if '2017' in text or '2018' in text or '2019' in text or '2020' in text or '2021' in text:
        year_match = re.search(r'\b(20(1[7-9]|[2-9]\d))\b', text)
        if year_match:
            year = int(year_match.group(1))
    
    if 'empirical' in text.lower():
        contribution = 'empirical'
    else:
        contribution = None
    
    if contribution == 'empirical' and year and year > 2016:
        empirical_papers_after_2016.append({'title': title, 'year': year})

print(f"Empirical papers after 2016: {len(empirical_papers_after_2016)}")
for paper in empirical_papers_after_2016:
    print(f"  Title: {paper['title']}")
    print(f"  Year: {paper['year']}")
    print()"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
