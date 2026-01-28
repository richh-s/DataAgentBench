code = """import json

# Load the MongoDB results
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Filter documents for 2022
spring_2022_projects = set()
for doc in civic_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if '2022' in filename or '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Identify potential project names (uppercase, reasonable length, not page numbers)
            if line.isupper() and len(line) > 15 and not line.startswith('PAGE'):
                # Skip header lines
                if 'AGENDA' not in line and 'PUBLIC WORKS' not in line and 'COMMISSION' not in line:
                    if 'MEETING' not in line and 'SUBJECT:' not in line and 'RECOMMENDED ACTION:' not in line:
                        # Check following lines for Spring 2022
                        look_ahead = '\n'.join(lines[i:i+20])
                        has_spring_2022 = ('Spring' in look_ahead and '2022' in look_ahead)
                        has_march_may_2022 = any(m in look_ahead for m in ['2022-03', '2022-04', '2022-05', '2022 Mar', '2022 Apr', '2022 May'])
                        if has_spring_2022 and 'Advertise' in look_ahead:
                            spring_2022_projects.add(line)
                        elif has_march_may_2022 and 'Advertise' in look_ahead:
                            spring_2022_projects.add(line)

result_list = sorted(list(spring_2022_projects))
print(f"Spring 2022 projects found: {len(result_list)}")
for proj in result_list:
    print(f"  - {proj}")

output = {'count': len(result_list), 'projects': result_list}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
