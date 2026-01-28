code = """import json, re
# Accessing previous tool results
commits = var_call_qCwbLpQUInJVz1G8vJPGUgJa
langs = var_call_b3YFq4KLyZZnzVJvdET5i5Ni

lang_map = {entry['repo_name']: entry.get('language_description') for entry in langs}

def parse_main_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    # Find patterns like: LanguageName (123,456 bytes)
    matches = re.findall(r'([A-Za-z0-9#\+\-_. ]+?)\s*\(\s*([\d,]+)\s*bytes\)', desc)
    if not matches:
        return None
    max_lang = None
    max_bytes = -1
    for name, bytes_str in matches:
        try:
            num = int(bytes_str.replace(',', ''))
        except:
            continue
        name_clean = name.strip().rstrip(',')
        if num > max_bytes:
            max_bytes = num
            max_lang = name_clean
    return max_lang

candidates = []
for rec in commits:
    repo = rec.get('repo_name')
    try:
        count = int(rec.get('commit_count'))
    except:
        try:
            count = int(str(rec.get('commit_count')).replace(',', ''))
        except:
            continue
    desc = lang_map.get(repo)
    if desc is None:
        # skip repos without language metadata (cannot determine main language)
        continue
    main = parse_main_language(desc)
    if main is None:
        # if unable to parse, skip
        continue
    if main.lower() == 'python':
        continue
    candidates.append((repo, count))

# Sort by commit count descending and take top 5
candidates.sort(key=lambda x: -x[1])
top5 = [r for r, c in candidates][:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_aZrAO8QpoMggapUfpnZyMg7K': ['languages', 'repos', 'licenses'], 'var_call_26zcsAMQ76XXpTf1dzcLrIKO': ['commits', 'contents', 'files'], 'var_call_RXUHoaxYucYLssE43jND8ZJm': 'file_storage/call_RXUHoaxYucYLssE43jND8ZJm.json', 'var_call_qCwbLpQUInJVz1G8vJPGUgJa': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_b3YFq4KLyZZnzVJvdET5i5Ni': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_gaC1lNUNLIvHftLtMP1o5wBB': []}

exec(code, env_args)
