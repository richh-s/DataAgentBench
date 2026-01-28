code = """import json, re, os

commits = var_call_gEGtyWcOnho3r2w7Qh1L2Amd
lang_records = var_call_j6qB4zCysKs2R4uyz9Isw6Z5
files_json_path = var_call_JOjJXZx0smEqT2wKhBm0Su5E

# Parse languages descriptions to find the language with max bytes
lang_map = {}
pat = re.compile(r"([A-Za-z0-9+#\-\._ ]+?)\s*\(([0-9,]+) bytes\)")
for rec in lang_records:
    repo = rec.get('repo_name')
    desc = rec.get('language_description','')
    matches = pat.findall(desc)
    max_lang = None
    max_bytes = -1
    for lang, bstr in matches:
        try:
            b = int(bstr.replace(',',''))
        except:
            continue
        if b > max_bytes:
            max_bytes = b
            max_lang = lang.strip()
    if max_lang:
        lang_map[repo] = max_lang

# For torvalds/linux, if not in lang_map, infer from files extensions
inferred_main = None
if isinstance(files_json_path, str) and os.path.exists(files_json_path):
    with open(files_json_path, 'r', encoding='utf-8') as f:
        files_list = json.load(f)
    # normalize extension->language map (lowercase keys)
    ext_lang = {
        '.py': 'Python',
        '.c': 'C',
        '.h': 'C',
        '.cpp': 'C++',
        '.cc': 'C++',
        '.cxx': 'C++',
        '.c++': 'C++',
        '.hpp': 'C++',
        '.s': 'Assembly',
        '.java': 'Java',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.swift': 'Swift',
        '.rb': 'Ruby',
        '.m': 'Objective-C',
        '.mm': 'Objective-C++',
        '.rs': 'Rust',
        '.sh': 'Shell',
        '.pl': 'Perl',
        '.php': 'PHP',
        '.scala': 'Scala',
        '.hs': 'Haskell',
        '.erl': 'Erlang',
        '.ex': 'Elixir',
        '.exs': 'Elixir',
        '.kt': 'Kotlin',
        '.dart': 'Dart',
        '.cs': 'C#',
        '.lua': 'Lua',
        '.vb': 'Visual Basic',
        '.asm': 'Assembly',
    }
    ext_counts = {}
    for entry in files_list:
        path = entry.get('path') if isinstance(entry, dict) else None
        if not path:
            continue
        _, ext = os.path.splitext(path)
        ext = ext.lower()
        if not ext:
            continue
        lang = ext_lang.get(ext)
        if not lang:
            # treat .h as C already included
            continue
        ext_counts[lang] = ext_counts.get(lang, 0) + 1
    if ext_counts:
        inferred_main = max(ext_counts.items(), key=lambda x: x[1])[0]

# Build final list
repos_info = []
for rec in commits:
    repo = rec.get('repo_name')
    ccount = int(rec.get('commit_count') or 0)
    main_lang = lang_map.get(repo)
    if not main_lang and repo == 'torvalds/linux':
        main_lang = inferred_main
    repos_info.append({'repo_name': repo, 'commit_count': ccount, 'main_language': main_lang})

# Filter out repos whose main language is Python
filtered = [r for r in repos_info if not (r['main_language'] and r['main_language'].strip().lower() == 'python')]
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)[:5]
result = [r['repo_name'] for r in filtered_sorted]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QHqo4zFNKBZeLwZTb9IgnaCD': ['languages', 'repos', 'licenses'], 'var_call_l1IqFOIS5hbQoeM9ZGIxi3X2': ['commits', 'contents', 'files'], 'var_call_7133Z8MPHfy827ouLWOFME22': 'file_storage/call_7133Z8MPHfy827ouLWOFME22.json', 'var_call_gEGtyWcOnho3r2w7Qh1L2Amd': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_j6qB4zCysKs2R4uyz9Isw6Z5': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_pmKLe9WQiBpZZGUrozdqJBgh': [], 'var_call_JOjJXZx0smEqT2wKhBm0Su5E': 'file_storage/call_JOjJXZx0smEqT2wKhBm0Su5E.json'}

exec(code, env_args)
