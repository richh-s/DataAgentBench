code = """import json
import re
# Access stored variables
commits = var_call_qPd5h8uki4snTRZZBTPGBaSW
langs_subset = var_call_S0cW2kdgXYLDzlfnTMZRMhCn
langs_missing = var_call_wqOwkvJb2h8YM5aJgEaLzdDm
langs_file_path = var_call_a16TlIUhm9B3OyvKzQKdZuVn

# Load the full languages list from file if it's a filepath
full_langs = []
if isinstance(langs_file_path, str):
    with open(langs_file_path, 'r', encoding='utf-8') as f:
        full_langs = json.load(f)
elif isinstance(langs_file_path, list):
    full_langs = langs_file_path

# Build mapping repo_name -> language_description from full_langs
lang_map = {}
for rec in full_langs:
    rn = rec.get('repo_name')
    ld = rec.get('language_description')
    if rn and ld:
        lang_map[rn] = ld
# Merge in subset and missing (which may overwrite but should be same)
for rec in langs_subset:
    rn = rec.get('repo_name')
    ld = rec.get('language_description')
    if rn and ld:
        lang_map[rn] = ld
for rec in langs_missing:
    rn = rec.get('repo_name')
    ld = rec.get('language_description')
    if rn and ld:
        lang_map[rn] = ld

# Function to extract primary language from language_description
pat = re.compile(r"([A-Za-z0-9\+\#\._ ]+?) \(([\d,]+) bytes\)")

def primary_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        # try alternative patterns like 'mainly written in Language (number bytes)'
        alt = re.findall(r"([A-Za-z0-9\+\#\._ ]+?) \(([\d,]+)\)", desc)
        matches = alt
    if not matches:
        # As a fallback, try to find first language word capitalized
        m = re.search(r"(mainly written in|The majority of the code is in|While most of the project is built in) ([A-Za-z0-9\+\#\._ ]+)", desc)
        if m:
            return m.group(2).strip()
        return None
    # Convert bytes to int and pick max
    best_lang = None
    best_bytes = -1
    for lang, bytes_str in matches:
        num = int(bytes_str.replace(',', ''))
        lang_clean = lang.strip()
        if num > best_bytes:
            best_bytes = num
            best_lang = lang_clean
    return best_lang

# Build primary language map for repos in commits
results = []
for rec in commits:
    repo = rec.get('repo_name')
    cnt = rec.get('commit_count')
    try:
        cnt = int(cnt)
    except:
        try:
            cnt = int(float(cnt))
        except:
            cnt = 0
    desc = lang_map.get(repo)
    prim = primary_language(desc)
    results.append({'repo_name': repo, 'commit_count': cnt, 'primary_language': prim, 'language_description': desc})

# Filter out those whose primary language is Python (case-insensitive)
filtered = [r for r in results if not (r['primary_language'] and r['primary_language'].strip().lower() == 'python')]
# Also exclude if primary_language is None (unknown) to be conservative
filtered = [r for r in filtered if r['primary_language']]

# Sort by commit_count descending
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)
# Take top five
top5 = filtered_sorted[:5]
# Prepare output list of repo names in order
top5_repos = [r['repo_name'] for r in top5]

out = json.dumps(top5_repos)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_qPd5h8uki4snTRZZBTPGBaSW': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}], 'var_call_a16TlIUhm9B3OyvKzQKdZuVn': 'file_storage/call_a16TlIUhm9B3OyvKzQKdZuVn.json', 'var_call_S0cW2kdgXYLDzlfnTMZRMhCn': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_wqOwkvJb2h8YM5aJgEaLzdDm': []}

exec(code, env_args)
