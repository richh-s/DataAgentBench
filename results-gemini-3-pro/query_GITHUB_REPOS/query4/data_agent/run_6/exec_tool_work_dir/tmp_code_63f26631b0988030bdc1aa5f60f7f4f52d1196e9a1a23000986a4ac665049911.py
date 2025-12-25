code = """import json
import re

# Load languages data
with open(locals()['var_function-call-8999517540046935819'], 'r') as f:
    languages_data = json.load(f)

# Load commit counts
commit_counts_data = locals()['var_function-call-17404398676993255548']
# commit_counts_data is a list of dicts: [{'repo_name': '...', 'commit_count': '...'}]
# Convert commit_count to int
commit_counts = {item['repo_name']: int(item['commit_count']) for item in commit_counts_data}

# Function to parse language description and find main language
def get_main_language(desc):
    if not desc:
        return None
    # Find all matches of "Language (Bytes bytes)"
    # Allow spaces in language names just in case, but usually followed by " ("
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\.\s]+) \(([0-9,]+) bytes\)', desc)
    
    max_bytes = -1
    main_lang = None
    
    for lang, bytes_str in matches:
        # Clean up language name (trim whitespace)
        lang = lang.strip()
        # Remove commas from bytes and convert to int
        byte_count = int(bytes_str.replace(',', ''))
        
        if byte_count > max_bytes:
            max_bytes = byte_count
            main_lang = lang
            
    return main_lang

# Process languages
repo_languages = {}
for item in languages_data:
    repo = item['repo_name']
    desc = item['language_description']
    main_lang = get_main_language(desc)
    repo_languages[repo] = main_lang

# Combine and filter
results = []
for repo, count in commit_counts.items():
    main_lang = repo_languages.get(repo)
    
    # If main_lang is missing, we might assume it's not Python or skip. 
    # But usually we should have metadata. If not found, safe to skip or treat as unknown.
    # The requirement is "whose main language is not Python". 
    # If main_lang is None (unknown), it is technically "not Python", but let's stick to knowns.
    # However, if the repo is not in languages table, we can't determine language.
    
    if main_lang and main_lang != 'Python':
        results.append({'repo_name': repo, 'commit_count': count, 'main_language': main_lang})

# Sort by commit count descending
results.sort(key=lambda x: x['commit_count'], reverse=True)

# Get top 5
top_5 = [item['repo_name'] for item in results[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-1846333013294576427': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-17404398676993255548': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-8999517540046935819': 'file_storage/function-call-8999517540046935819.json'}

exec(code, env_args)
