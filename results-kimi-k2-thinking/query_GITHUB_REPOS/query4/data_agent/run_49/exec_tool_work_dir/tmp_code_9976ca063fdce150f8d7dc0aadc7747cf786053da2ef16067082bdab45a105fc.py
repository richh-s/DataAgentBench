code = """import json

# Read the commit data from storage
commit_data = locals()['var_functions.query_db:12']

# Read the language data from storage
language_data_file = locals()['var_functions.query_db:10']

# Load language data
with open(language_data_file, 'r') as f:
    language_data = json.load(f)

# Create a dictionary mapping repo_name to its language info (for fast lookup)
language_dict = {item['repo_name']: item['language_description'] for item in language_data}

# Function to determine main language from language_description
def get_main_language(lang_desc):
    """Parse language description to find the main language (not Python)"""
    # Look for patterns like "Language (bytes)"
    import re
    
    # Find all language-byte pairs
    lang_pattern = r'([A-Za-z\+#]+)\s*\((\d+)\s*bytes?\)'
    matches = re.findall(lang_pattern, lang_desc)
    
    # If no matches found, try different pattern
    if not matches:
        lang_pattern = r'([A-Za-z\+#]+)\s*\((\d+)\s*Bytes?\)'
        matches = re.findall(lang_pattern, lang_desc)
    
    # Convert to dictionary and find language with max bytes
    if matches:
        lang_bytes = {lang: int(bytes_) for lang, bytes_ in matches}
        if lang_bytes:
            main_lang = max(lang_bytes, key=lang_bytes.get)
            return main_lang
    
    # If we can't parse, return None
    return None

# Filter repos whose main language is NOT Python
top_5_non_python = []
for item in commit_data[:5]:  # Start with top 5 from commits
    repo_name = item['repo_name']
    if repo_name in language_dict:
        main_lang = get_main_language(language_dict[repo_name])
        if main_lang and main_lang.lower() != 'python':
            top_5_non_python.append(repo_name)

print('__RESULT__:')
print(json.dumps(top_5_non_python))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:14': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
