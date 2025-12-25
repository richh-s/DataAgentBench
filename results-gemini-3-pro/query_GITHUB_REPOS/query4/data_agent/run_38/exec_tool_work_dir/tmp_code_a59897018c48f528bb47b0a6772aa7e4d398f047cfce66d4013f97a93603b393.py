code = """import pandas as pd
import json
import re

# Load data
commits_data = locals()['var_function-call-1996706631264366614']
languages_data = locals()['var_function-call-17443207135755333322']

# Convert to dataframes
df_commits = pd.DataFrame(commits_data)
df_commits['commit_count'] = df_commits['commit_count'].astype(int)

df_languages = pd.DataFrame(languages_data)

# Merge
df = pd.merge(df_commits, df_languages, on='repo_name', how='inner')

# Function to parse language description and find main language
def get_main_language(desc):
    if not desc:
        return None
    # Pattern to extract Language and Bytes
    # Example: "Ruby (22,438 bytes)"
    # Regex: ([a-zA-Z0-9\+\#\s]+) \((\d{1,3}(?:,\d{3})*) bytes\)
    # Need to be careful with parsing the text structure
    
    # Simple strategy: find all matches of "Language (Bytes bytes)"
    # The text usually lists them.
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\s\.]+) \((\d[\d,]*) bytes\)', desc)
    
    lang_stats = {}
    for lang, bytes_str in matches:
        lang = lang.strip()
        # Clean up lang name from preceding text if any (e.g. "includes: Ruby")
        # The regex might capture "includes: Ruby". 
        # Looking at the examples: "Ruby (22,438 bytes), Shell (465 bytes)."
        # "incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes)..."
        
        # Let's refine regex to be more strict or clean up after.
        # Common languages: C++, Python, JavaScript, etc.
        # The capture group 1 might contain "The codebase includes: Ruby"
        # We can split by space and take the last word? No, "Objective-C++" or "Jupyter Notebook".
        
        # Better approach: The format seems to be "Language (Bytes bytes)".
        # The text before the language name is usually spaces or punctuation or introductory text.
        # Let's try to locate the open parenthesis and work backwards?
        
        # Let's stick to the regex but clean the language name.
        # usually language names don't have ":" or "includes". 
        # If "includes: Ruby", split by ": " and take last.
        if ":" in lang:
            lang = lang.split(":")[-1].strip()
        if "incorporates" in lang:
             lang = lang.split("incorporates")[-1].strip()
        
        # Remove common stopwords if stuck
        words = lang.split()
        if words and words[0].lower() in ['and', 'or', 'in', 'includes', 'incorporates', 'code', 'is', 'written', 'mainly', 'project', 'built']:
            # This is risky. 
            # Let's look at the specific descriptions provided.
            # "The codebase includes: Ruby (..." -> lang="The codebase includes: Ruby" -> split ":" -> "Ruby"
            # "While most of the project is built in C++ (..." -> lang="While most of the project is built in C++"
            # "The majority of the code is in Ruby (..."
            
            # Strategy: look for known languages or just take the last few words. 
            # Most languages are 1-3 words.
            pass
            
        bytes_count = int(bytes_str.replace(',', ''))
        lang_stats[lang] = bytes_count
        
    if not lang_stats:
        return None
    
    # Find max bytes
    main_lang = max(lang_stats, key=lang_stats.get)
    
    # specific cleanup for the extracted main_lang string
    # "While most of the project is built in C++" -> we need "C++"
    # We can try to match the language name against a known list or heuristics.
    # Heuristic: The language name is at the end of the captured string.
    # "built in C++" -> "C++"
    
    # Let's just take the last word? No "Jupyter Notebook".
    # Let's take the string after the last lowercase word?
    # Or just looking at the provided examples:
    # "built in C++" -> "C++"
    # "code is in Ruby" -> "Ruby"
    # "includes: Ruby" -> "Ruby"
    
    # We can assume the language name starts with an Uppercase letter (mostly, except iOS etc? but here they seem capitalized).
    # And allows special chars like +, #.
    # Let's re-parse using a better regex for the whole string.
    
    return main_lang, lang_stats[main_lang]

# Better parsing within the loop
# We can just extract all "Name (Count bytes)" and then for each name, clean it.
# The name is likely the tokens immediately preceding the " (".
# But "Jupyter Notebook (" has 2 tokens.
# "Objective-C++ (" has 1.

# Let's try to extract cleanly.
parsed_data = []
for index, row in df.iterrows():
    desc = row['language_description']
    # Find all pattern occurrences
    # We look for: <Language Name> (<Bytes> bytes)
    # The Language Name can be multiple words.
    # It usually follows a space, comma, or start of line.
    # But also words like "in", "includes:".
    
    # Let's use the property that language names are usually Capitalized.
    # Regex:  (?:in|includes:|by|,)\s+([A-Z0-9][a-zA-Z0-9\+\-\#\s\.]*?)\s*\((\d[\d,]*)\s*bytes\)
    # This might miss "C++" if it follows something else.
    
    # Let's iterate over all `(... bytes)` matches and look at text before it.
    
    matches = list(re.finditer(r'([^\(\)\,]+?)\s*\((\d[\d,]*)\s*bytes\)', desc))
    
    repo_langs = {}
    for m in matches:
        raw_lang = m.group(1).strip()
        bytes_count = int(m.group(2).replace(',', ''))
        
        # Clean raw_lang
        # remove "The codebase includes:"
        # remove "While most of the project is built in"
        # remove "followed by"
        # remove "The majority of the code is in"
        
        tokens = raw_lang.split()
        # Take from the end until we hit a lowercase word (excluding 'C++', 'C#', etc which are fine)
        # or a stopword.
        
        # Keywords to stop at (reading backwards):
        stop_words = ["in", "by", "includes:", "incorporates", "code", "project", "language"]
        
        clean_lang = []
        for token in reversed(tokens):
            if token in stop_words or token.endswith(':'):
                break
            clean_lang.insert(0, token)
        
        lang_name = " ".join(clean_lang)
        # Fix for "C++" being stuck to something? No, space split handles it.
        # Fix for "Objective-C++"
        
        if lang_name:
            repo_langs[lang_name] = bytes_count
            
    if repo_langs:
        main_lang = max(repo_langs, key=repo_langs.get)
        parsed_data.append({'repo_name': row['repo_name'], 'main_language': main_lang, 'commit_count': row['commit_count']})

result_df = pd.DataFrame(parsed_data)
# Filter out Python
# Careful with "Python" vs "python"
result_df = result_df[result_df['main_language'] != 'Python']

# Sort by commit_count desc
result_df = result_df.sort_values('commit_count', ascending=False)

print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-17405164670818123081': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1996706631264366614': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17443207135755333322': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-10697510515514900360': 'file_storage/function-call-10697510515514900360.json', 'var_function-call-1405919473621303940': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-2272947150352257507': [], 'var_function-call-13621845005973201119': [{'count(DISTINCT repo_name)': '6'}]}

exec(code, env_args)
