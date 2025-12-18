code = """import pandas as pd
import re

df_languages = pd.read_json(locals()['var_function-call-8309339118835681289'])

def parse_languages(description):
    if not isinstance(description, str):
        return []
    language_regex = '([A-Za-z+#]+(?: [A-Za-z+#]+)*) \\((\\d+,?\\d* bytes)'
    matches = re.findall(language_regex, description)
    parsed_languages = []
    for lang, bytes_str in matches:
        bytes_count = int(bytes_str.replace(' bytes', '').replace(',', ''))
        parsed_languages.append({'language': lang.strip(), 'bytes': bytes_count})
    return parsed_languages

df_languages['parsed_languages'] = df_languages['language_description'].apply(parse_languages)

def get_primary_language(parsed_languages):
    if not parsed_languages:
        return None
    primary_lang = sorted(parsed_languages, key=lambda x: x['bytes'], reverse=True)
    return primary_lang[0]['language'] if primary_lang else None

df_languages['primary_language'] = df_languages['parsed_languages'].apply(get_primary_language)

non_python_repos = df_languages[df_languages['primary_language'] != 'Python']['repo_name'].tolist()

import json
print('__RESULT__:')
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-8309339118835681289': 'file_storage/function-call-8309339118835681289.json'}

exec(code, env_args)
