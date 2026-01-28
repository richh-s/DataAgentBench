code = """# Load the commit data
commits_data = var_functions.query_db:10

# Load the language data
languages_data = var_functions.query_db:8

# If languages_data is a file path string, read the JSON file
if isinstance(languages_data, str):
    f = open(languages_data, 'r')
    file_content = f.read()
    f.close()
    languages_data = eval(file_content)

# Create commit count dictionary
commit_dict = {}
for item in commits_data:
    repo_name = item.get('repo_name', '')
    commit_count = int(item.get('commit_count', 0))
    commit_dict[repo_name] = commit_count

# Function to extract primary language
def get_primary_language(desc):
    if not desc:
        return None
    
    import re
    # Find all occurrences of "Language (X bytes)"
    pattern = r'([A-Za-z\+#]+)\s*\(([\d,]+)\s+bytes\)'
    matches = re.findall(pattern, desc)
    
    if not matches:
        return None
    
    # Find language with max bytes
    max_bytes = -1
    max_lang = None
    for lang, bytes_str in matches:
        byte_count = int(bytes_str.replace(',', ''))
        if byte_count > max_bytes:
            max_bytes = byte_count
            max_lang = lang
    
    return max_lang

# Build results list
results = []
for lang_item in languages_data:
    repo_name = lang_item.get('repo_name', '')
    lang_desc = lang_item.get('language_description', '')
    
    primary_lang = get_primary_language(lang_desc)
    commit_count = commit_dict.get(repo_name, 0)
    
    # Only include repos that are not Python and have commits
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

# Extract only repo names
final_result = [repo['repo_name'] for repo in top_5]

# Create JSON string
import json
result_json = json.dumps(final_result)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['commits', 'contents', 'files'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
