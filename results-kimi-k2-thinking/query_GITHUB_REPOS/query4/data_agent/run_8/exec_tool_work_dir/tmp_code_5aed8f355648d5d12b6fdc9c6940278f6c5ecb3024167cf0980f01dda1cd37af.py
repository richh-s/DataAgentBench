code = """import json
import re

# Read language file
file_path = locals()['var_functions.query_db:14']
with open(file_path, 'r') as f:
    all_languages = json.load(f)

# Get commit counts from both queries
commit_counts = locals()['var_functions.query_db:22']

# Build language lookup
data = []
for commit_entry in commit_counts:
    repo_name = commit_entry['repo_name']
    commit_count = int(commit_entry['commit_count'])
    
    # Find language description
    lang_desc = None
    for lang_entry in all_languages:
        if lang_entry['repo_name'] == repo_name:
            lang_desc = lang_entry['language_description']
            break
    
    if lang_desc:
        # Parse languages and bytes
        lang_bytes = {}
        pattern = r'([A-Za-z#+]+)\s*\(([\d,]+)\s+bytes\)'
        matches = re.findall(pattern, lang_desc)
        
        for lang, bytes_str in matches:
            lang = lang.strip()
            bytes_val = int(bytes_str.replace(',', ''))
            lang_bytes[lang] = bytes_val
        
        # Get main language
        main_lang = max(lang_bytes, key=lang_bytes.get) if lang_bytes else None
        
        data.append({
            'repo_name': repo_name,
            'commit_count': commit_count,
            'main_language': main_lang,
            'all_languages': lang_bytes
        })

# Filter for non-Python repos
non_python = [repo for repo in data if repo['main_language'] != 'Python']

# Sort by commit count descending
non_python_sorted = sorted(non_python, key=lambda x: x['commit_count'], reverse=True)

# Get top 5
result = non_python_sorted[:5]

# Prepare final answer
answer = []
for repo in result:
    answer.append(f"{repo['repo_name']}")

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'torvalds/linux', 'commit': '78e3f1f01d23c1a0d5828669d35afa2e7951987d'}, {'repo_name': 'torvalds/linux', 'commit': '4a4e07c1bdbbc24d905e4c266b92cada9371db5d'}, {'repo_name': 'torvalds/linux', 'commit': 'afe1bb73f8ed588ab6268c27c5a447fe0484e48f'}, {'repo_name': 'torvalds/linux', 'commit': 'b7ac233515c6263d6cb471d9e0f57bdd7ea36894'}, {'repo_name': 'torvalds/linux', 'commit': '71c11c378f46e42ca67c1e227646ce23bf43a8c6'}, {'repo_name': 'torvalds/linux', 'commit': '76cdd58e558669366adfaded436fda01b30cce3e'}, {'repo_name': 'torvalds/linux', 'commit': '2565409fc0303f3ab8d66b8326702a687962a29b'}, {'repo_name': 'torvalds/linux', 'commit': '7779d7bed950a7fb1af4f540c2f82a6b81b65901'}, {'repo_name': 'torvalds/linux', 'commit': '3443ad095fc330ace0ef23bf965354a56298bf58'}, {'repo_name': 'torvalds/linux', 'commit': '42e41c54d61e32e8a349943607daa53205324d7f'}], 'var_functions.list_db:5': ['languages', 'repos', 'licenses'], 'var_functions.query_db:6': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:8': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_functions.execute_python:10': {'main_languages': {'tensorflow/tensorflow': {'main_language': 'Python', 'bytes': 42782002}, 'twbs/bootstrap': {'main_language': 'JavaScript', 'bytes': 865640}, 'apple/swift': {'main_language': 'Swift', 'bytes': 41439628}, 'facebook/react': {'main_language': 'JavaScript', 'bytes': 6256474}, 'Microsoft/vscode': {'main_language': 'TypeScript', 'bytes': 21066876}}, 'commit_counts': {'torvalds/linux': 16061, 'apple/swift': 1051, 'twbs/bootstrap': 340, 'Microsoft/vscode': 190, 'facebook/react': 178, 'tensorflow/tensorflow': 156}, 'linux_lang_found': False}, 'var_functions.execute_python:12': {'status': 'need_more_data'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [], 'var_functions.query_db:18': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:20': {'total_repos_with_lang': 3325634, 'total_repos_in_commit_counts': 6, 'common_repos_count': 5, 'common_repos': ['Microsoft/vscode', 'apple/swift', 'facebook/react', 'tensorflow/tensorflow', 'twbs/bootstrap']}, 'var_functions.query_db:22': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:24': [{'repository': 'apple/swift', 'main_language': 'Swift', 'commits': 1051}, {'repository': 'twbs/bootstrap', 'main_language': 'JavaScript', 'commits': 340}, {'repository': 'Microsoft/vscode', 'main_language': 'TypeScript', 'commits': 190}, {'repository': 'facebook/react', 'main_language': 'JavaScript', 'commits': 178}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': [{'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
