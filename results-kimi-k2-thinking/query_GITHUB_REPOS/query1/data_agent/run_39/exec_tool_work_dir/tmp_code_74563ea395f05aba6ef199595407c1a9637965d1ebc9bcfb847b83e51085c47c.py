code = """import json
import re

# Read the languages data
languages_file = locals()['var_functions.query_db:28']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Read the README data
readme_file = locals()['var_functions.query_db:20']
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Identify repositories that don't use Python
# A repository doesn't use Python if:
# 1. Python is not mentioned in language_description
#   OR
# 2. Python is mentioned but is not the primary language (has smaller byte count)

non_python_repos = set()
python_repos = set()

copyright_pattern = re.compile(r'(copyright|©|Copyright)', re.IGNORECASE)

for lang_record in languages_data:
    repo_name = lang_record['repo_name']
    lang_desc = lang_record['language_description']
    
    # Check if Python is mentioned
    if 'ython' in lang_desc:  # Catches both "Python" and "python"
        # Python is mentioned - need to check if it's the primary language
        # Extract byte counts from description
        bytes_match = re.findall(r'(?i)(\w+)\s*\(([\d,]+)\s*bytes?\)', lang_desc)
        
        if bytes_match:
            max_bytes = 0
            max_lang = ''
            
            for lang, byte_str in bytes_match:
                bytes_val = int(byte_str.replace(',', ''))
                if bytes_val > max_bytes:
                    max_bytes = bytes_val
                    max_lang = lang
            
            if max_lang and 'ython' not in max_lang:
                # Python is mentioned but not the primary language
                non_python_repos.add(repo_name)
            elif max_lang and 'ython' in max_lang:
                # Python is the primary language
                python_repos.add(repo_name)
        else:
            # Can't parse byte counts - check if Python appears as "mainly written in Python" or similar
            if 'mainly written in' in lang_desc and 'ython' in lang_desc.lower():
                python_repos.add(repo_name)
            elif 'majority of the code' in lang_desc and 'ython' in lang_desc.lower():
                python_repos.add(repo_name)
            else:
                # Ambiguous case - treat as non-Python to be conservative
                non_python_repos.add(repo_name)
    else:
        # Python not mentioned in language description
        non_python_repos.add(repo_name)

# Now check which non-Python repositories have README.md files with copyright
non_python_repos_with_readme = []
readme_repos = set(record['sample_repo_name'] for record in readme_data)

readme_with_copyright = 0
total_non_python_readme = 0

for readme_record in readme_data:
    repo_name = readme_record['sample_repo_name']
    
    # Only consider repositories that don't use Python
    if repo_name in non_python_repos and repo_name not in python_repos:
        total_non_python_readme += 1
        
        if 'content' in readme_record and readme_record['content']:
            if copyright_pattern.search(readme_record['content']):
                readme_with_copyright += 1
                non_python_repos_with_readme.append({
                    'repo_name': repo_name,
                    'has_copyright': True
                })

# Calculate statistics
result = {
    'total_non_python_repos': len(non_python_repos),
    'total_python_repos': len(python_repos),
    'non_python_repos_with_readme_files': total_non_python_readme,
    'non_python_readme_with_copyright': readme_with_copyright,
    'proportion_with_copyright': readme_with_copyright / total_non_python_readme if total_non_python_readme > 0 else 0,
    'sample_non_python_copyright_repos': non_python_repos_with_readme[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.list_db:4': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'total_repos': '400000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [{'total_readme': '195'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:26': {'total_readme_files': 195, 'copyright_count': 23, 'proportion_with_copyright': 0.11794871794871795, 'sample_records': [{'repo_name': 'rtrouton/rtrouton_scripts', 'has_copyright': False}, {'repo_name': 'DynamoRIO/dynamorio', 'has_copyright': False}, {'repo_name': 'ninja-ide/ninja-ide', 'has_copyright': False}, {'repo_name': 'sclorg/rhscl-dockerfiles', 'has_copyright': False}, {'repo_name': 'cwilso/midi-synth', 'has_copyright': False}]}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
