code = """import json
import pandas as pd
import re

languages_data = json.load(open(locals()['var_function-call-11167423624507883408']))
df_languages = pd.DataFrame(languages_data)

def extract_main_language(description):
    languages_bytes = {}
    matches = re.findall(r'(\w+) \((\d+) bytes\)', description)
    for lang, bytes_str in matches:
        languages_bytes[lang] = int(bytes_str)

    if not languages_bytes:
        return None

    main_language = max(languages_bytes, key=languages_bytes.get)
    return main_language

df_languages['main_language'] = df_languages['language_description'].apply(extract_main_language)
non_python_repos = df_languages[df_languages['main_language'] != 'Python']
repo_names_non_python = non_python_repos['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(repo_names_non_python))"""

env_args = {'var_function-call-4786600211105115112': [{'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-11167423624507883408': 'file_storage/function-call-11167423624507883408.json'}

exec(code, env_args)
