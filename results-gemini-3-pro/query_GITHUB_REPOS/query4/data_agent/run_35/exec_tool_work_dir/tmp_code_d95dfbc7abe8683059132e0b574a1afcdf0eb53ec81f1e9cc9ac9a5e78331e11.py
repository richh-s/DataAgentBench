code = """import json
import re

# Load data
languages_file = locals()['var_function-call-11926634395432356297']
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

commits_data = locals()['var_function-call-12131814289532468915']

# Create a dictionary for languages
# repo_name -> language_description
lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

repo_commits = []
for item in commits_data:
    repo_name = item['repo_name']
    commit_count = int(item['commit_count'])
    
    if repo_name not in lang_map:
        # If no language info, we can't determine if it's Python or not. 
        # Assuming we skip or treat as not Python? 
        # Let's check if we have data for these repos.
        continue

    desc = lang_map[repo_name]
    
    # Parse description
    # Regex to find Language (Bytes bytes)
    # Handling comma in numbers
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\.]+(?: [a-zA-Z0-9\+\-\#\.]+)*) \((\d+(?:,\d+)*) bytes\)', desc)
    
    if not matches:
        continue
        
    # Calculate bytes for each language
    lang_bytes = {}
    for lang, bytes_str in matches:
        bytes_val = int(bytes_str.replace(',', ''))
        # Clean language name (it might capture leading words if my regex is loose, but based on structure it looks ok)
        # Structure is usually "...: Lang (bytes), Lang (bytes)." or "... in Lang (bytes)..."
        # The regex matches the immediate name before " (".
        # Let's refine if needed.
        # But actually, the text before the language name is variable.
        # E.g. "includes: Ruby" -> "Ruby"
        # "written in Ruby" -> "Ruby"
        # "followed by Shell" -> "Shell"
        # My regex `([a-zA-Z0-9\+\-\#\.]+(?: [a-zA-Z0-9\+\-\#\.]+)*)` matches "Ruby" or "Shell".
        # It shouldn't match "written in Ruby" because "in" is a word, but "written in" has space.
        # The regex allows spaces. So "written in Ruby" might be matched?
        # Let's test the regex against "written in Ruby (1,000 bytes)"
        # match: "written in Ruby" -> group 1.
        # This is bad. I need to be careful.
        pass
    
    # Improved parsing strategy:
    # The format seems to always list languages as "Name (Bytes bytes)".
    # Common languages don't have spaces usually, except maybe "Objective C" or "C++".
    # Let's trust that the language name is the last word(s) before the parenthesis.
    # Actually, looking at the examples:
    # "Ruby (22,438 bytes)"
    # "Shell (465 bytes)"
    # The pattern is fairly clean.
    # Let's assume the language name is captured. I'll need to clean it up.
    # Usually, the list is comma separated or "and" separated or just text.
    # Wait, the structure is natural language.
    # "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
    # "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes)."
    
    # Let's extract all matches of `(\d+(?:,\d+)*) bytes` and the preceding word(s).
    # Since we can't easily predict the number of words in the language name, 
    # but we know valid languages.
    # Alternatively, just look at the captured string and take the last word if it looks like a preposition?
    # No, "C++" is not a word.
    
    # Let's try to extract just the `Name (Bytes bytes)` part.
    # We can split by `bytes)` and look backwards?
    # Or just use the regex and see what we get for the known repos.
    pass

# Let's do a specific check for the 6 repos we have.
target_repos = [item['repo_name'] for item in commits_data]
repos_lang_info = []
for repo in target_repos:
    if repo in lang_map:
        repos_lang_info.append((repo, lang_map[repo]))

print("__RESULT__:")
print(json.dumps(repos_lang_info))"""

env_args = {'var_function-call-14058082338286716352': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1405807797254836993': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-11926634395432356297': 'file_storage/function-call-11926634395432356297.json', 'var_function-call-12131814289532468915': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'facebook/react', 'commit_count': '178'}], 'var_function-call-2005433854702355848': [{'count(DISTINCT repo_name)': '6'}]}

exec(code, env_args)
