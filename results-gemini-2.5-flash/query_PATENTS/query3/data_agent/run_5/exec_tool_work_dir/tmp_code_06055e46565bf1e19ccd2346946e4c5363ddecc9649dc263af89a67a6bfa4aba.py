code = """import json
import re

file_path = locals()['var_function-call-13532911310427381018']
with open(file_path, 'r') as f:
    univ_california_patents_data = json.load(f)

univ_california_publication_numbers = set()
for record in univ_california_patents_data:
    patents_info = record['Patents_info']
    match = re.search(r'pub\\. number (US-\d{7,8}-[A-Z]\d)', patents_info)
    if match:
        univ_california_publication_numbers.add(match.group(1))

print('__RESULT__:')
print(json.dumps(list(univ_california_publication_numbers)))"""

env_args = {'var_function-call-13930125777228040085': ['publicationinfo'], 'var_function-call-1621381890062432431': [], 'var_function-call-10802364016398363406': [], 'var_function-call-13532911310427381018': 'file_storage/function-call-13532911310427381018.json'}

exec(code, env_args)
