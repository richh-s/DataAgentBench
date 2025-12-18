code = """import json
import re
import pandas as pd

# Load the language data from the previous step
with open(locals()['var_function-call-15828829545132002990'], 'r') as f:
    languages_data = json.load(f)

# Prepare a list to store repository names whose main language is not Python
non_python_main_language_repos = []

for repo_info in languages_data:
    repo_name = repo_info['repo_name']
    description = repo_info['language_description']

    language_bytes = {}
    # Regex to find language and byte count. Handles commas in byte counts.
    matches = re.findall(r'([a-zA-Z0-9+#-]+)\s+\(([\d,]+)\s+bytes\)', description)
    for lang, byte_count_str in matches:
        language_bytes[lang] = int(byte_count_str.replace(',', ''))

    if language_bytes:
        # Find the language with the maximum byte count
        main_language = max(language_bytes, key=language_bytes.get)
        if main_language != 'Python':
            non_python_main_language_repos.append(repo_name)

# Remove duplicate repository names if any
non_python_main_language_repos = list(set(non_python_main_language_repos))

# Prepare the result for the next tool call
print("__RESULT__:")
print(json.dumps({"non_python_main_language_repos": non_python_main_language_repos}))"""

env_args = {'var_function-call-2340926761176457406': 'file_storage/function-call-2340926761176457406.json', 'var_function-call-13863585805078690205': 'file_storage/function-call-13863585805078690205.json', 'var_function-call-8689555944964674122': 'file_storage/function-call-8689555944964674122.json', 'var_function-call-3767942551275076807': [], 'var_function-call-8917675196223738767': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-2689555683014066056': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-8429983972344603568': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17346842645571104268': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-13315386200547261605': {'query': "SELECT repo_name, language_description FROM languages WHERE repo_name IN ('torvalds/linux', 'apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react');"}, 'var_function-call-2669334337497921648': [{'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-446953779997160791': 'file_storage/function-call-446953779997160791.json', 'var_function-call-2550803593441403300': 'file_storage/function-call-2550803593441403300.json', 'var_function-call-969932074112391872': 'file_storage/function-call-969932074112391872.json', 'var_function-call-11894990576406263134': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-6612999448854114548': 'file_storage/function-call-6612999448854114548.json', 'var_function-call-5884717469768522957': 'file_storage/function-call-5884717469768522957.json', 'var_function-call-7543182874213555558': 'file_storage/function-call-7543182874213555558.json', 'var_function-call-14543911196145242349': 'file_storage/function-call-14543911196145242349.json', 'var_function-call-2886024573394915013': 'file_storage/function-call-2886024573394915013.json', 'var_function-call-18438416596286588483': 'file_storage/function-call-18438416596286588483.json', 'var_function-call-15828829545132002990': 'file_storage/function-call-15828829545132002990.json', 'var_function-call-6476213616587755942': 'file_storage/function-call-6476213616587755942.json', 'var_function-call-10322922487115648317': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}]}

exec(code, env_args)
