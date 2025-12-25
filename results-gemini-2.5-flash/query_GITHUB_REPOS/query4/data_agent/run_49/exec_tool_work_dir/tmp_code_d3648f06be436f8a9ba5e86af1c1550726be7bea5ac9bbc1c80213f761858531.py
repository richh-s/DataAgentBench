code = """import pandas as pd
import re
import json

def parse_language_description(description):
    languages = {}
    # Regex to find language and byte count pairs
    matches = re.findall(r'([A-Za-z0-9+# ]+?) \((\d{1,3}(?:,\d{3})* bytes)\)', description)
    for lang, bytes_str in matches:
        lang = lang.strip()
        bytes_str = bytes_str.replace(',', '').replace(' bytes', '')
        languages[lang] = int(bytes_str)

    if not languages:
        return None

    # Determine the main language by the highest byte count
    main_language = max(languages, key=languages.get)
    return main_language

language_data_path = locals()['var_function-call-1708783691274098257']

with open(language_data_path, 'r') as f:
    df_languages = pd.read_json(f)

df_languages['main_language'] = df_languages['language_description'].apply(parse_language_description)

non_python_repos = df_languages[df_languages['main_language'] != 'Python'].copy()

__RESULT__:
print(non_python_repos[['repo_name', 'main_language']].to_json(orient='records'))"""

env_args = {'var_function-call-4431169940473660024': ['languages', 'repos', 'licenses'], 'var_function-call-900972872601352991': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1708783691274098257': 'file_storage/function-call-1708783691274098257.json'}

exec(code, env_args)
