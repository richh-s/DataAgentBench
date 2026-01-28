code = """import json

# Check what variables are available
print("Available variables:", list(locals().keys()))

# Print info about the query result
if 'var_functions.query_db_6' in locals():
    languages_data = var_functions.query_db_6
    print(f"Languages data type: {type(languages_data)}")
    print(f"Languages data length: {len(languages_data) if hasattr(languages_data, '__len__') else 'No length'}")
    print(f"First item: {languages_data[0] if languages_data else 'Empty'}")
    
    # Count Python vs non-Python repos
    non_python_repos = []
    python_repos = []
    
    for row in languages_data:
        repo_name = row['repo_name']
        lang_desc = row['language_description'].lower()
        
        if 'python' in lang_desc:
            python_repos.append(repo_name)
        else:
            non_python_repos.append(repo_name)
    
    print(f"Total repos: {len(languages_data)}")
    print(f"Python repos: {len(python_repos)}")
    print(f"Non-Python repos: {len(non_python_repos)}")
    
    # Save result
    result = {
        'non_python_repos': non_python_repos,
        'non_python_count': len(non_python_repos),
        'total_count': len(languages_data)
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print("var_functions.query_db_6 not found")
    print('__RESULT__:')
    print('{"error": "variable not found"}')"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'status': 'checked variables'}}

exec(code, env_args)
