code = """import json
import re

# Read the language data from the JSON file
with open('var_functions.query_db:6', 'r') as f:
    languages_data = json.load(f)

# Read the commits data
commit_data = locals()['var_functions.query_db:5']

# Parse language descriptions
repo_languages = {}
for row in languages_data:
    repo_name = row['repo_name']
    lang_desc = row['language_description']
    
    # Extract language names and byte counts using regex
    # Pattern matches: Language (bytes) 
    lang_pattern = r'(\w+)\s*\((\d+(?:,\d+)*)\s*bytes?\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    if matches:
        # Convert matches to dict of language -> bytes
        lang_bytes = {}
        for lang, byte_str in matches:
            # Remove commas and convert to int
            byte_count = int(byte_str.replace(',', ''))
            lang_bytes[lang] = byte_count
        
        # Find main language (highest byte count)
        if lang_bytes:
            main_lang = max(lang_bytes, key=lang_bytes.get)
            repo_languages[repo_name] = main_lang

# Create dict of commit counts from the query result
commit_counts = {}
for row in commit_data:
    commit_counts[row['repo_name']] = int(row['commit_count'])

print('__RESULT__:')
print(json.dumps({
    'sample_languages_parsed': dict(list(repo_languages.items())[:5]),
    'sample_commit_counts': dict(list(commit_counts.items())[:5]),
    'total_repos_with_languages': len(repo_languages),
    'total_repos_with_commits': len(commit_counts)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
