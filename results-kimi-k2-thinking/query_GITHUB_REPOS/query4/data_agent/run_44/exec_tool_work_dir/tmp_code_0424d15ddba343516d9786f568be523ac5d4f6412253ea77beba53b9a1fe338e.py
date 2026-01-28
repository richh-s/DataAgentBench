code = """import json
import re

# Load the language data from the file
lang_file_path = var_functions.query_db:0
with open(lang_file_path, 'r') as f:
    languages_data = json.load(f)

# Load the commit count data
commit_counts = var_functions.query_db:2

# Parse languages data to find main language for each repository
repos_main_lang = []
for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    # Extract language-byte pairs using regex
    # Pattern matches: Language (bytes)
    lang_pattern = r'(\w+)\s*\((\d+)\s*bytes?\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    if matches:
        # Find the language with highest byte count
        max_bytes = 0
        main_lang = None
        for lang, bytes_str in matches:
            bytes_count = int(bytes_str)
            if bytes_count > max_bytes:
                max_bytes = bytes_count
                main_lang = lang
        
        repos_main_lang.append({
            'repo_name': repo_name,
            'main_language': main_lang,
            'main_language_bytes': max_bytes
        })

# Filter out repositories whose main language is Python
non_python_repos = [repo for repo in repos_main_lang if repo['main_language'].lower() != 'python']

# Create a dictionary of commit counts for easy lookup
commit_counts_dict = {item['repo_name']: int(item['commit_count']) for item in commit_counts}

# Filter to only repositories we have commit data for, and add commit counts
repos_with_commits = []
for repo in non_python_repos:
    if repo['repo_name'] in commit_counts_dict:
        repos_with_commits.append({
            'repo_name': repo['repo_name'],
            'main_language': repo['main_language'],
            'commit_count': commit_counts_dict[repo['repo_name']]
        })

# Sort by commit count descending
sorted_repos = sorted(repos_with_commits, key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5_repos = sorted_repos[:5]

# Extract just the repository names
result = [repo['repo_name'] for repo in top_5_repos]

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
