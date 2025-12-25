code = """import json
import re

languages_data = json.load(open(locals()['var_function-call-11062886338066533241'], 'r'))

repo_main_language = {}

for entry in languages_data:
    repo_name = entry['repo_name']
    language_description = entry['language_description']

    languages_bytes = {}
    matches = re.findall(r'(\w+) \((\d+ bytes)\)', language_description)
    for lang, bytes_str in matches:
        languages_bytes[lang] = int(bytes_str.replace(' bytes', ''))

    if languages_bytes:
        # Find the language with the maximum bytes
        main_language = max(languages_bytes, key=languages_bytes.get)
        repo_main_language[repo_name] = main_language

non_python_repos = [repo for repo, lang in repo_main_language.items() if lang != 'Python']

print("__RESULT__:")
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-3592447668533597204': ['languages', 'repos', 'licenses'], 'var_function-call-16393034236963869547': ['commits', 'contents', 'files'], 'var_function-call-11062886338066533241': 'file_storage/function-call-11062886338066533241.json'}

exec(code, env_args)
