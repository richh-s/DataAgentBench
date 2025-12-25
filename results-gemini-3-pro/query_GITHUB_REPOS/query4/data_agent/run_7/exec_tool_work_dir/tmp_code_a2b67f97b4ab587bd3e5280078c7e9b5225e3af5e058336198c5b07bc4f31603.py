code = """import json
import re
import pandas as pd

# Load commits data
# The previous result was not a file, so it's a list variable
commits_data = locals()['var_function-call-15279119177356948517']
# commits_data is a list of dicts: [{'repo_name': '...', 'commit_count': '...'}]

# Load languages data
# The previous result was a file
languages_file_path = locals()['var_function-call-15657998434769201345']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Convert languages to a dict for easy lookup
# repo_name -> language_description
lang_dict = {item['repo_name']: item['language_description'] for item in languages_data}

def get_main_language(description):
    if not description:
        return None
    # Regex to find Language and Bytes
    # Pattern looks for: Language Name (X bytes)
    # Handling comma in numbers
    # Language name can be multiple words? Usually "Ruby", "Shell", "C++", "C#".
    # Based on examples: "Ruby (22,438 bytes)", "Shell (465 bytes)"
    # Some descriptions have text before.
    
    # We can search for all occurrences of: ([A-Za-z0-9\+\-\#\.\s]+) \(([0-9,]+) bytes\)
    # But we must be careful not to capture "The codebase includes: " as part of the language name.
    # The format seems to be: Language (Bytes)
    # Let's try to split by commas or just find all matches.
    
    # Let's assume the language name is immediately before " ("
    matches = re.findall(r'([A-Za-z0-9\+\-\#\.\s]+)\s\(([0-9,]+)\sbytes\)', description)
    
    if not matches:
        return None
    
    # Process matches
    parsed_langs = []
    for lang_str, bytes_str in matches:
        # Clean language name (remove leading "includes:", "written in", etc if possible, but the regex captures preceding words)
        # Actually, looking at "The codebase includes: Ruby (22,438 bytes)"
        # Match 1: "The codebase includes: Ruby"
        # This is bad.
        
        # Better approach:
        # The languages seem to be capitalized and standard names.
        # But "The codebase includes: " is present.
        # Let's look closer at the structure.
        # "Ruby (22,438 bytes), Shell (465 bytes)."
        # It seems languages are separated by comma or text.
        
        # Let's try to match the pattern `Language (Bytes)` where Language does not contain "includes:" etc.
        # But I don't know the list of all languages.
        
        # Heuristic: The language name is usually the last word(s) before " (".
        # Let's strip the captured group.
        
        # If I capture `([A-Za-z0-9\+\-\#\.]+) \(([0-9,]+) bytes\)` (no space in lang name except maybe "C++")
        # "Visual Basic" has space.
        
        # Let's try to be more specific.
        # We can extract the byte count and the word immediately preceding it.
        pass

    # Alternative regex:
    # Find `(bytes)` and look back?
    # Let's iterate over the string.
    
    # Let's try a regex that captures the last few words before the open parenthesis.
    # But "The codebase includes: Ruby" -> "Ruby"
    # "mainly written in Ruby" -> "Ruby"
    # "incorporates Shell" -> "Shell"
    # "followed by Shell" -> "Shell"
    
    # It seems the language name is always the noun phrase before the parenthesis.
    # Common prefixes: ": ", "in ", "by ", "includes: ".
    
    # Let's try to split the string by `(` and take the part before.
    
    lang_stats = []
    # Split by closing parenthesis to get chunks like "..., Shell (115 bytes)"
    # But first, let's just use a regex that assumes the language name doesn't contain standard sentence words like "includes", "in", "by".
    # Or, we can look at the Capitalized words? "Ruby", "Shell".
    
    # Let's try this:
    # 1. Find all `([0-9,]+) bytes` to get the numbers.
    # 2. For each number, look at the text immediately preceding the ` (`.
    # 3. Clean that text.
    
    raw_matches = re.finditer(r'\(([0-9,]+) bytes\)', description)
    
    for m in raw_matches:
        bytes_val = int(m.group(1).replace(',', ''))
        end_idx = m.start()
        # Look backwards from end_idx
        # Text before is like "... includes: Ruby "
        # We want "Ruby".
        
        # Grab, say, 50 chars before.
        pre_text = description[max(0, end_idx-50):end_idx].strip()
        
        # The language name is at the end of pre_text.
        # It is likely preceded by ":", "in", "by", ",", or is at the start.
        # Let's tokenize by space and take the last word?
        # What about "Objective-C"? Single token.
        # "Visual Basic"? Two tokens.
        
        # Let's try splitting by common delimiters: ":", "in ", "by ", ", ", ". "
        # And take the last segment.
        
        # A simple robust way: split by space, take the last token, if it looks like a language.
        # If the last token is "C", check previous? "Objective C"?
        
        # Let's assume language names are Capitalized.
        # Take all words at the end of pre_text that are capitalized?
        # "Shell" -> Capitalized.
        # "Ruby" -> Capitalized.
        
        words = pre_text.split()
        if not words:
            continue
            
        lang_name = words[-1]
        # Handle "Objective-C" (one word)
        # Handle "C++" (one word)
        # Handle "Visual Basic" ?
        # If words[-1] is "Basic", check words[-2] is "Visual".
        
        # Let's just store the last word for now, and see if it makes sense.
        # Most repos in the example are single-word languages: Ruby, Shell.
        
        # Let's do a quick check for common multi-word langs if needed.
        # But for the purpose of "Python", "Python" is single word.
        # So if I find "Python", I exclude.
        
        lang_stats.append((lang_name, bytes_val))
        
    if not lang_stats:
        return None
        
    # Sort by bytes desc
    lang_stats.sort(key=lambda x: x[1], reverse=True)
    return lang_stats[0][0]

repo_infos = []

for repo_dict in commits_data:
    repo_name = repo_dict['repo_name']
    commit_count = int(repo_dict['commit_count'])
    
    desc = lang_dict.get(repo_name)
    main_lang = get_main_language(desc)
    
    repo_infos.append({
        'repo_name': repo_name,
        'commit_count': commit_count,
        'main_lang': main_lang
    })

# Filter out Python
# "Python" might be "Python" or "python" (usually capitalized in description)
# But we should check carefully.
filtered_repos = []
for r in repo_infos:
    lang = r['main_lang']
    if lang and 'Python' in lang: # "Python" or "IPython" etc? Just "Python".
        # If lang is "Python", exclude.
        pass
    else:
        # Include
        # Also include if lang is None? (No language info). 
        # The query asks for repos "whose main language is not Python".
        # If unknown, it's not Python.
        # But usually we should have metadata.
        # Let's just strictly exclude if main_lang == "Python"
        if lang != "Python":
            filtered_repos.append(r)

# Sort by commit count desc
filtered_repos.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = filtered_repos[:5]

result = [r['repo_name'] for r in top_5]
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5286727036878620176': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15279119177356948517': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-15657998434769201345': 'file_storage/function-call-15657998434769201345.json'}

exec(code, env_args)
