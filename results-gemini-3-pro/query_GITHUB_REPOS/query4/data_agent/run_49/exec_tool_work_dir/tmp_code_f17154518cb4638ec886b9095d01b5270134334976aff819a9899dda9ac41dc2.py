code = """import json
import re

commits_data = [
    {"repo_name": "apple/swift", "num_commits": 1051},
    {"repo_name": "twbs/bootstrap", "num_commits": 340},
    {"repo_name": "Microsoft/vscode", "num_commits": 190},
    {"repo_name": "facebook/react", "num_commits": 178},
    {"repo_name": "tensorflow/tensorflow", "num_commits": 156}
]

languages_data = locals()['var_function-call-12174352403184281946']

repo_commits = {item['repo_name']: item['num_commits'] for item in commits_data}

def get_main_language(description):
    # Regex to find Language (Bytes)
    # Put hyphen at the end of character class
    matches = re.findall(r"([A-Za-z0-9 +#.]+?) \(([0-9,]+) bytes\)", description)
    
    languages = []
    for name, bytes_str in matches:
        bytes_val = int(bytes_str.replace(',', ''))
        name = name.strip()
        # Sometimes the name might capture preceding words if not careful, but the format seems consistent: "Name (Bytes bytes)"
        # The description usually lists them.
        # Example: "includes: Ruby (22,438 bytes)" -> matches "Ruby"
        # "built in C++ (126...)" -> matches "C++"
        languages.append((name, bytes_val))
    
    if not languages:
        return None
        
    # Sort by bytes desc
    languages.sort(key=lambda x: x[1], reverse=True)
    return languages[0][0]

results = []
for item in languages_data:
    repo = item['repo_name']
    desc = item['language_description']
    if repo in repo_commits:
        main_lang = get_main_language(desc)
        commits = repo_commits[repo]
        results.append({
            "repo_name": repo,
            "main_language": main_lang,
            "commits": commits
        })

# Filter not Python
final_repos = [r for r in results if r['main_language'] != 'Python']

# Sort by commits desc
final_repos.sort(key=lambda x: x['commits'], reverse=True)

# Top 5
top_5 = final_repos[:5]
top_5_names = [r['repo_name'] for r in top_5]

print("__RESULT__:")
print(json.dumps(top_5_names))"""

env_args = {'var_function-call-3124255539606389072': [{'repo_name': 'torvalds/linux', 'num_commits': '16061'}, {'repo_name': 'apple/swift', 'num_commits': '1051'}, {'repo_name': 'twbs/bootstrap', 'num_commits': '340'}, {'repo_name': 'Microsoft/vscode', 'num_commits': '190'}, {'repo_name': 'facebook/react', 'num_commits': '178'}, {'repo_name': 'tensorflow/tensorflow', 'num_commits': '156'}], 'var_function-call-3124255539606391359': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12174352403184281946': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-11925431017883649786': 'file_storage/function-call-11925431017883649786.json', 'var_function-call-15913131660505055244': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-793082568256913038': [{'count(DISTINCT repo_name)': '6'}]}

exec(code, env_args)
