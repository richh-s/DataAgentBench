code = """import json
import re

# Load data
commits_data = locals()['var_function-call-10720339218588320447']
languages_data = locals()['var_function-call-18105978839226373612']

# Map repo_name to commit_count
repo_commits = {}
for item in commits_data:
    repo_commits[item['repo_name']] = int(item['commit_count'])

# Function to parse language description and get main language
def get_main_language(desc):
    # Regex to find Language (bytes)
    # Example: "Ruby (22,438 bytes), Shell (465 bytes)"
    # Pattern: ([a-zA-Z0-9\+\-\.\#\s]+) \((\d{1,3}(,\d{3})*) bytes\)
    matches = re.findall(r'([a-zA-Z0-9\+\-\.\#\s]+)\s\((\d{1,3}(?:,\d{3})*) bytes\)', desc)
    
    languages = []
    for lang, bytes_str in matches:
        lang = lang.strip().replace("The codebase includes: ", "").replace("The majority of the code is in ", "").replace("This repository is mainly written in ", "").replace("While most of the project is built in ", "").replace("with additional code in ", "").replace("it also incorporates ", "").replace("followed by ", "").strip()
        # Clean up language name from prefix text if regex captured too much
        # My regex ([a-zA-Z0-9\+\-\.\#\s]+) is greedy and might capture "The codebase includes: Ruby"
        # Let's refine the parsing strategy.
        pass

    # A better approach: The text is somewhat structured but variable.
    # However, the pattern "Language (Number bytes)" is consistent.
    # Let's extract just that part.
    
    raw_matches = re.findall(r'([a-zA-Z0-9\+\#\s\.\-]+)\s+\(([\d,]+)\s+bytes\)', desc)
    
    lang_stats = {}
    for r in raw_matches:
        l_name = r[0].strip()
        # Remove common prefixes from l_name if they were captured
        # These prefixes are usually at the start of the string, but regex might capture them if they are adjacent
        # The prompt examples show specific sentences.
        # "The codebase includes: Ruby (..." -> "The codebase includes: Ruby" captured.
        # split by ':' or just look at the last word(s)? Some languages have spaces "Jupyter Notebook".
        
        # Let's try to clean the language name.
        # Common noise words in the description:
        noise = ["The codebase includes:", "This repository is mainly written in", "The majority of the code is in", "While most of the project is built in", "with additional code in", "it also incorporates", "followed by", ",", "and"]
        
        for n in noise:
            if n in l_name:
                l_name = l_name.replace(n, "")
        
        l_name = l_name.strip()
        
        bytes_val = int(r[1].replace(",", ""))
        lang_stats[l_name] = bytes_val
        
    if not lang_stats:
        return None
        
    # Sort by bytes desc
    sorted_langs = sorted(lang_stats.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[0][0]

processed_repos = []

for item in languages_data:
    repo = item['repo_name']
    desc = item['language_description']
    main_lang = get_main_language(desc)
    
    if main_lang and main_lang != 'Python':
        count = repo_commits.get(repo, 0)
        processed_repos.append({'repo_name': repo, 'main_lang': main_lang, 'commits': count})

# Sort by commits desc
processed_repos.sort(key=lambda x: x['commits'], reverse=True)

# Get top 5
top_5 = [x['repo_name'] for x in processed_repos[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-3076196026403173195': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12577198480471059467': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-5703809960800587967': 'file_storage/function-call-5703809960800587967.json', 'var_function-call-10720339218588320447': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-18105978839226373612': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-17993519261610570657': []}

exec(code, env_args)
