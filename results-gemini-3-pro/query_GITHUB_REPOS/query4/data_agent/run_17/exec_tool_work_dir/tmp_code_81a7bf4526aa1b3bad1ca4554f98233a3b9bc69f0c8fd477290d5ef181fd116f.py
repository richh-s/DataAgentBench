code = """import json
import re

# Load commit counts
commits_data = locals()['var_function-call-507962262134349788']

# Load languages data
languages_file_path = locals()['var_function-call-507962262134348277']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Convert languages_data to a dict for easy lookup
languages_map = {item['repo_name']: item['language_description'] for item in languages_data}

def get_main_language(description):
    # Regex to find "Language (bytes)" patterns
    # Examples: "Ruby (22,438 bytes)", "Shell (465 bytes)"
    matches = re.findall(r'([a-zA-Z\+\#\.]+(?: [a-zA-Z\+\#\.]+)*) \(([\d,]+) bytes\)', description)
    
    if not matches:
        return None
    
    max_bytes = -1
    main_lang = None
    
    for lang, bytes_str in matches:
        # distinct "The codebase includes: " or similar prefixes if caught by regex?
        # The regex captures the language name before " ("
        # We might capture "includes: Ruby" if not careful, but the space logic handles it?
        # Let's refine the regex.
        # The format seems to be ", Language (N bytes)" or "includes: Language (N bytes)"
        
        # Clean bytes string
        bytes_count = int(bytes_str.replace(',', ''))
        
        if bytes_count > max_bytes:
            max_bytes = bytes_count
            main_lang = lang.strip()
            
    return main_lang

filtered_repos = []

for repo in commits_data:
    name = repo['repo_name']
    count = int(repo['commit_count'])
    
    lang_desc = languages_map.get(name)
    if lang_desc:
        main_lang = get_main_language(lang_desc)
        if main_lang and main_lang.lower() != 'python':
            filtered_repos.append(repo['repo_name'])
    else:
        # If no language info, decide what to do. Maybe include or exclude?
        # Usually implies we can't determine if it is Python.
        # But given the problem statement, I should probably only include if I know it's not Python.
        # However, for top repos like linux, swift, etc., they likely have language info.
        pass

# We need top 5
top_5 = filtered_repos[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-13619765481203691763': ['commits', 'contents', 'files'], 'var_function-call-13619765481203693066': ['languages', 'repos', 'licenses'], 'var_function-call-507962262134349788': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-507962262134348277': 'file_storage/function-call-507962262134348277.json'}

exec(code, env_args)
