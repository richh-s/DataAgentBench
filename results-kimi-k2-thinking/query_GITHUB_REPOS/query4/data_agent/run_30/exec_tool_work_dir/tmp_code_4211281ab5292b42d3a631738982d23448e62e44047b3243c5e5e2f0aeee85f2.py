code = """import json
import re

# Get data from storage
lang_storage_key = 'var_functions.query_db:28'
lang_data = locals()[lang_storage_key]

commit_storage_key = 'var_functions.query_db:32'
commit_data = locals()[commit_storage_key]

# Parse language descriptions more carefully
repo_main_lang = {}
for item in lang_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    # Find all language entries with improved regex
    # Match patterns like: Language (1,234 bytes) or Language (123 bytes)
    lang_bytes = re.findall(r'([\w+#-]+(?:\s+[\w+#-]+)*)\s*\(([\d,]+)\s*bytes?\)', lang_desc)
    
    if lang_bytes:
        lang_dict = {}
        for lang, bytes_str in lang_bytes:
            # Remove commas from numbers
            bytes_count = int(bytes_str.replace(',', ''))
            lang_dict[lang] = bytes_count
        
        if lang_dict:
            main_lang = max(lang_dict, key=lang_dict.get)
            repo_main_lang[repo_name] = main_lang

# Process commit data
valid_repos = []
for commit_item in commit_data:
    repo_name = commit_item['repo_name']
    if repo_name in repo_main_lang:
        main_lang = repo_main_lang[repo_name]
        # Filter out Python repos
        if main_lang != 'Python':
            valid_repos.append({
                'repo_name': repo_name,
                'commit_count': int(commit_item['commit_count']),
                'main_language': main_lang
            })

# Sort by commit count descending
valid_repos_sorted = sorted(valid_repos, key=lambda x: x['commit_count'], reverse=True)

print('__RESULT__:')
print(json.dumps(valid_repos_sorted))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'type': "<class 'str'>", 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.execute_python:12': {'total_repos': 914225, 'non_python_repos': 893211, 'language_counts': {'Shell': 185349, 'CSS': 113124, 'HTML': 94995, 'Makefile': 80811, 'JavaScript': 80595, 'Ruby': 63902, 'C': 34293, 'ApacheConf': 33937, 'Batchfile': 31309, 'Python': 21014}, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'tibastral/web_motion', 'Haegin/stately', 'Scripted/pandago-ruby']}, 'var_functions.query_db:14': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:20': {'type': "<class 'list'>", 'value': "[{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode"}, 'var_functions.execute_python:22': ['twbs/bootstrap', 'Microsoft/vscode', 'tensorflow/tensorflow'], 'var_functions.query_db:24': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.execute_python:26': {'available_repos': 4, 'repo_info': [{'repo_name': 'twbs/bootstrap', 'main_language': 'PowerShell', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'main_language': 'PHP', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'main_language': 'Python', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'main_language': 'Snippet', 'commit_count': '156'}], 'missing_repos': ['torvalds/linux', 'apple/swift']}, 'var_functions.query_db:28': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_functions.execute_python:30': ['twbs/bootstrap', 'Microsoft/vscode', 'tensorflow/tensorflow'], 'var_functions.query_db:32': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:34': [], 'var_functions.execute_python:36': [{'repo_name': 'twbs/bootstrap', 'commit_count': 340, 'main_language': 'PowerShell'}, {'repo_name': 'Microsoft/vscode', 'commit_count': 190, 'main_language': 'PHP'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': 156, 'main_language': 'Snippet'}]}

exec(code, env_args)
