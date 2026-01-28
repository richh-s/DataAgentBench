code = """import json
import re

result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents retrieved: {len(civic_docs)}")

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 10 and (line.isupper() or (line.istitle() and not line.startswith('Page'))):
            if not any(keyword in line.lower() for keyword in ['agenda', 'item', 'public works', 'commission', 'meeting', 'subject:', 'recommended action:']):
                following_text = '\n'.join(lines[i:i+20])
                if re.search(r'2022.*?Spring', following_text, re.IGNORECASE) or \
                   re.search(r'Spring.*?2022', following_text, re.IGNORECASE) or \
                   re.search(r'2022[\-\s](?:Mar|Apr|May|03|04|05)', following_text) or \
                   re.search(r'(?:Mar|Apr|May|03|04|05)[\-\s]2022', following_text):
                    spring_projects.append(line)

unique_projects = []
seen = set()
for proj in spring_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print(f"Projects starting in Spring 2022: {len(unique_projects)}")
for proj in unique_projects:
    print(f"  - {proj}")

result = {'count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
