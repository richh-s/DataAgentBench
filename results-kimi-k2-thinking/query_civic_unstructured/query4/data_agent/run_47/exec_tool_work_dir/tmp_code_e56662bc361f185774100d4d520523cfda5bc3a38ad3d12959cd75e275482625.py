code = """import json
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)
print(f"Total documents: {len(civic_docs)}")
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line.isupper() and len(line) > 15 and not line.startswith('PAGE'):
                skip_terms = ['AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'MEETING', 'SUBJECT:', 'RECOMMENDED ACTION:']
                should_skip = False
                for term in skip_terms:
                    if term in line:
                        should_skip = True
                        break
                if not should_skip:
                    following = '\n'.join(lines[i:i+15])
                    if 'Spring' in following and '2022' in following:
                        spring_projects.append(line)

unique = list(set(spring_projects))
print(f"Spring 2022 projects: {len(unique)}")
result = {'count': len(unique), 'projects': unique}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
