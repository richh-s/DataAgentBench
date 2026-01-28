code = """import json
import re

# Load stored variables
commits = var_call_gHUxg4p977HFIACjR4H6Udxx  # list of dicts
langs = var_call_Xvz40Xu9YfOdchuCrSQ3zxFC  # list of dicts
files_var = var_call_b0PgNyC3jvfqH6n2Y72mOUeb  # may be file path or list

# If files_var is a path to a JSON file, load it
if isinstance(files_var, str):
    with open(files_var, 'r', encoding='utf-8') as f:
        files_data = json.load(f)
else:
    files_data = files_var

# Build languages map
lang_map = {r['repo_name']: r.get('language_description', '') for r in langs}

# Function to parse main language from description
def parse_main_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    pattern = re.compile(r"([A-Za-z0-9\+\#\- ]+?)\s*\(\s*([0-9,]+)\s*bytes\)")
    matches = pattern.findall(desc)
    if matches:
        best_lang = None
        best_bytes = -1
        for lang, bytes_str in matches:
            num = int(bytes_str.replace(',', ''))
            lang_clean = lang.strip()
            if num > best_bytes:
                best_bytes = num
                best_lang = lang_clean
        return best_lang
    m = re.search(r"mainly written in ([A-Za-z0-9\+\#\- ]+)", desc, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

# Function to infer main language from file paths
def infer_language_from_files(repo_name, files_list):
    # files_list is list of dicts with 'path'
    ext_map = {
        '.py': 'Python', '.c': 'C', '.h': 'C', '.cpp': 'C++', '.cc': 'C++', '.cxx': 'C++', '.hpp': 'C++',
        '.js': 'JavaScript', '.ts': 'TypeScript', '.java': 'Java', '.swift': 'Swift', '.go': 'Go', '.rb': 'Ruby',
        '.rs': 'Rust', '.php': 'PHP', '.scala': 'Scala', '.m': 'Objective-C', '.mm': 'Objective-C++', '.kt': 'Kotlin',
        '.sh': 'Shell', '.ps1': 'PowerShell', '.scala': 'Scala'
    }
    counts = {}
    for entry in files_list:
        p = entry.get('path') if isinstance(entry, dict) else None
        if not p:
            continue
        # Only consider paths under repo_name? files_data was for torvalds/linux only, but we'll check
        # In this dataset, files_data came from a query restricted to torvalds/linux, so assume all belong
        _, dot, ext = p.rpartition('.')
        ext = f'.{ext}' if dot else ''
        lang = ext_map.get(ext)
        if lang:
            counts[lang] = counts.get(lang, 0) + 1
    if not counts:
        return None
    # return language with max count
    return max(counts.items(), key=lambda x: x[1])[0]

# Build a mapping from repo to main language
main_lang = {}
for rec in commits:
    rn = rec.get('repo_name')
    desc = lang_map.get(rn)
    ml = parse_main_language(desc) if desc is not None else None
    # special-case: if no description and repo is torvalds/linux, infer
    if not ml and rn == 'torvalds/linux':
        ml = infer_language_from_files(rn, files_data)
    main_lang[rn] = ml

# Filter repos where main language is not Python
filtered = []
for rec in commits:
    rn = rec.get('repo_name')
    try:
        count = int(rec.get('commit_count'))
    except:
        continue
    ml = main_lang.get(rn)
    if ml is None:
        # if unknown, skip
        continue
    if ml.lower() != 'python':
        filtered.append({'repo_name': rn, 'commit_count': count, 'main_language': ml})

# Sort by commit_count desc and take top 5
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)[:5]
result = [r['repo_name'] for r in filtered_sorted]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_31OkCYRJpc2hPeWGZ88LNM6r': ['languages', 'repos', 'licenses'], 'var_call_1dqQAtFHM2YL0xbY1oRZIzit': ['commits', 'contents', 'files'], 'var_call_37oivPXvbyFi6yaBpcUQl15b': 'file_storage/call_37oivPXvbyFi6yaBpcUQl15b.json', 'var_call_gHUxg4p977HFIACjR4H6Udxx': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_3HL7kd7w4XioRS1hlmQK90cc': [], 'var_call_Xvz40Xu9YfOdchuCrSQ3zxFC': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_eLq6Sb9AltWVUSENnGmzZqQZ': [], 'var_call_b0PgNyC3jvfqH6n2Y72mOUeb': 'file_storage/call_b0PgNyC3jvfqH6n2Y72mOUeb.json'}

exec(code, env_args)
