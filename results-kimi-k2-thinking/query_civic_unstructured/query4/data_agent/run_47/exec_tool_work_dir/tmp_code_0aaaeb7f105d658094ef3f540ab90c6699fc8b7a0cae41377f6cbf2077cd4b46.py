code = """import json
import os

result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total documents: {len(civic_docs)}")

all_2022_refs = []
for i, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    if '2022' in text and ('Spring' in text or 'Advertise' in text or 'Begin' in text or 'Complete' in text):
        all_2022_refs.append((i, doc))

print(f"Docs with 2022 and time references: {len(all_2022_refs)}")

spring_projects = []
for doc_idx, doc in all_2022_refs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if line.isupper() and len(line) > 15:
            skip_words = ['page', 'agenda item', 'public works', 'commission', 'meeting', 'subject:', 'recommended action:', 'prepared by', 'approved by', 'date prepared', 'discussion:']
            should_skip = any(word in line.lower() for word in skip_words)
            if not should_skip:
                following = ' '.join(lines[i:i+10])
                if '2022' in following and 'Spring' in following:
                    spring_projects.append(line)

uniq = []
seen = set()
for p in spring_projects:
    if p not in seen:
        seen.add(p)
        uniq.append(p)

print(f"Spring 2022 projects found: {len(uniq)}")
print("Names:")
for p in uniq[:10]:
    print("  -", p)

result = {'count': len(uniq), 'projects': uniq}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
