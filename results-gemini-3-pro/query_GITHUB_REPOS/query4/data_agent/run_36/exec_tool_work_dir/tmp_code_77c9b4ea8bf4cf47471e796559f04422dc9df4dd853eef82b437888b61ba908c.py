code = """import re
import json

repo_commits = {
    "torvalds/linux": 16061,
    "apple/swift": 1051,
    "twbs/bootstrap": 340,
    "Microsoft/vscode": 190,
    "facebook/react": 178,
    "tensorflow/tensorflow": 156
}

repo_langs = {
    "tensorflow/tensorflow": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).",
    "twbs/bootstrap": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).",
    "apple/swift": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).",
    "facebook/react": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).",
    "Microsoft/vscode": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."
}

def get_main_language(desc):
    # Pattern to match "Language (bytes)"
    # Examples: "C++ (126,099,822 bytes)", "Python (42,782,002 bytes)"
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\s]+) \((\d{1,3}(?:,\d{3})*) bytes\)', desc)
    
    max_bytes = -1
    main_lang = None
    
    for lang, byte_str in matches:
        lang = lang.strip()
        byte_count = int(byte_str.replace(',', ''))
        if byte_count > max_bytes:
            max_bytes = byte_count
            main_lang = lang
            
    return main_lang

valid_repos = []
for repo, desc in repo_langs.items():
    main_lang = get_main_language(desc)
    if main_lang != 'Python':
        valid_repos.append({
            "repo_name": repo,
            "commits": repo_commits.get(repo, 0),
            "main_lang": main_lang
        })

# Sort by commits desc
valid_repos.sort(key=lambda x: x['commits'], reverse=True)

print("__RESULT__:")
print(json.dumps([r['repo_name'] for r in valid_repos]))"""

env_args = {'var_function-call-4484298634938645453': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-4484298634938645020': [{'repo_name': 'torvalds/linux', 'commit': '78e3f1f01d23c1a0d5828669d35afa2e7951987d'}, {'repo_name': 'torvalds/linux', 'commit': '4a4e07c1bdbbc24d905e4c266b92cada9371db5d'}, {'repo_name': 'torvalds/linux', 'commit': 'afe1bb73f8ed588ab6268c27c5a447fe0484e48f'}, {'repo_name': 'torvalds/linux', 'commit': 'b7ac233515c6263d6cb471d9e0f57bdd7ea36894'}, {'repo_name': 'torvalds/linux', 'commit': '71c11c378f46e42ca67c1e227646ce23bf43a8c6'}], 'var_function-call-17762877937917738903': [{'count(DISTINCT repo_name)': '6'}], 'var_function-call-16118952074507722349': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'twbs/bootstrap'}], 'var_function-call-6478610051040281873': [{'COUNT(*)': '3325634'}], 'var_function-call-7555768861814212784': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_function-call-7555768861814213299': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-14897316134430946169': [], 'var_function-call-3602150021865317023': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-17790960626389812885': 'file_storage/function-call-17790960626389812885.json', 'var_function-call-14453494884671526472': [{'repo_name': 'dinahosting/dinaip-linux-grafica', 'language_description': 'The majority of the code is in Ruby (54,423 bytes), followed by Shell (2,392 bytes).'}, {'repo_name': 'linuxsimba/packer-libvirt-profiles', 'language_description': 'The codebase includes: Shell (23,811 bytes), Ruby (11,965 bytes).'}, {'repo_name': 'instantlinux/desviar', 'language_description': 'The codebase includes: Ruby (36,344 bytes), Shell (1,854 bytes).'}, {'repo_name': 'pexip/os-util-linux', 'language_description': 'This repository is mainly written in C (4,861,385 bytes), with additional code in Makefile (1,424,739 bytes), Shell (909,014 bytes), Roff (802,856 bytes), M4 (203,114 bytes), Berry (84,168 bytes), Yacc (41,713 bytes), Python (8,511 bytes), Perl (528 bytes), sed (370 bytes).'}, {'repo_name': 'ShinySide/Linux-Patches', 'language_description': 'Nearly all of the code is in Groff, totaling 106,202 bytes.'}, {'repo_name': 'arcivanov/linuxbrew', 'language_description': 'The majority of the code is in Ruby (5,266,706 bytes), followed by Groff (29,628 bytes), Shell (21,488 bytes), Perl (608 bytes), PostScript (485 bytes).'}, {'repo_name': 'Ginfung/linux-variability-analysis-tools', 'language_description': 'The codebase includes: Scala (113,078 bytes).'}, {'repo_name': 'leutheus/linux-variability-analysis-tools.fm-translation', 'language_description': 'This repository is mainly written in Scala (151,690 bytes).'}, {'repo_name': 'ohnosequences/amazon-linux-ami', 'language_description': 'This project is built entirely in Scala (5,640 bytes of code).'}, {'repo_name': 'christinloehner/linuxcounter-update-examples', 'language_description': 'The codebase includes: Shell (37,205 bytes).'}], 'var_function-call-8470965486504387939': []}

exec(code, env_args)
