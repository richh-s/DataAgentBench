code = """import json

# Load the language data to get non-Python repos
lang_file = locals()['var_functions.query_db:5']
with open(lang_file, 'r') as f:
    language_data = json.load(f)

# Create a set of non-Python repository names
non_python_repos = set(
    item['repo_name'] for item in language_data 
    if not ('python' in item['language_description'].lower())
)

# Load the README data
readme_file = locals()['var_functions.query_db:18']
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Process READMEs - filter to non-Python repos and check for copyright
import re

copyright_keywords = ['copyright', '©', '(c)', 'all rights reserved']
readme_count = 0
copyright_readme_count = 0
non_python_readme_data = []

for item in readme_data:
    repo_name = item['sample_repo_name']
    if repo_name in non_python_repos:
        readme_count += 1
        content = item['content'] or ''
        has_copyright = any(keyword in content.lower() for keyword in copyright_keywords)
        if has_copyright:
            copyright_readme_count += 1
            non_python_readme_data.append({
                'repo_name': repo_name,
                'has_copyright': True,
                'sample_path': item['sample_path']
            })
        else:
            non_python_readme_data.append({
                'repo_name': repo_name,
                'has_copyright': False,
                'sample_path': item['sample_path']
            })

proportion = copyright_readme_count / readme_count if readme_count > 0 else 0

print('__RESULT__:')
print(json.dumps({
    'total_non_python_readmes': readme_count,
    'readmes_with_copyright': copyright_readme_count,
    'proportion_with_copyright': proportion,
    'sample_readmes_with_copyright': [item for item in non_python_readme_data if item['has_copyright']][:5],
    'sample_readmes_without_copyright': [item for item in non_python_readme_data if not item['has_copyright']][:5]
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_repositories': 3325634, 'python_repositories': 550905, 'non_python_repositories': 2774729, 'sample_python_repos': [{'repo_name': 'mattf-horton/metron', 'language_description': 'The majority of the code is in Java (5,520,754 bytes), followed by HTML (1,788,682 bytes), TypeScript (933,459 bytes), CSS (763,669 bytes), Python (269,546 bytes), JavaScript (172,067 bytes), Shell (161,784 bytes), C (49,573 bytes), Ruby (19,141 bytes), ANTLR (12,811 bytes), Scala (2,700 bytes), Makefile (2,579 bytes).'}, {'repo_name': 'ottobackwards/metron', 'language_description': 'This repository is mainly written in Java (7,558,475 bytes), with additional code in HTML (2,153,404 bytes), TypeScript (1,224,366 bytes), CSS (783,007 bytes), Python (356,176 bytes), Shell (221,579 bytes), JavaScript (184,903 bytes), C (49,573 bytes), Ruby (26,376 bytes), Dockerfile (16,690 bytes), ANTLR (12,811 bytes), Scala (2,700 bytes), Makefile (2,579 bytes), TSQL (2,401 bytes).'}, {'repo_name': 'GBGamer/rust', 'language_description': 'The majority of the code is in Rust (21,265,061 bytes), followed by C (391,581 bytes), Makefile (306,032 bytes), Shell (270,571 bytes), Python (197,397 bytes), Yacc (81,068 bytes), C++ (64,107 bytes), JavaScript (45,051 bytes), CSS (27,753 bytes), ANTLR (27,014 bytes), Pascal (13,456 bytes), Lex (9,270 bytes), Puppet (3,296 bytes), HTML (496 bytes), Awk (271 bytes), PHP (265 bytes).'}], 'sample_non_python_repos': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}]}, 'var_functions.list_db:12': ['commits', 'contents', 'files'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
