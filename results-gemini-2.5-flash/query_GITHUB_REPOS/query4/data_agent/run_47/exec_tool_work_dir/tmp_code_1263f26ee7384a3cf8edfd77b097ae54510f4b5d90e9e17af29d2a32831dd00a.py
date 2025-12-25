code = """import pandas as pd
import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-17345825887054219745'], 'r') as f:
    languages_data = json.load(f)

df_languages = pd.DataFrame(languages_data)

def extract_main_language(description):
    languages = {}
    matches = re.findall(r'(\w+)\s+\((\d+)\s+bytes\)', description)
    for lang, bytes_str in matches:
        languages[lang] = int(bytes_str)
    
    if not languages:
        return None
    
    main_language = max(languages, key=languages.get)
    return main_language

df_languages['main_language'] = df_languages['language_description'].apply(extract_main_language)
non_python_repos = df_languages[df_languages['main_language'] != 'Python']['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-17345825887054219745': 'file_storage/function-call-17345825887054219745.json'}

exec(code, env_args)
