code = """import json
import os

# Access the file path from the storage variable
file_path = var_functions.query_db_6  # This should be the path to the JSON file

print(f"File path: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

# If it's a string path, read it
if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        languages_data = json.load(f)
    print(f"Loaded {len(languages_data)} records")
    
    # Function to check if Python is mentioned in the language description
    def contains_python(lang_desc):
        return 'Python' in lang_desc
    
    # Count Python vs non-Python repos
    python_repos = []
    non_python_repos = []
    
    for item in languages_data:
        repo_name = item['repo_name']
        lang_desc = item['language_description']
        
        if contains_python(lang_desc):
            python_repos.append(repo_name)
        else:
            non_python_repos.append(repo_name)
    
    result = {
        'total_repos': len(languages_data),
        'python_repos_count': len(python_repos),
        'non_python_repos_count': len(non_python_repos),
        'python_repos_sample': python_repos[:10],
        'non_python_repos_sample': non_python_repos[:10]
    }
else:
    # If it's already loaded as a variable
    languages_data = var_functions.query_db_6
    print(f"Direct variable with {len(languages_data)} records")
    
    # Function to check if Python is mentioned in the language description
    def contains_python(lang_desc):
        return 'Python' in lang_desc
    
    # Count Python vs non-Python repos
    python_repos = []
    non_python_repos = []
    
    for item in languages_data:
        repo_name = item['repo_name']
        lang_desc = item['language_description']
        
        if contains_python(lang_desc):
            python_repos.append(repo_name)
        else:
            non_python_repos.append(repo_name)
    
    result = {
        'total_repos': len(languages_data),
        'python_repos_count': len(python_repos),
        'non_python_repos_count': len(non_python_repos),
        'python_repos_sample': python_repos[:10],
        'non_python_repos_sample': non_python_repos[:10]
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
