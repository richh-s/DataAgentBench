code = """import json
# Load results from previous calls
commits_top = var_call_y8jJiUGz3Wac0Fr4orVcQfZo
langs = var_call_MvlEI0JUi1w1WpYMEY5nlwRo
# Prepare mapping from repo to commit_count (as int)
commit_map = {r['repo_name']: int(r['commit_count']) for r in commits_top}
# For each repo in commits_top, find language_description
lang_map = {r['repo_name']: r['language_description'] for r in langs}
# Combine and determine main language by parsing the language_description string
import re

def main_language(desc):
    # find patterns like "Language (number bytes)"
    # return language with largest bytes
    if not desc or desc.strip()=="":
        return None
    parts = re.findall(r"([A-Za-z+#.0-9]+) \((\d[\d,]*) bytes\)", desc)
    if not parts:
        # fallback: find first language word
        m = re.match(r"^([A-Za-z+#.0-9]+)", desc.strip())
        return m.group(1) if m else None
    # convert bytes, choose max
    best = None
    best_bytes = -1
    for lang, num in parts:
        num_clean = int(num.replace(',',''))
        if num_clean > best_bytes:
            best_bytes = num_clean
            best = lang
    return best

results = []
for r in commits_top:
    repo = r['repo_name']
    commits = int(r['commit_count'])
    lang_desc = lang_map.get(repo)
    main_lang = main_language(lang_desc) if lang_desc is not None else None
    results.append({'repo_name': repo, 'commit_count': commits, 'main_language': main_lang})

# Filter where main_language is not Python
filtered = [r for r in results if (r['main_language'] is None) or (r['main_language'].lower() != 'python')]
# Sort by commit_count desc and take top 5
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count'], reverse=True)[:5]
print('__RESULT__:')
print(json.dumps(filtered_sorted))"""

env_args = {'var_call_y8jJiUGz3Wac0Fr4orVcQfZo': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_MvlEI0JUi1w1WpYMEY5nlwRo': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_40v778aCDpjwbLvrzbNqgyqM': [], 'var_call_Xmei2bDiavXrS3GVUJJcF1ki': [{'repo_name': 'torvalds/subsurface', 'language_description': 'This repository is mainly written in C++ (1,499,813 bytes), with additional code in C (925,754 bytes), XSLT (241,013 bytes), Shell (72,247 bytes), QML (64,225 bytes), CMake (43,823 bytes), JavaScript (40,793 bytes), HTML (33,129 bytes), CSS (12,885 bytes), Perl (9,298 bytes), QMake (9,165 bytes), R (4,070 bytes), Makefile (3,446 bytes), TeX (1,671 bytes), Objective-C (301 bytes).'}], 'var_call_J65zk5XoxkMyuSppH55MMrFI': [{'sample_path': 'drivers/i2c/busses/i2c-mv64xxx.c'}]}

exec(code, env_args)
