code = """import json
import re

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:11']
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Search for projects with 2022 Spring dates in the text
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for 2022-Spring or Spring 2022 patterns
    if '2022' in text and ('Spring' in text or 'spring' in text):
        # Extract potential project names from lines containing both 2022 and Spring
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and ('Spring' in line or 'spring' in line):
                # Clean the line
                clean_line = line.strip()
                if len(clean_line) > 10:
                    spring_2022_projects.append(clean_line)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_mentions': len(spring_2022_projects),
    'sample_lines': spring_2022_projects[:15]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
