code = """import json
import pandas as pd
import re

# Load data from previous tool calls (provided variables)
commits = var_call_Owk4FNjj6zikZYRWuMOQqv81
languages = var_call_P6ejTMCRW20JkdKczqyP7JBn
# var_call_DdWqSFa4diKpaWooukzOVcKm is empty list for linux
langs_df = pd.DataFrame(languages)
commits_df = pd.DataFrame(commits)
# convert commit_count to int
commits_df['commit_count'] = commits_df['commit_count'].astype(int)
# sort descending
commits_df = commits_df.sort_values('commit_count', ascending=False).reset_index(drop=True)

# function to determine primary language from language_description
pat = re.compile(r"([A-Za-z0-9\+\#\-. ]+?)\s*\(([\d,]+)\s*bytes\)")

def primary_language(desc):
    if not isinstance(desc, str) or desc.strip() == "":
        return None
    matches = pat.findall(desc)
    if not matches:
        # try simple heuristic: take first word before '(' or ':'
        parts = re.split(r'[:\(]', desc)
        first = parts[0]
        # attempt to extract a language-like token
        tok = first.split()[-1].strip()
        return tok if tok else None
    # choose language with max bytes
    max_lang = None
    max_bytes = -1
    for lang, bytes_str in matches:
        num = int(bytes_str.replace(',', ''))
        name = lang.strip()
        if num > max_bytes:
            max_bytes = num
            max_lang = name
    return max_lang

# build a map from repo_name to primary language
lang_map = {}
for _, row in langs_df.iterrows():
    repo = row['repo_name']
    desc = row.get('language_description', '')
    lang_map[repo] = primary_language(desc)

# Now iterate over commits_df in descending commit_count and select those whose primary language is not Python
selected = []
for _, row in commits_df.iterrows():
    repo = row['repo_name']
    primary = lang_map.get(repo, None)
    # treat None (unknown) as not Python
    if primary is None or primary.lower() != 'python':
        selected.append({'repo_name': repo, 'commit_count': int(row['commit_count']), 'primary_language': primary})
    if len(selected) >= 5:
        break

result_list = [r['repo_name'] for r in selected]
print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_call_oBf8gXU5DYGmZGkxwcYj5XjV': ['languages', 'repos', 'licenses'], 'var_call_oEutEk7EVUsslhFBsUSFOzs2': ['commits', 'contents', 'files'], 'var_call_Owk4FNjj6zikZYRWuMOQqv81': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_call_P6ejTMCRW20JkdKczqyP7JBn': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_DdWqSFa4diKpaWooukzOVcKm': []}

exec(code, env_args)
