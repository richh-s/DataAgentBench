code = """import json

result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    documents = json.load(f)

print('Found', len(documents), 'documents')

projects = []

for doc in documents:
    text = doc['text'].lower()
    if 'park' in text and 'completed' in text and '2022' in text:
        # Simple extraction
        lines = doc['text'].split('\n')
        for line in lines:
            if any(word in line.lower() for word in ['park','playground']):
                if 'completed' in doc['text'].lower() and '2022' in doc['text'].lower():
                    projects.append(line.strip())
                    break

unique_projects = list(set([p for p in projects if len(p) > 5]))
print('Found projects:', len(unique_projects))

result = json.dumps(unique_projects[:20])
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
