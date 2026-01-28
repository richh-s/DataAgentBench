code = """import json
import re

# Load data from previous tool calls
commits = var_call_V4B9raBacpNEITFvHI2WE2CW
langs_partial = var_call_lmH9Xz56FgVPuZcRCWWz4Rdw
linux_counts = var_call_kUIn1feUg28nuQUsaGkj91U8

# build languages dict from langs_partial
lang_map = {entry['repo_name']: entry.get('language_description') for entry in langs_partial}

def parse_main_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    # find all occurrences like "Language (123,456 bytes)" or "Language (123 bytes)"
    pattern = r"([A-Za-z+#+\-\. ]+?)\s*\((?:[\d,]+) bytes\)"
    matches = re.findall(pattern, desc)
    if not matches:
        # try alternative phrasing 'mainly written in X (123 bytes)'
        pattern2 = r"written in ([A-Za-z+#+\-\. ]+?)\s*\((?:[\d,]+) bytes\)"
        m2 = re.findall(pattern2, desc)
        if m2:
            return m2[0].strip()
        return None
    # Now extract numbers too to pick the largest
    pattern_num = r"([A-Za-z+#+\-\. ]+?)\s*\(([\d,]+) bytes\)"
    matches_num = re.findall(pattern_num, desc)
    if not matches_num:
        return matches[0].strip()
    # convert and pick max
    max_lang = None
    max_bytes = -1
    for lang, num in matches_num:
        try:
            val = int(num.replace(',', ''))
        except:
            val = 0
        if val > max_bytes:
            max_bytes = val
            max_lang = lang.strip()
    return max_lang

selected = []
for entry in commits:
    repo = entry['repo_name']
    if len(selected) >= 5:
        break
    main_lang = None
    if repo in lang_map and lang_map[repo]:
        main_lang = parse_main_language(lang_map[repo])
    else:
        # fallback for linux using file extension counts
        if repo == 'torvalds/linux' and linux_counts and isinstance(linux_counts, list) and linux_counts[0]:
            counts = linux_counts[0]
            # simple heuristic: if c_count > 0 consider C as main
            try:
                if float(counts.get('c_count', 0)) > 0:
                    main_lang = 'C'
            except:
                main_lang = None
    if main_lang is None:
        # if unknown, assume not Python to be conservative? But safer to skip
        # We'll skip unknown to avoid false positives
        continue
    if main_lang.lower() != 'python':
        selected.append(repo)

# Ensure we have 5; if not, continue scanning commits beyond initial limit
if len(selected) < 5:
    # try to include remaining commits entries beyond first few
    for entry in commits:
        repo = entry['repo_name']
        if repo in selected:
            continue
        main_lang = None
        if repo in lang_map and lang_map[repo]:
            main_lang = parse_main_language(lang_map[repo])
        if main_lang and main_lang.lower() != 'python':
            selected.append(repo)
        if len(selected) >= 5:
            break

# prepare JSON-serializable string
result_str = json.dumps(selected)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_JVie3WkCFLL4CBrAiQMYqbsX': ['languages', 'repos', 'licenses'], 'var_call_fyRpuqE38ov4Midyzasc2M9H': ['commits', 'contents', 'files'], 'var_call_aamvbKKC2mN4eC02YEcQ6jBz': 'file_storage/call_aamvbKKC2mN4eC02YEcQ6jBz.json', 'var_call_V4B9raBacpNEITFvHI2WE2CW': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_lmH9Xz56FgVPuZcRCWWz4Rdw': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_5y6ChfYeO5Cz7aydSVIk5zes': [], 'var_call_xA4o9OmwD3uEh6VsB3vGDGMT': [{'sample_path': 'drivers/i2c/busses/i2c-mv64xxx.c', 'repo_data_description': 'The dataset includes this non-binary file, 27802 bytes in size and copied 235 times (mode: 33188).'}], 'var_call_kUIn1feUg28nuQUsaGkj91U8': [{'c_count': '1.0', 'h_count': '0.0', 'cpp_count': '0.0', 'py_count': '0.0', 'rs_count': '0.0', 'java_count': '0.0'}]}

exec(code, env_args)
