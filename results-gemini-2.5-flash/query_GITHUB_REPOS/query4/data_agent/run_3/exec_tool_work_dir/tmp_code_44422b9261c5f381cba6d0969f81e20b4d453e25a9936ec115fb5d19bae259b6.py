code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-6648005358843189280'], 'r') as f:
    languages_data = json.load(f)

df_languages = pd.DataFrame(languages_data)

def get_main_language(description):
    if not isinstance(description, str):
        return None

    # Try to extract the main language by finding the language with the highest byte count
    language_bytes_pairs = []
    # Regex to find patterns like 'Language (Bytes)'
    matches = re.findall(r'([A-Za-z]+)\s+\(([0-9,]+)\s+bytes\)', description)
    for match in matches:
        language_name = match[0].strip()
        bytes_count = int(match[1].replace(',', ''))
        language_bytes_pairs.append((language_name, bytes_count))

    if language_bytes_pairs:
        # Sort by bytes count in descending order and pick the first one
        main_lang_info = sorted(language_bytes_pairs, key=lambda item: item[1], reverse=True)[0]
        return main_lang_info[0]
    else:
        # Fallback if no specific byte counts are found, try to find a single language mentioned first
        # This handles cases like 'This repository is mainly written in Ruby'
        match_main = re.search(r'(?:mainly written in|The majority of the code is in|While most of the project is built in)\s+([A-Za-z]+)', description)
        if match_main:
            return match_main.group(1).strip()
    return None

df_languages['main_language'] = df_languages['language_description'].apply(get_main_language)

non_python_repos = df_languages[df_languages['main_language'] != 'Python']
result = non_python_repos[['repo_name', 'main_language']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-6648005358843189280': 'file_storage/function-call-6648005358843189280.json', 'var_function-call-4624580587509127227': 'file_storage/function-call-4624580587509127227.json'}

exec(code, env_args)
