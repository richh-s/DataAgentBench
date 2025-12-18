code = """import json
import pandas as pd
import re

# Load the full language data
with open(locals()['var_function-call-994111513243905501'], 'r') as f:
    language_data = json.load(f)

# Create a list to store processed language data
processed_languages = []

for record in language_data:
    repo_name = record['repo_name']
    description = record['language_description']

    # Regex to find language and byte count
    matches = re.findall(r'([A-Za-z0-9+#-]+)(?: \(| \()([0-9,]+) bytes', description)

    main_language = None
    max_bytes = -1

    if matches:
        for lang, byte_str in matches:
            # Clean up language name and convert byte count to int
            lang = lang.strip().replace('While most of the project is built in ', '').replace('The majority of the code is in ', '').replace('This repository is mainly written in ', '').replace('The codebase includes: ', '').replace('additional code in ', '')
            lang = lang.replace('(','') # Remove any stray parenthesis
            lang = lang.strip()
            bytes_count = int(byte_str.replace(',', ''))

            if bytes_count > max_bytes:
                max_bytes = bytes_count
                main_language = lang
    else:
        # Handle cases where language description might be like "Shell (40,034 bytes)"
        single_lang_match = re.search(r'([A-Za-z0-9+#-]+) \(([0-9,]+) bytes\)', description)
        if single_lang_match:
            main_language = single_lang_match.group(1).strip()
            max_bytes = int(single_lang_match.group(2).replace(',', ''))
        else:
            # Fallback for descriptions like "Ruby" without byte counts if needed, but not strictly required by the prompt
            pass

    if main_language:
        processed_languages.append({'repo_name': repo_name, 'main_language': main_language})

# Filter out repositories where the main language is Python
non_python_repos = [repo for repo in processed_languages if repo['main_language'] != 'Python']

df_non_python_repos = pd.DataFrame(non_python_repos)

print('__RESULT__:')
print(df_non_python_repos.to_json(orient='records'))"""

env_args = {'var_function-call-18166555447577494955': [{'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-994111513243905501': 'file_storage/function-call-994111513243905501.json'}

exec(code, env_args)
