code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-9475326180653849631']
with open(file_path, 'r') as f:
    language_data = json.load(f)

def get_main_language(description):
    languages = re.findall(r'([A-Za-z]+) \(([0-9,]+) bytes\)', description)
    if not languages:
        return None
    
    main_lang = None
    max_bytes = -1
    for lang, bytes_str in languages:
        bytes_count = int(bytes_str.replace(',', ''))
        if bytes_count > max_bytes:
            max_bytes = bytes_count
            main_lang = lang
    return main_lang

processed_data = []
for item in language_data:
    repo_name = item['repo_name']
    language_description = item['language_description']
    main_language = get_main_language(language_description)
    if main_language and main_language != 'Python':
        processed_data.append({'repo_name': repo_name, 'main_language': main_language})

df = pd.DataFrame(processed_data)
result = df.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9475326180653849631': 'file_storage/function-call-9475326180653849631.json'}

exec(code, env_args)
