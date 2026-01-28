code = """# Access the languages data from storage
languages_data = locals()['var_functions.query_db:14']

# Process the data to identify repositories that do NOT use Python
import json
import re

non_python_repos = []
python_repos = []

for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    # Check if Python is mentioned in the language description
    if 'python' in lang_desc.lower():
        python_repos.append(repo_name)
    else:
        non_python_repos.append(repo_name)

print("__RESULT__:")
print(json.dumps({
    "total_repos": len(languages_data),
    "python_repos": len(python_repos),
    "non_python_repos": len(non_python_repos),
    "sample_non_python": non_python_repos[:5]
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.execute_python:2': 'Sample data loaded', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': 38, 'var_functions.list_db:12': ['languages', 'repos', 'licenses'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
