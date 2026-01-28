code = """import json

# Load language data
lang_file = var_functions.query_db:0
with open(lang_file, 'r') as f:
    languages_data = json.load(f)

# Load commit data
commit_data = var_functions.query_db:10

# Identify repositories whose main language is NOT Python
non_python_repos = set()

for item in languages_data:
    repo_name = item['repo_name']
    language_description = item['language_description']
    
    # If Python is not mentioned at all, it's non-Python
    if 'Python' not in language_description:
        non_python_repos.add(repo_name)
    else:
        # Check if Python is the main language by byte count
        import re
        
        # Extract language-byte pairs
        pattern = r'(\w+)\s*\((\d+)\s+bytes\)'
        matches = re.findall(pattern, language_description)
        
        if matches:
            # Find language with max bytes
            max_lang = max(matches, key=lambda x: int(x[1]))[0]
            if max_lang != 'Python':
                non_python_repos.add(repo_name)
        else:
            # Check phrasing like "mainly written in Python"
            if "mainly written in Python" not in language_description:
                non_python_repos.add(repo_name)

# Filter commit data for non-Python repos
filtered_commits = []
for commit_item in commit_data:
    if commit_item['repo_name'] in non_python_repos:
        filtered_commits.append({
            'repo_name': commit_item['repo_name'],
            'commit_count': int(commit_item['commit_count'])
        })

# Sort by commit count descending
filtered_commits.sort(key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5 = filtered_commits[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
