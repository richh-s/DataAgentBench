code = """import json

# The result is stored under the key 'functions.query_db:0' which contains the file path
result_file = locals()['functions.query_db:0']
print(f"Reading from file: {result_file}")

with open(result_file, 'r') as f:
    languages_data = json.load(f)

print(f"Total repositories: {len(languages_data)}")

# Filter repositories whose main language is NOT Python
non_python_repos = []
for item in languages_data:
    repo_name = item['repo_name']
    language_description = item['language_description']
    
    # Check if Python is the main language
    if 'Python' not in language_description:
        non_python_repos.append(repo_name)
    else:
        # Extract the main language by looking for the language with highest bytes
        import re
        
        # Find all language-byte pairs
        pattern = r'(\w+)\s*\((\d+)\s+bytes\)'
        matches = re.findall(pattern, language_description)
        
        if matches:
            # Find the language with max bytes
            max_lang = max(matches, key=lambda x: int(x[1]))[0]
            if max_lang != 'Python':
                non_python_repos.append(repo_name)
        else:
            # If we can't parse, check if Python is mentioned as "mainly written in"
            if "mainly written in Python" not in language_description:
                non_python_repos.append(repo_name)

print("__RESULT__:")
print(json.dumps({
    'non_python_repo_count': len(non_python_repos),
    'sample_repos': non_python_repos[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
