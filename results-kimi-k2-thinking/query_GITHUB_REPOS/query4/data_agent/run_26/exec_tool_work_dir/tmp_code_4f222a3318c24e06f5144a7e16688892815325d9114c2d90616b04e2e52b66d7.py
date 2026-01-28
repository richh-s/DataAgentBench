code = """import json
import re

# Get the data
languages_file_path = locals()['var_functions.query_db:6']
commits_data = locals()['var_functions.query_db:5']

# Load languages data from file
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Parse language descriptions to extract main language
repo_languages = {}
for row in languages_data:
    repo_name = row['repo_name']
    lang_desc = row['language_description']
    
    # Pattern to match: Language (bytes)
    lang_pattern = r'(\w+)\s*\((\d+(?:,\d+)*)\s*bytes?\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    if matches:
        # Convert to dict of language -> bytes
        lang_bytes = {}
        for lang, byte_str in matches:
            byte_count = int(byte_str.replace(',', ''))
            lang_bytes[lang] = byte_count
        
        # Get main language (highest byte count)
        if lang_bytes:
            main_lang = max(lang_bytes, key=lang_bytes.get)
            repo_languages[repo_name] = main_lang

# Create dict of commit counts
commit_counts = {row['repo_name']: int(row['commit_count']) for row in commits_data}

# Find repos where main language is not Python, ordered by commit count
non_python_repos = []
for repo, commits in commit_counts.items():
    main_lang = repo_languages.get(repo)
    if main_lang and main_lang != 'Python':
        non_python_repos.append((repo, commits, main_lang))

# Sort by commit count descending
non_python_repos.sort(key=lambda x: x[1], reverse=True)

# Get top 5
top_5 = non_python_repos[:5]

result = {
    'top_5_repos': [(repo, commits, lang) for repo, commits, lang in top_5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
