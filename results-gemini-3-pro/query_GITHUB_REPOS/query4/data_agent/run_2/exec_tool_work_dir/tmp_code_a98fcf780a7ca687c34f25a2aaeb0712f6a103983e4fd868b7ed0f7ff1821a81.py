code = """import json
import re

commits_data = locals()['var_function-call-3099508853970280112']
languages_data = locals()['var_function-call-15151662092780727701']

# Create a dict for commit counts
commit_counts = {item['repo_name']: int(item['commit_count']) for item in commits_data}

# Helper to parse language string
def get_main_language(lang_desc):
    # Regex to find Language (bytes)
    # Pattern: Name (number bytes)
    # The string looks like "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
    # or "While most of the project is built in C++ (126,099,822 bytes), it also incorporates..."
    
    # We can search for all occurrences of "([a-zA-Z0-9\+\-\#\s]+) \(([0-9,]+) bytes\)"
    # But language names can contain special chars like C++, C#, Objective-C++
    
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\s\.]+) \(([0-9,]+) bytes\)', lang_desc)
    
    languages = []
    for match in matches:
        lang_name = match[0].strip()
        # Clean up lang_name: sometimes it might have leading words like "built in " if the regex captures too much.
        # However, the structure seems to be comma separated.
        # Let's rely on the fact that the language name is immediately before " (bytes)".
        # The regex `([a-zA-Z0-9\+\-\#\s\.]+)` is greedy. 
        # Example: "built in C++" -> "built in C++". 
        # We need to be careful.
        # Let's refine the regex or parsing.
        
        # Actually, looking at the examples:
        # "Ruby (22,438 bytes), Shell (465 bytes)"
        # "built in C++ (126,099,822 bytes)"
        
        # Let's split by comma first? No, the sentence structure varies.
        pass

    # Better approach:
    # Iterate over the matches found by the regex `([A-Za-z0-9\+\#\-\.]+(?: [A-Za-z0-9\+\#\-\.]+)*) \(([0-9,]+) bytes\)`
    # The language name is usually clean enough or we can take the last word(s).
    # But languages can be multi-word like "Jupyter Notebook".
    
    # Let's just capture the bytes and the preceding string, then clean the string.
    # Common prefixes in the description: "The codebase includes:", "This repository is mainly written in", "with additional code in", "followed by", "While most of the project is built in", "it also incorporates".
    
    parsed = []
    for name_chunk, bytes_str in matches:
        byte_count = int(bytes_str.replace(',', ''))
        
        # Clean name_chunk
        name = name_chunk.strip()
        # Remove common prefixes
        prefixes = [
            "The codebase includes:", 
            "This repository is mainly written in", 
            "The majority of the code is in", 
            "While most of the project is built in",
            "it also incorporates",
            "followed by",
            "with additional code in", 
            "and"
        ]
        
        for p in prefixes:
            if name.lower().startswith(p.lower()):
                name = name[len(p):].strip()
        
        # Also, sometimes it might be "built in C++". "built in" might be part of the prefix logic or just noise.
        if name.lower().startswith("built in"):
            name = name[8:].strip()
            
        parsed.append((name, byte_count))
        
    # Sort by bytes desc
    parsed.sort(key=lambda x: x[1], reverse=True)
    
    if parsed:
        return parsed[0][0] # Main language
    return None

results = []

for lang_item in languages_data:
    repo = lang_item['repo_name']
    desc = lang_item['language_description']
    main_lang = get_main_language(desc)
    
    if repo in commit_counts:
        count = commit_counts[repo]
        results.append({
            'repo_name': repo,
            'commit_count': count,
            'main_language': main_lang
        })

# Filter not Python
final_list = [r for r in results if r['main_language'] != 'Python']

# Sort by commit count desc
final_list.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = final_list[:5]

print("__RESULT__:")
print(json.dumps([t['repo_name'] for t in top_5]))"""

env_args = {'var_function-call-15142950971022273675': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15142950971022272370': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}], 'var_function-call-3099508853970280112': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-15151662092780727701': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-16554450105515713701': []}

exec(code, env_args)
