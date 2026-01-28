code = """languages_data = [
    {"repo_name": "torvalds/linux"},
    {"repo_name": "apple/swift", "language_description": "C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes)..."},
    {"repo_name": "twbs/bootstrap", "language_description": "JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)"},
    {"repo_name": "Microsoft/vscode", "language_description": "TypeScript (21,066,876 bytes), JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes)..."},
    {"repo_name": "facebook/react", "language_description": "JavaScript (6,256,474 bytes), HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)"},
    {"repo_name": "tensorflow/tensorflow", "language_description": "C++ (126,099,822 bytes), Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes)..."}
]

commits_data = [
    {"repo_name": "torvalds/linux", "commit_count": "16061"},
    {"repo_name": "apple/swift", "commit_count": "1051"},
    {"repo_name": "twbs/bootstrap", "commit_count": "340"},
    {"repo_name": "Microsoft/vscode", "commit_count": "190"},
    {"repo_name": "facebook/react", "commit_count": "178"},
    {"repo_name": "tensorflow/tensorflow", "commit_count": "156"}
]

import re

def extract_main_language(description):
    """Extract the main language from a language description."""
    if not description:
        return None
    
    # Parse all languages and their byte counts
    pattern = r"([A-Za-z+#-]+)\s*\(([^)]+)\s*bytes\)"
    matches = re.findall(pattern, description)
    
    if not matches:
        return None
    
    # Find the language with the maximum byte count
    max_bytes = 0
    max_language = ""
    
    for lang, bytes_str in matches:
        try:
            # Remove commas from the byte count
            bytes_str = bytes_str.replace(",", "")
            bytes_val = int(bytes_str)
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                max_language = lang.strip()
        except ValueError:
            continue
    
    return max_language

# Extract main languages for each repository
repo_info = []

for commit_data in commits_data:
    repo_name = commit_data["repo_name"]
    commit_count = int(commit_data["commit_count"])
    
    # Get language data for this repo
    lang_data = None
    for lang in languages_data:
        if lang["repo_name"] == repo_name and "language_description" in lang:
            lang_data = lang
            break
    
    if repo_name == "torvalds/linux":
        # Special case: Linux kernel is mainly C
        main_language = "C"
    else:
        # Extract main language from description
        desc = None
        if lang_data:
            desc = lang_data.get("language_description", "")
        main_language = extract_main_language(desc) if desc else None
    
    repo_info.append({
        "repo_name": repo_name,
        "commit_count": commit_count,
        "main_language": main_language
    })

# Filter out repositories whose main language is Python
non_python_repos = [repo for repo in repo_info if repo["main_language"] and repo["main_language"] != "Python"]

# Sort by commit count (descending) and get top 5
non_python_repos_sorted = sorted(non_python_repos, key=lambda x: x["commit_count"], reverse=True)
top_5_repos = non_python_repos_sorted[:5]

# Print result
print("__RESULT__:")
print(f"Top 5 non-Python repositories by commit count: {top_5_repos}")"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:5': [{'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_functions.query_db:10': [{'repo_name': 'dinahosting/dinaip-linux-grafica'}, {'repo_name': 'linuxsimba/packer-libvirt-profiles'}, {'repo_name': 'instantlinux/desviar'}, {'repo_name': 'pexip/os-util-linux'}, {'repo_name': 'ShinySide/Linux-Patches'}], 'var_functions.query_db:12': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'repo_name': 'ivanich/wireless-testing_torvalds', 'language_description': 'While most of the project is built in C (418,010,935 bytes), it also incorporates Assembly (9,191,393 bytes), Objective-C (2,292,876 bytes), C++ (1,604,022 bytes), Perl (489,655 bytes), Shell (116,793 bytes), Python (55,967 bytes), Scilab (21,433 bytes), ASP (4,528 bytes), Ruby (3,642 bytes), JavaScript (1,797 bytes), VimL (1,355 bytes).'}, {'repo_name': 'AuHau/linus-torvalds-cli-presentation', 'language_description': 'This repository is mainly written in Shell (149 bytes).'}, {'repo_name': 'jderrick/linux-torvalds', 'language_description': 'While most of the project is built in C (519,997,278 bytes), it also incorporates Assembly (10,126,330 bytes), C++ (3,334,779 bytes), Makefile (1,452,159 bytes), Perl (599,275 bytes), Objective-C (530,172 bytes), Python (175,524 bytes), Shell (163,552 bytes), Yacc (82,095 bytes), Lex (42,692 bytes), Scilab (21,433 bytes), Awk (19,627 bytes), UnrealScript (11,588 bytes), SourcePawn (4,687 bytes), Clojure (549 bytes).'}, {'repo_name': 'Linus-Torvalds/psychic-octo-sniffle', 'language_description': 'No language information available.'}, {'repo_name': 'torvalds/subsurface', 'language_description': 'This repository is mainly written in C++ (1,499,813 bytes), with additional code in C (925,754 bytes), XSLT (241,013 bytes), Shell (72,247 bytes), QML (64,225 bytes), CMake (43,823 bytes), JavaScript (40,793 bytes), HTML (33,129 bytes), CSS (12,885 bytes), Perl (9,298 bytes), QMake (9,165 bytes), R (4,070 bytes), Makefile (3,446 bytes), TeX (1,671 bytes), Objective-C (301 bytes).'}, {'repo_name': 'shabinp555/https-github.com-torvalds-linux', 'language_description': 'The majority of the code is in C (486,555,305 bytes), followed by Assembly (10,106,479 bytes), C++ (3,489,016 bytes), Objective-C (1,653,009 bytes), Makefile (1,339,557 bytes), Perl (575,838 bytes), Python (171,612 bytes), Shell (162,998 bytes), Bison (82,866 bytes), Scilab (21,433 bytes), Awk (19,627 bytes), UnrealScript (11,588 bytes), Clojure (5,263 bytes).'}, {'repo_name': 'BoringTorvalds/mirror-frontend', 'language_description': 'This repository is mainly written in JavaScript (598,898 bytes), with additional code in CSS (6,401 bytes), HTML (905 bytes).'}]}

exec(code, env_args)
