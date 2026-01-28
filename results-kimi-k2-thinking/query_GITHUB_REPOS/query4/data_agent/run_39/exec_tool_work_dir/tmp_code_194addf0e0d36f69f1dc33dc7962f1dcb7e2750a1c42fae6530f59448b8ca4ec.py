code = """# Load the commit data (should be a list)
commits_data = var_functions.query_db:10

# Load the language data
languages_data = var_functions.query_db:8
# If languages_data is a file path string, read the JSON file
if isinstance(languages_data, str):
    f = open(languages_data, 'r')
    file_content = f.read()
    f.close()
    # Parse JSON manually (avoiding import json)
    languages_data = eval(file_content)  # Using eval as a workaround since we can't import json

# Debug info
print("Commits data type:", type(commits_data))
print("Languages data type:", type(languages_data))
print("Sample commits:", str(commits_data[:2]) if commits_data else "Empty")
print("Sample languages:", str(languages_data[:2]) if languages_data else "Empty")

# Create a dictionary for quick lookup of commit counts
commit_dict = {}
for item in commits_data:
    repo_name = item.get('repo_name', '')
    commit_count = int(item.get('commit_count', 0))
    commit_dict[repo_name] = commit_count

# Function to extract primary language from description
def get_primary_language(desc):
    if not desc:
        return None
    
    # Find all language-byte pairs like "Ruby (22,438 bytes)"
    import sys
    lang_bytes = {}
    
    # Simple parsing without regex
    parts = desc.split(",")
    for part in parts:
        # Look for pattern: Language (X bytes)
        open_paren = part.find("(")
        close_paren = part.find(")")
        if open_paren > 0 and close_paren > open_paren:
            lang = part[:open_paren].strip()
            # Extract number
            num_part = part[open_paren+1:close_paren]
            num_start = -1
            for i, char in enumerate(num_part):
                if char.isdigit():
                    num_start = i
                    break
            if num_start >= 0:
                num_end = num_start
                while num_end < len(num_part) and num_part[num_end].isdigit():
                    num_end += 1
                try:
                    bytes_count = int(num_part[num_start:num_end])
                    lang_bytes[lang] = bytes_count
                except:
                    pass
    
    # Find language with max bytes
    if lang_bytes:
        max_lang = max(lang_bytes, key=lang_bytes.get)
        return max_lang
    return None

# Build list of repos with their primary language and commit count
results = []
for lang_item in languages_data:
    repo_name = lang_item.get('repo_name', '')
    lang_desc = lang_item.get('language_description', '')
    
    primary_lang = get_primary_language(lang_desc)
    commit_count = commit_dict.get(repo_name, 0)
    
    if primary_lang and primary_lang != 'Python' and commit_count > 0:
        results.append({
            'repo_name': repo_name,
            'primary_language': primary_lang,
            'commit_count': commit_count
        })

# Sort by commit count descending
results.sort(key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5 = results[:5]
print("\nTop 5 non-Python repos:")
for repo in top_5:
    print(f"  {repo['repo_name']}: {repo['commit_count']} commits ({repo['primary_language']})")

# Extract just the repo names
repo_names = [repo['repo_name'] for repo in top_5]

# Convert to string representation (since we can't use json.dumps)
result_str = str(repo_names)

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
