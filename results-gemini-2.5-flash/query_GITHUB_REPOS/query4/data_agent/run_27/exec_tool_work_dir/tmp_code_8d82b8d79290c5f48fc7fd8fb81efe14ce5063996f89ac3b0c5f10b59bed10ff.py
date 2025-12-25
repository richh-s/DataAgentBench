code = """import json
import re

with open(locals()['var_function-call-9216244957271528698'], 'r') as f:
    language_data = json.load(f)

repo_main_languages = []
for entry in language_data:
    repo_name = entry['repo_name']
    description = entry['language_description']

    languages_bytes = {}
    # Regex to find 'Language (bytes)' patterns
    matches = re.findall(r'([a-zA-Z]+) \((\d{1,3}(?:,\d{3})*|\d+) bytes\)', description)

    for lang, byte_str in matches:
        bytes_count = int(byte_str.replace(',', ''))
        languages_bytes[lang] = bytes_count

    if not languages_bytes:
        continue

    # Determine the main language (language with the most bytes)
    main_language = max(languages_bytes, key=languages_bytes.get)
    main_language_bytes = languages_bytes[main_language]

    repo_main_languages.append({
        'repo_name': repo_name,
        'main_language': main_language,
        'main_language_bytes': main_language_bytes
    })

# Filter out repositories where the main language is Python
non_python_repos = [repo for repo in repo_main_languages if repo['main_language'] != 'Python']

print('__RESULT__:')
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-13197283897871611695': ['languages', 'repos', 'licenses'], 'var_function-call-16169134888971643462': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-9216244957271528698': 'file_storage/function-call-9216244957271528698.json', 'var_function-call-8861686383021131793': ['commits', 'contents', 'files']}

exec(code, env_args)
