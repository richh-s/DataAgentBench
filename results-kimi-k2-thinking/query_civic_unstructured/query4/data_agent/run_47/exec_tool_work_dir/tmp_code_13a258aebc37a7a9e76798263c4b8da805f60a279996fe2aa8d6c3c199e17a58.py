code = """import json
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

spring_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'Spring' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line.isupper() and len(line) > 15 and not line.startswith('PAGE'):
                if 'AGENDA' not in line and 'PUBLIC WORKS' not in line and 'COMMISSION' not in line:
                    following = '\n'.join(lines[i:i+15])
                    if '2022' in following and 'Spring' in following:
                        spring_projects.add(line)

result_data = {'count': len(spring_projects), 'projects': sorted(list(spring_projects))}
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
