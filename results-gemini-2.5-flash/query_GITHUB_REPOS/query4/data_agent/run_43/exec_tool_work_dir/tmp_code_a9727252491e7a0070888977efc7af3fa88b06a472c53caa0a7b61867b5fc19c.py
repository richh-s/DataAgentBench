code = """import pandas as pd
import json
import re

language_data = json.loads(open(locals()['var_function-call-15701927023968665033'], 'r').read())
df_languages = pd.DataFrame(language_data)

def get_main_language(description):
    languages = re.findall(r'([A-Za-z0-9+#]+) \(([0-9,]+) bytes\)', description)
    if not languages:
        return None
    
    # Convert bytes to int for comparison
    languages = [(lang, int(bytes_str.replace(',', ''))) for lang, bytes_str in languages]
    
    # Sort by bytes in descending order to find the main language
    languages.sort(key=lambda x: x[1], reverse=True)
    
    return languages[0][0] if languages else None

df_languages['main_language'] = df_languages['language_description'].apply(get_main_language)

non_python_repos = df_languages[df_languages['main_language'] != 'Python']
repo_names_non_python = non_python_repos['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(repo_names_non_python))"""

env_args = {'var_function-call-15701927023968665033': 'file_storage/function-call-15701927023968665033.json'}

exec(code, env_args)
