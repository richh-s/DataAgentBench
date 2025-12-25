code = """import json
import re

# Load commit counts
commits_data = locals()['var_function-call-993125701442150257']
# Convert to a dictionary mapping repo_name -> commit_count (int)
repo_commits = {}
for entry in commits_data:
    try:
        count = int(entry['commit_count'])
        repo_commits[entry['repo_name']] = count
    except ValueError:
        continue

# Load languages data
languages_file_path = locals()['var_function-call-17748333109832134525']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Regex to extract language and bytes
# Pattern: looks for something that looks like a language name followed by "(N bytes)"
# Language names in the examples: "Ruby", "Shell", "C++", "C#", "Objective-C"
# They seem to appear as "Language (bytes)".
# Sometimes they are preceded by "in ", "includes: ", etc. but the capture group needs to handle the name.
# Let's try to capture broadly and then clean.
pattern = re.compile(r'([A-Za-z0-9\+\-\.# ]+?)\s+\(([\d,]+)\s+bytes\)')

# Function to parse language description and find main language
def get_main_language(desc):
    matches = pattern.findall(desc)
    languages = {}
    for lang_str, bytes_str in matches:
        # Clean language name
        # It might capture preceding words because the regex is greedy or non-greedy depending on context.
        # But wait, the previous words are separated by spaces.
        # e.g. "includes: Ruby" -> "Ruby" is what we want.
        # "in Ruby" -> "Ruby"
        # The captured group `([A-Za-z0-9\+\-\.# ]+?)` is non-greedy.
        # But if we have "... in Ruby (..." and we match `in Ruby`, `in` starts with lower case. 
        # Most languages in the description seem capitalized.
        # Let's clean by taking the last word(s) if it looks like a sentence structure, 
        # OR assuming the regex starts matching at the right place.
        
        # Actually, let's look at the structure again.
        # "...: Ruby (..." -> ": " is not in the char class.
        # "...in Ruby (..." -> "in " IS in the char class (space and letters).
        
        # Strategy: Split by " " and take the last part if it makes sense?
        # Better: The descriptions seem to list languages separated by commas or "and".
        # Let's just trust the regex to find `Name (Bytes)` and clean `Name`.
        # Common noise words at the start of the match: "in", "includes", "built", "written", "incorporates", "code", "of", "the", "majority", "followed", "by".
        
        clean_lang = lang_str.strip()
        words = clean_lang.split()
        
        # Heuristic: Remove common stop words from the end of the capture if they exist (unlikely) 
        # or from the start.
        stop_words = {'in', 'includes', 'built', 'written', 'incorporates', 'code', 'of', 'the', 'majority', 'followed', 'by', 'and', 'also', 'main', 'project', 'is', 'mostly', 'mainly', 'repository', 'with', 'additional', 'part'}
        
        # Filter out stop words from the start
        valid_words = []
        for w in words:
            # remove punctuation like ':'
            w_clean = w.replace(':', '')
            if w_clean.lower() not in stop_words:
                valid_words.append(w_clean)
        
        if not valid_words:
            continue
            
        final_lang_name = " ".join(valid_words)
        
        try:
            bytes_count = int(bytes_str.replace(',', ''))
            languages[final_lang_name] = bytes_count
        except ValueError:
            continue
            
    if not languages:
        return None
        
    # Find language with max bytes
    return max(languages, key=languages.get)

# Filter and collect candidates
candidates = []

for entry in languages_data:
    repo = entry['repo_name']
    desc = entry['language_description']
    
    if not desc:
        continue
        
    main_lang = get_main_language(desc)
    
    if main_lang and main_lang.lower() != 'python':
        # Check if we have commit count for this repo
        # The user query implies filtering the top 5 *of the available data* 
        # or *finding the top 5 globally*.
        # I only have commit counts for a subset of repos? 
        # Let's check if the repo exists in `repo_commits`.
        if repo in repo_commits:
            candidates.append({
                'repo_name': repo,
                'commits': repo_commits[repo],
                'main_lang': main_lang
            })

# Sort by commits descending
candidates.sort(key=lambda x: x['commits'], reverse=True)

# Get top 5
top_5 = candidates[:5]

# Prepare result
result_names = [c['repo_name'] for c in top_5]

print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_function-call-14089913042029323930': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-993125701442150257': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17748333109832134525': 'file_storage/function-call-17748333109832134525.json'}

exec(code, env_args)
