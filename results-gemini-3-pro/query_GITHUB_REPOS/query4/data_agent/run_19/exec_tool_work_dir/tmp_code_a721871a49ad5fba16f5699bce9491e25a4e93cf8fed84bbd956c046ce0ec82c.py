code = """import json
import re

commits_data = [{"repo_name": "torvalds/linux", "commit_count": 16061}, {"repo_name": "apple/swift", "commit_count": 1051}, {"repo_name": "twbs/bootstrap", "commit_count": 340}, {"repo_name": "Microsoft/vscode", "commit_count": 190}, {"repo_name": "facebook/react", "commit_count": 178}, {"repo_name": "tensorflow/tensorflow", "commit_count": 156}]
languages_data = [{"repo_name": "tensorflow/tensorflow", "language_description": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes)."}, {"repo_name": "twbs/bootstrap", "language_description": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)."}, {"repo_name": "apple/swift", "language_description": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes)."}, {"repo_name": "facebook/react", "language_description": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)."}, {"repo_name": "Microsoft/vscode", "language_description": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."}]

# Convert lists to dicts for easier access
commits_map = {item['repo_name']: int(item['commit_count']) for item in commits_data}
langs_map = {item['repo_name']: item['language_description'] for item in languages_data}

repo_langs = []

for repo, count in commits_map.items():
    main_lang = None
    if repo in langs_map:
        desc = langs_map[repo]
        # Regex to find languages and bytes
        # Pattern example: "Ruby (22,438 bytes)"
        matches = re.findall(r'([a-zA-Z0-9\+\-\#\s]+)\s\((\d{1,3}(?:,\d{3})*) bytes\)', desc)
        
        max_bytes = 0
        for lang, byte_str in matches:
            lang = lang.strip()
            # Clean lang name from "The codebase includes: " or similar if regex caught too much?
            # My regex starts with language name, but let's be careful.
            # The regex `([a-zA-Z0-9\+\-\#\s]+)` might capture leading words if not careful.
            # But the structure is usually "Language (bytes)".
            # Let's refine regex to be safe: look for "Language (bytes)" where Language is the immediate preceding words.
            # However, simpler: the descriptions are comma separated usually or "includes: ".
            pass
        
        # Better parsing:
        # Remove "The codebase includes: " etc?
        # Let's iterate over matches.
        
        current_repo_langs = {}
        for lang, byte_str in matches:
            # lang might contain "and", "includes", etc if the regex is too greedy or text is unstructured.
            # But usually the pattern "Name (Bytes)" is distinct.
            # Clean the byte string
            bytes_val = int(byte_str.replace(',', ''))
            
            # Clean lang
            # Sometimes "Ruby"
            # Sometimes "codebase includes: Ruby" -> regex would match "Ruby" if careful
            # The regex `([a-zA-Z0-9\+\-\#\s]+)` is greedy.
            # Let's split by comma first? No, the text is natural language.
            # Let's look at specific examples.
            # "Ruby (22,438 bytes), Shell (465 bytes)."
            # "Ruby (22,438 bytes)" -> match 1: Ruby, match 2: 22,438
            
            # If the text is "The codebase includes: Ruby (22...", the regex `([a-zA-Z0-9\+\-\#\s]+)` will capture "The codebase includes: Ruby".
            # I should pick the last word or words that look like a language.
            # But languages can be multi-word like "Jupyter Notebook".
            
            # Let's use a split strategy or simpler regex.
            # The format seems to be `Language (Bytes bytes)`.
            # Let's assume the language name doesn't contain ":" or ".".
            
            lang = lang.split(':')[-1].split('.')[-1].strip()
            # Also remove "and" if it appears? "and Python (..."
            if lang.lower().startswith('and '):
                lang = lang[4:]
            
            current_repo_langs[lang] = bytes_val
        
        if current_repo_langs:
            main_lang = max(current_repo_langs, key=current_repo_langs.get)
        
    else:
        # Handle torvalds/linux or others missing
        if repo == 'torvalds/linux':
            main_lang = 'C'
        else:
            main_lang = 'Unknown'
            
    repo_langs.append({
        'repo_name': repo,
        'commit_count': count,
        'main_language': main_lang
    })

# Filter and Sort
filtered = [r for r in repo_langs if r['main_language'] != 'Python']
filtered.sort(key=lambda x: x['commit_count'], reverse=True)

top_5 = [r['repo_name'] for r in filtered[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-686105992023740660': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-3449814864305943530': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-16977174348230569550': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-10897968413967989929': [], 'var_function-call-14950388040249074906': [{'count(DISTINCT repo_name)': '6'}], 'var_function-call-10989052343025478175': 'file_storage/function-call-10989052343025478175.json'}

exec(code, env_args)
